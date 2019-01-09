from .models import Book
from rest_framework import serializers
"""
rest_framework模块
"""


class BookSerializer(serializers.ModelSerializer):
    """图书数据序列化器"""
    class Meta:
        model = Book
        fields = '__all__'