from django.urls import path

from personalpage import views
urlpatterns = [
    path('', views.personalpage, name='personal_page'),
    path('search/', views.personal_materials_recommend, name='materials_recommend'),
]