from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import home
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register-client/', views.register_client, name='register_client'),
    path('add-program/', views.add_program, name='add_program'),
    path('enroll-client/', views.enroll_client, name='enroll_client'),
    path('client/<int:pk>/', views.client_profile, name='client_profile'),
    path('enrolled_clients/', views.enrolled_clients, name='enrolled_clients'),
    path('clients/', views.all_clients, name='all_clients'),
    path('api/client/<int:client_id>/', views.client_profile_api, name='client_profile_api'),
]
