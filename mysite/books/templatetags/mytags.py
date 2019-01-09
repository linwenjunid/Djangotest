from django import template
from ..models import Book
import datetime

register = template.Library()


@register.filter(name='rep')
def rep(value, arg):
    return value.replace(arg, '')


@register.simple_tag
def cut4(format_string):
    try:
        return format_string[0:3]
    except UnicodeEncodeError:
        return ''


@register.inclusion_tag('books.html',takes_context=True)
def books(context):
    books = Book.objects.all()
    return {'books': books,
            'str':context['mystring']}


@register.tag(name="current_time")
def do_current_time(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, format_string = token.split_contents()
    except ValueError:
        msg = '%r tag requires a single argument' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
    return CurrentTimeNode(format_string[1:-1])


class CurrentTimeNode(template.Node):
    def __init__(self, format_string):
        self.format_string = str(format_string)

    def render(self, context):
        now = datetime.datetime.now()
        return now.strftime(self.format_string)