from django.db import models


class Article(models.Model):
    """
    文章模型
    """
    title = models.CharField(verbose_name='文章', max_length=200, null=False, blank=False)
    date = models.DateTimeField(auto_created=True)
