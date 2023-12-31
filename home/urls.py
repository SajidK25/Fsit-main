from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('blogs', views.blogs, name='blogs'),
    path('careers', views.careers, name='careers'),
    path('contact', views.contact, name='contact'),
    path('team', views.team, name='team'),
    path('services/<int:pk>', views.servicesdetail, name='servicesdetail'),
    path('blogs/<int:blog_id>/', views.blogsdetail, name='blogsdetail'),
]