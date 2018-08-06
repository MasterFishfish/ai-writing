from django.urls import path

from personalpage import views
urlpatterns = [
    path('', views.welcomepage, name="welcome"),
    path('<int:user_id>/', views.personalpage, name='personal_page'),
    path('<int:user_id>/materials', views.personal_materials_recommend, name='materials_recommend'),
]