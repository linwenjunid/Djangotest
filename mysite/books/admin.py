from django.contrib import admin
from .models import Publisher, Author, Book


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','address','city','state_province','country','website')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date', 'publisher')
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    fields = ('title', 'authors', 'publisher', 'publication_date')
    filter_horizontal = ('authors',)#filter_vertical垂直排布 多项项过多时的选择
    #raw_id_fields = ('publisher',) #单选项过多时的选择
# Register your models here.


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
