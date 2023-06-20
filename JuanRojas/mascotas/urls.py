from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('create/', views.create, name='create'),
    path('modify/<int:id>', views.modify, name='modify'),
    path('list/', views.list, name='list'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('registrar/', views.registrar, name='registrar'),
    path('products/', views.products, name='products'),
]