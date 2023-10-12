from django.urls import path 
from .views import getAllArticles, getArticle, createArticle

urlpatterns = [
    path("getarticles/", getAllArticles),
    path("getarticle/<int:id>", getArticle),
    path("createarticle/", createArticle)
]