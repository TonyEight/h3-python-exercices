from django.shortcuts import get_object_or_404
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


class CategoryDetailView(generic.DetailView):
    template_name='content_management/category_detail.html'
    context_object_name='category'
    model = Category

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'categories': Category.objects.annotate(
                article_count=Count('articles')
            ).filter(article_count__gt=0)
        })
        return context


class ArticleRedirectView(generic.base.RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'content_management:article-detail'

    def get_redirect_url(self, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs['pk'])
        return super().get_redirect_url(article.slug)

class ArticleDetailView(generic.DetailView):
    template_name='content_management/article_detail.html'
    context_object_name='article'
    model = Article

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        current_category_pk = self.request.GET.get('category', None)
        current_category = None
        related_articles = None
        if current_category_pk is not None:
            current_category = Category.objects.get(pk=int(current_category_pk))
            related_articles = current_category.articles.exclude(pk=self.get_object().pk)
        context.update({
            'categories': Category.objects.annotate(
                article_count=Count('articles')
            ).filter(article_count__gt=0),
            'current_category': current_category,
            'related_articles': related_articles
        })
        return context
