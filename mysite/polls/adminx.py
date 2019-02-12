import xadmin
from xadmin import views
from .models import Question, Choice
from django.http import HttpResponseRedirect


# Register your models here.
# class ChoiceInline(admin.StackedInline):
class ChoiceInline:
    model = Choice
    extra = 1


# @xadmin.sites.register(Question)
class QuestionAdmin:
    search_fields = ['question_text']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']

    def copy_one(self, request, queryset):
        if queryset.count() == 1:
            old_data = queryset.values()[0]
            old_data.pop('id')
            new_data = Question.objects.create(**old_data)
            return HttpResponseRedirect(
                '{}{}/update'.format(request.path, new_data.id))
        else:
            self.message_user(request, "只能选取一条数据！")
    copy_one.short_description = '复制所选数据'
    actions = [copy_one]


# @xadmin.sites.register(views.BaseAdminView)
class BaseSetting:
    enable_themes = True  # 开启主题功能
    use_bootswatch = True


# @xadmin.site.register(views.CommAdminView)
class GlobalSettings:
    """
    后台修改
    """
    site_title = '修改后的名称'
    site_footer = '修改后的底部'
    menu_style = 'accordion'  # 开启分组折叠


xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(Question, QuestionAdmin)
