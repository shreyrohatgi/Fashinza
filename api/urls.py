from django.conf.urls import url
from django.urls import path
from api import views
from .views import *

urlpatterns = [
	path('add/', views.AddProduct.as_view(), name='add-product'),
	path('edit/<int:pk>/', views.EditProduct.as_view(), name='edit-product'),
	path('delete/<int:pk>/', views.DeleteProduct.as_view(), name='delete-product'),
	path('products/', TextSearch.as_view(), name='text-search'),
	path('categories/', SearchCategory.as_view(), name='categoty-search')
]