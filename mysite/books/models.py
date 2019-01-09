from django.db import models


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

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ['first_name']#默认排序字段
        verbose_name = '作者'
        verbose_name_plural = '作者'


class Book(models.Model):
    title = models.CharField('书名', max_length=100)
    authors = models.ManyToManyField(Author, verbose_name = '作者')
    publisher = models.ForeignKey(Publisher, verbose_name = '出版商', on_delete=models.PROTECT)
    # 设置时间字段为空必须同时指定 blank=True, null=True
    publication_date = models.DateField('出版日期', blank=True, null=True)
    num_pages = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']#默认排序字段
        verbose_name = '书籍'
        verbose_name_plural = '书籍'