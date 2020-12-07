from django.db import models
from django.core.exceptions import ValidationError


class Article(models.Model):
    """
    文章模型
    """
    title = models.CharField(verbose_name='文章', max_length=200, null=False, blank=False)
    like = models.IntegerField(verbose_name='点赞')
    date = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.title == 'liuxin':
            raise ValidationError('Title can not be named liuxin!')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.full_clean()
        return super(Article, self).save(force_insert=False, force_update=False, using=None, update_fields=None)


class Hobby(models.Model):
    """
    爱好模型
    """
    name = models.CharField(verbose_name='爱好', max_length=80, blank=False, null=False)

    class Meta:
        db_table = 'hobby'

    def __str__(self):
        return f'id: {self.pk}, name: {self.name}'


class Student(models.Model):
    """
    学生模型
    """
    name = models.CharField(verbose_name='姓名', max_length=80, blank=False, null=False)
    age = models.IntegerField(verbose_name='年龄')
    hobbies = models.ManyToManyField(Hobby)

    def __str__(self):
        return f'id: {self.pk}, name: {self.name}'

    class Meta:
        db_table = 'student'


class Company(models.Model):
    """
    公司模型
    """
    employees = models.IntegerField()
    chairs = models.IntegerField()


class Author(models.Model):
    """
    作者模型
    """
    name = models.CharField(verbose_name='作者', max_length=80)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'author'
        ordering = ('name',)


class Publisher(models.Model):
    """
    出版商模型
    """
    name = models.CharField(verbose_name='发布者', max_length=80)

    class Meta:
        db_table = 'publisher'
        ordering = ('name',)


class Book(models.Model):
    """
    书籍模型
    """
    name = models.CharField(verbose_name='书籍名称', max_length=300)
    pages = models.IntegerField(verbose_name='书籍页数')
    price = models.DecimalField(verbose_name='书籍价格', max_digits=10, decimal_places=2)
    rating = models.FloatField(verbose_name='书籍评分')
    authors = models.ManyToManyField(Author)
    publishers = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField(verbose_name='发布日期')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'book'
        ordering = ('name',)


class Store(models.Model):
    """
    书店模型
    """
    name = models.CharField(verbose_name='书店名', max_length=100)
    books = models.ManyToManyField(Book)

    class Meta:
        db_table = 'store'
        ordering = ('name',)

