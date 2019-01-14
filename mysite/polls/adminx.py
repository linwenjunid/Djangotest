import xadmin as admin
from xadmin import views
from .models import Question, Choice


# Register your models here.
# class ChoiceInline(admin.StackedInline):
class ChoiceInline:
    model = Choice
    extra = 1


class QuestionAdmin:
    search_fields = ['question_text']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']


class BaseSetting:
    enable_themes = True  # 开启主题功能
    use_bootswatch = True


class GlobalSettings:
    """
    后台修改
    """
    site_title = '修改后的名称'
    site_footer = '修改后的底部'
    menu_style = 'accordion'  # 开启分组折叠


admin.site.register(views.CommAdminView, GlobalSettings)
admin.site.register(views.BaseAdminView, BaseSetting)
admin.site.register(Question, QuestionAdmin)
