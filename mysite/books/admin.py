from django.contrib import admin
from .models import Publisher, Author, Book
from django.contrib.auth.models import User


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','address','city','state_province','country','website')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
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

    get_title.short_description = '书名'

    list_display = ('id','title' ,get_authors, 'publisher', 'publication_date', get_title)
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'title')
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50
    # 筛选器
    list_filter = ('publication_date', 'authors', 'publisher')
    # 搜索字段
    search_fields = ('title',)
    # 详细时间分层筛选　
    date_hierarchy = 'publication_date'
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-publication_date',)
    fields = ('title', 'authors', 'publisher', 'publication_date','master')
    filter_horizontal = ('authors',)#filter_vertical垂直排布 多项项过多时的选择
    #raw_id_fields = ('publisher',) #单选项过多时的选择
# Register your models here.


# admin.site.register(Publisher, PublisherAdmin)
# admin.site.register(Author, AuthorAdmin)
# admin.site.register(Book, BookAdmin)
