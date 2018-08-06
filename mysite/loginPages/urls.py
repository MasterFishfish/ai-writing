from django.urls import path

from loginPages import views

urlpatterns = [
    path('', views.login, name="login"),
    path('loginresult/', views.login_results, name="login_result"),
    path('do_login/', views.do_login, name="do_login"),
    path('regist/', views.regist, name="regist"),
    path('do_regist/', views.do_regist, name="do_regist"),
    #path('<int:choice_id>/', views.detail, name='detail'),
]