from django.urls import path
from . import views

app_name = 'content_management'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path(
        'category/<int:pk>/',
        views.CategoryDetailView.as_view(),
        name='category-detail'
    ),
    path(
        'article/<int:pk>/',
        views.ArticleRedirectView.as_view()
    ),
    path(
        'article/<slug:slug>/',
        views.ArticleDetailView.as_view(),
        name='article-detail'
    ),
]
