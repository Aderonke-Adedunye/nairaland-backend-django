from django.urls import path 
from .views import getAllArticles, getArticle

urlpatterns = [
    path("getarticles/", getAllArticles),
    path("getarticle/<int:id>", getArticle)
]