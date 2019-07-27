from django.urls import path
from . import views 

urlpatterns = [
    path('v1/analytics/', views.data_analytics, name='data_analytics')
]