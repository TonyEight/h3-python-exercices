from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Article, Category


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_display_links = ('title',)
    prepopulated_fields = {
        'slug': ('title',)
    }
    summernote_fields = ('content',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
