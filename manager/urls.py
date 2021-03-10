from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('fillupform',views.fillupform, name='fillupform'),

]
