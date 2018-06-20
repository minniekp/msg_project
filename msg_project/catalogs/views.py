# catalogs/views.py 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy


from . import models

class CatalogCreateView(CreateView): 
	model = models.Catalog 
	template_name = 'catalog_new.html' 
	fields = ['DatasetName', 'Type', 'Classification', 'OriginalSource', 'OriginalOwner'] 

class CatalogListView(ListView): 
	model = models.Catalog 
	template_name = 'catalog_list.html'
	

class CatalogDetailView(DetailView): 
	model = models.Catalog
	template_name = 'catalog_detail.html'

class CatalogUpdateView(UpdateView): 
	model = models.Catalog 
	fields = ['DatasetName'] 
	template_name = 'catalog_edit.html'

class CatalogDeleteView(DeleteView): 
	model = models.Catalog
	template_name = 'catalog_delete.html' 
	success_url = reverse_lazy('catalog_list')