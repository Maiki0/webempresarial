from django.urls import path
from . import views

urlpatterns = [
    path('history/', views.history, name='history'),
    path('', views.home, name='home'),
    path('visit/', views.visit, name='visit'),
]