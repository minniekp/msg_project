# catalogs/urls.py 
from django.urls import path
from . import views

urlpatterns = [
 	path('', views.CatalogListView.as_view(), name='catalog_list'), 
 	path('<int:pk>/edit/', views.CatalogUpdateView.as_view(), name='catalog_edit'), # new 
 	path('<int:pk>/', views.CatalogDetailView.as_view(), name='catalog_detail'), # new 
 	path('new/', views.CatalogCreateView.as_view(), name='catalog_new'), 
    path('<int:pk>/delete/', views.CatalogDeleteView.as_view(), name='catalog_delete'), # new
]
