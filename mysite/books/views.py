from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse,HttpResponseRedirect
from .models import Book


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('请输入关键字.')
        elif len(q) > 20:
            errors.append('关键字超过20个字符')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                                      {'books': books, 'query': q})
    return render_to_response('search_form.html',
                              {'errors': errors,
                               'myString': '过滤器函数应该总有返回值。'})


def books_list_plaintext(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=books.txt'
    books = Book.objects.all()
    for book in books:
        response.writelines(book.title + '\r\n')
    return response


def books_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 3)

    page = request.GET.get('page', 1)
    book_page = paginator.get_page(page)
    return render(request, 'list.html', {'contacts': book_page})


"""
rest_framework模块
"""
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .filter import UserFilter


class UsersPagination(PageNumberPagination):
    # 指定每一页的个数
    page_size = 2
    # 可以让前端来设置page_szie参数来指定每页个数
    page_size_query_param = 'page_size'
    # 设置页码的参数
    page_query_param = 'page'


class BooksViewSet(ModelViewSet):
    queryset = Book.objects.all()
    # 设置序列化的class
    serializer_class = BookSerializer
    # 设置分页的class
    pagination_class = UsersPagination
    # 设置认证的class
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    # 设置过滤器
    filter_backends = (DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter)
    # 设置过滤字段
    # filter_fields = ('title', 'publication_date')
    # 设置自定义过滤器
    filter_class = UserFilter
    # 设置搜索条件
    search_fields = ('title',)
    # 设置排序字段
    ordering_fields = ('title',)
