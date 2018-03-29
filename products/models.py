from django.db import models
import random
import os

from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator



def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	print('')
	print("base_name:", base_name)
	name, ext = os.path.splitext(base_name)
	print(name, ext)
	print('')
	return name, ext


def upload_image_path(instance, filename):
	print(instance)
	print(filename)
	new_filename = random.randint(1,5000)
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
	print(final_filename)
	return "products/{new_filename}/'{final_filename}".format(
		new_filename=new_filename, 
		final_filename=final_filename)



class ProductManager(models.Manager):
	def featured(self):
		return self.get_queryset().filter(featured=True)

	def get_by_id(self, id):
		qs = self.get_queryset().filter(id=id) ## Product.object == self.get_queryset() kind of
		if qs.count() == 1:
			print('gs.first() is:', qs.first())
			return qs.first()
		return None


class Product(models.Model):
	title 		= models.CharField(max_length=120)
	slug		= models.SlugField(blank=True, unique=True)
	description = models.TextField()
	price 		= models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
	image		= models.ImageField(upload_to=upload_image_path, null=True, blank=True) # bylo upload_to='products/'
	# this was for FileField
	#image		= models.FileField(upload_to=upload_image_path, null=True, blank=True) # bylo upload_to='products/'
	featured	= models.BooleanField(default=False)
	active		= models.BooleanField(default=True)


	objects = ProductManager()

	def __str__(self):
		return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = 'abc'

pre_save.connect(product_pre_save_receiver, sender=Product)