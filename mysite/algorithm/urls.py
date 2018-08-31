from django.conf.urls import url
from algorithm.views import Search_keyword

urlpatterns = [
    url(r'^search/', Search_keyword.as_view()),
]