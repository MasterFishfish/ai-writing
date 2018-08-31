from django.conf.urls import url
from .views import UserShow, ChangePassword
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^$', UserShow.as_view()),
    url(r'^password/', ChangePassword.as_view()),
]