from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name="article_list"),
    path('<slug>', views.article_detail, name="detail")
]