from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('fillupform',views.fillupform, name='fillupform'),
    path('user_login',views.user_login, name='user_login'),
    path('sign_up',views.sign_up, name='sign_up'),
]
