from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Default homepage
    path('about/', views.about, name='about'),  # Custom about page
    path('contact/', views.contact, name='contact'),  # Custom contact page
    path('api/data/', views.api_data, name='api_data'),  # Custom API endpoint for data retrieval
    path('api/data/<int:data_id>/', views.api_data_detail, name='api_data_detail'),  # Custom API endpoint for data detail
]