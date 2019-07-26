from django.urls import path
from . import views 

urlpatterns = [
    path('analytics/', views.data_analytics, name='data_analytics')
]