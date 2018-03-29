from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import Http404

from .models import Product


### Featured
class ProductFeaturedListView(ListView):
	#queryset = Product.objects.all()
	template_name = "products/list.html"

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.featured()


class ProductFeaturedDetailView(DetailView):
	#queryset = Product.objects.all() <-- not needed now that we have def get_object
	template_name = "products/featured-detail.html"

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.featured()





### List Views
class ProductListView(ListView):
	#queryset = Product.objects.all()
	template_name = "products/list.html"

	# def get_context_data(self, *args, **kwargs):
	# 	context = super(ProductListView, self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	return context

	#new
	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.all()


def product_list_view(request):
	queryset = Product.objects.all()
	context = {
		'object_list': queryset
	}
	return render(request, "products/list.html", context)




### Detail Views
class ProductDetailSlugView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"

	def get_object(self, *args, **kwargs):
		request = self.request
		#print('request is:', request)
		slug = self.kwargs.get('slug')
		#instance = get_object_or_404(Product, slug=slug, active=True)
		#print('instance is:', instance)
		try:
			instance = Product.objects.get(slug=slug, active=True)
		except Product.DoesNotExist:
			raise Http404("Not found...")
		except Product.MultipleObjectsReturned:
			qs = Product.objects.filter(slug=slug, active=True)
			instance = qs.first()
		except:
			raise http404("uhmmm...")
		return instance


class ProductDetailView(DetailView):
	#queryset = Product.objects.all() <-- not needed now that we have def get_object
	template_name = "products/detail.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		#context['abc'] = 123
		return context

	# new
	def get_object(self, *args, **kwargs):
		request = self.request
		pk = self.kwargs.get('pk')
		instance = Product.objects.get_by_id(pk)
		#print('instance is:', instance)
		if instance is None:
			raise Http404('Product does not exist! 3')
		return instance


def product_detail_view(request, pk=None,  *args, **kwargs):
	print('args:', args)
	print('kwargs:', kwargs)
	#instance = Product.objects.get(pk=pk) #id
	print('pk:', pk)
	#instance = get_object_or_404(Product, pk=pk)
	print('pk after:', pk)

	# try:
	# 	instance = Product.objects.get(id=pk)
	# 	print(instance)
	# except Product.DoesNotExist:
	# 	print('no product here')
	# 	raise Http404('Product does not exist!')
	# except:
	# 	print('huh?')

	instance = Product.objects.get_by_id(pk)
	#print('instance is:', instance)
	if instance is None:
		raise Http404('Product does not exist! 3')

	# commented out
	# qs = Product.objects.filter(id=pk)
	# print(qs)
	# if qs.exists() and qs.count() == 1:
	# 	instance = qs.first()
	# else:
	# 	raise Http404('Product does not exist! 2')

	context = {
		'object': instance
	}
	print(instance)
	return render(request, "products/detail.html", context)