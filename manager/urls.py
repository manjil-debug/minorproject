from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('fillupform', views.fillupform, name='fillupform'),
    path('user_login', views.user_login, name='user_login'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('venues/soltee', views.soltee, name='soltee'),
    path('venues/sangrila', views.sangrila, name='sangrila'),
    path('venues/annapurna', views.annapurna, name='annapura'),
    path('venues/himalayan', views.himalayan, name='himalayan'),
    path('venues/dhulikhel', views.dhulikhel, name='dhulikhel')
]
