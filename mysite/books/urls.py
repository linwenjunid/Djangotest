from django.urls import path, include
from . import views

app_name = 'books'

"""
rest_framework模块
"""
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
router = DefaultRouter()  # 可以处理视图的路由器
router.register('books', views.BooksViewSet)  # 向路由器中注册视图集


urlpatterns = (
    path('search/', views.search, name='search'),
    path('downbooks/', views.books_list_plaintext, name='downbooks'),
    path('list/', views.books_list, name='booklist'),
    path('api/',include(router.urls), name = 'api'),
    path('api-token-auth/', obtain_jwt_token)
    )




#urlpatterns += tuple(router.urls)  # 将路由器中的所有路由信
