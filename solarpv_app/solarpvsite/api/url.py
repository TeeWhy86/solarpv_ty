from django.urls import path
from . import views
app_name = 'dashboard'
urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/<pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('certificate/', views.CertificateListView.as_view(), name='certificate_list'),
    path('certificate/<pk>/', views.CertificateDetailView.as_view(), name='certificate_detail'),
    path('service/', views.ServiceListView.as_view(), name='service_list'),
    path('service/<pk>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('client/', views.ClientListView.as_view(), name='client_list'),
    path('client/<pk>/', views.ClientDetailView.as_view(), name='client_detail'),
]
