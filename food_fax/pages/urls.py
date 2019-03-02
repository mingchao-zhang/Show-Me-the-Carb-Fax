from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('demo', views.demo, name='demo'),
    path('about', views.about, name='about'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('contact', views.contact, name='contact'),
]