from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('careers', views.careers, name='careers'),
    path('contact', views.contact, name='contact'),
    path('team', views.team, name='team'),
    path('clients', views.clients, name='clients'),
    path('services/<int:pk>', views.servicesdetail, name='servicesdetail'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/<int:blog_id>/', views.blog_detail, name='blog_detail'),  # Add this line for blog_detail
    path('subscribe/', views.subscribe, name='subscribe'),
    path('error/', views.page_not_found, name='error'),





]