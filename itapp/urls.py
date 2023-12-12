from django.urls import path
from .views import post,about,blog,contact,error,project,service,team,testimonial,home
urlpatterns = [
    path('',post,),
    path('home/<int:pk>/', home, name='home'),
    path('about/<int:pk>/', about, name='about'),
    path('blog/<int:pk>/', blog, name='blog'),
    path('contact/<int:pk>/', contact, name='contact'),
    path('error/<int:pk>/', error, name='error'),
    path('project/<int:pk>/', project, name='project'),
    path('service/<int:pk>/',service, name='service'),
    path('team/<int:pk>/', team, name='team'),
    path('testimonial/<int:pk>/', testimonial, name='testimonial'),
    ]