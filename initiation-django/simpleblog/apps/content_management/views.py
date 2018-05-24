from django.views import generic
from .models import Category, Article
from django.db.models import Count


class HomeView(generic.ListView):
    template_name='content_management/home.html'
    context_object_name='categories'

    def get_queryset(self):
        return Category.objects.annotate(
            article_count=Count('articles')
        ).filter(article_count__gt=0)
