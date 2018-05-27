from django.db import models
from django.conf import settings


class Category(models.Model):
    label = models.CharField(
        verbose_name='label',
        max_length=255,
        unique=True
    )
    description = models.TextField(
        verbose_name='description'
    )

    def __str__(self):
        return '{label}'.format(label=self.label)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['label',]


class Article(models.Model):
    title = models.CharField(
        verbose_name='title',
        max_length=700
    )
    content = models.TextField(
        verbose_name='content'
    )
    featured_picture = models.ImageField(
        verbose_name='featured picture',
        null=True,
        blank=True,
        upload_to='featured_pictures/%Y/'
    )
    slug = models.SlugField(
        verbose_name='slug',
        max_length=100
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='author',
        on_delete=models.CASCADE,
        related_name='written_articles'
    )
    categories = models.ManyToManyField(
        Category,
        verbose_name='categories',
        related_name='articles'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='created at'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='updated_at'
    )

    def __str__(self):
        return '{title}'.format(title=self.title)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-updated_at', '-created_at',]
