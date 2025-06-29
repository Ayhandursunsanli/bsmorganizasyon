from django.urls import path
from . import views

app_name = 'bsmapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:pk>/', views.blog_single, name='blog_single'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('services/<int:pk>/', views.service_detail, name='service_detail'),
] 