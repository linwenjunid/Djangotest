from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Publisher(models.Model):
    name = models.CharField('名称',max_length=30)
    address = models.CharField('地址',max_length=50)
    city = models.CharField('市',max_length=60)
    state_province = models.CharField('省',max_length=30)
    country = models.CharField('国家',max_length=50)
    website = models.URLField('网址')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']#默认排序字段
        verbose_name = '出版商'
        verbose_name_plural = '出版商'


class Author(models.Model):
    first_name = models.CharField('名', max_length=30)
    last_name = models.CharField('姓', max_length=40)
    email = models.EmailField('邮箱', blank=True)
    nation = models.CharField('国籍', max_length=20, default='中国')

    def __str__(self):
        if self.nation == '中国':
            str = u'%s %s' % (self.last_name, self.first_name)
        else:
            str = u'%s %s' % (self.first_name, self.last_name)
        return str

    class Meta:
        ordering = ['first_name']#默认排序字段
        verbose_name = '作者'
        verbose_name_plural = '作者'


class Book(models.Model):
    title = models.CharField('书名', max_length=100)
    authors = models.ManyToManyField(Author, verbose_name = '作者')
    publisher = models.ForeignKey(Publisher, verbose_name = '出版商', on_delete = models.PROTECT)
    # 设置时间字段为空必须同时指定 blank=True, null=True
    publication_date = models.DateField('出版日期', blank=True, null=True)
    num_pages = models.IntegerField(blank=True, null=True)
    master = models.ForeignKey(User, verbose_name = '责任人', on_delete = models.PROTECT, null = True)
    last_update_time = models.DateTimeField('最后一次更新日期', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']#默认排序字段
        verbose_name = '书籍'
        verbose_name_plural = '书籍'


class Tag(models.Model):
    tag = models.CharField('关键字', max_length=20)
    book = models.ForeignKey(Book, verbose_name='关键字', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.tag

    class Meta:
        ordering = ['tag']
        verbose_name = '关键字'
        verbose_name_plural = '关键字'