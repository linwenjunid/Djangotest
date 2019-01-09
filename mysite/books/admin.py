from django.contrib import admin
from django.http import HttpResponseRedirect
from .models import Publisher, Author, Book, Tag
from django.contrib.auth.models import User


class TagInline(admin.TabularInline):
    model = Tag
    extra = 1


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','address','city','state_province','country','website')
    list_editable = ('address',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # 自定义动作 复制一条记录
    def copy_one(self, request, queryset):
        if queryset.count() == 1:
            old_data = queryset.values()[0]
            old_data.pop('id')
            new_data = Book.objects.create(**old_data)
            return HttpResponseRedirect('{}{}/change'.format(request.path, new_data.id))
        else:
            self.message_user(request, "只能选取一条数据！")
    copy_one.short_description = '复制所选数据'
    actions = [copy_one]

    # 不同的用户显示不同的操作
    def get_actions(self, request):
        actions = super(BookAdmin, self).get_actions(request)
        if request.user.is_superuser:
            if 'copy_one' in actions:
                del actions['copy_one']
        return actions

    # 不同的用户显示不同的内容
    def change_view(self, request, object_id, form_url='', extra_context=None):
        if request.user.is_superuser:
            self.fieldsets = [
                ('基础信息',{'fields': ['title','authors','master']}),
                ('出版信息',{'fields': ['publisher', 'publication_date']}),
            ]
        else:
            self.fieldsets = [
                ('基础信息', {'fields': ['title', 'authors']}),
                ('出版信息', {'fields': ['publisher', 'publication_date']}),
            ]
        return super(BookAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

    # 保存时自动
    def save_model(self, request, obj, form, change):
        if not obj.master:
            obj.master = request.user
        super(BookAdmin, self).save_model(request, obj, form, change)

    readonly_fields = ['master',]

    # 重新定义此函数，限制普通用户所能修改的字段
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            self.readonly_fields = []
        return self.readonly_fields

    # 通过当前登录的用户过滤显示的数据
    def get_queryset(self, request):
        qs = super(BookAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(master=User.objects.get(username=request.user))

    # ManyToManyField 字段的展示
    def get_authors(self):
        return ", ".join([x.__str__() for x in self.authors.all()])

    get_authors.short_description = '作者'

    # 颜色显示
    def get_title(self):
        from django.utils.html import format_html
        if self.title=='自由':
            return format_html(
                '<span style="color: red;">{}</span>',
                '无效')
        else:
            return format_html(
                '<span style="color: green;">{}</span>',
                '有效')

    get_title.short_description = '状态'

    list_display = ('id','title' ,get_authors, 'publisher', 'publication_date', get_title, 'last_update_time')
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'title')
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 5
    # 筛选器
    list_filter = ('publication_date', 'authors', 'publisher')
    # 搜索字段
    search_fields = ('title',)
    # 详细时间分层筛选　
    date_hierarchy = 'publication_date'
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-publication_date',)
    # filter_vertical垂直排布 多项项过多时的选择
    filter_horizontal = ('authors',)
    # 单选项过多时的选择
    # raw_id_fields = ('publisher',)

    # 用fields或exclude控制显示或者排除的字段
    # fields = ('title', 'authors', ('publisher', 'publication_date'),'master')
    fieldsets = [
        ('基础信息',{'fields': ['title','authors','master']}),
        ('出版信息',{'fields': ['publisher', 'publication_date']}),
    ]

    # 主从表处理 扩展处理
    inlines = [TagInline]

# Register your models here.
# admin.site.register(Publisher, PublisherAdmin)
# admin.site.register(Author, AuthorAdmin)
# admin.site.register(Book, BookAdmin)
