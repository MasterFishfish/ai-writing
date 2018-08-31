from django.conf.urls import url
from algorithm import views

urlpatterns = [
    url(r'^search/', views.search_keyword, name="search"),
]