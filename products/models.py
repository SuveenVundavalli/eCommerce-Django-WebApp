from django.db import models
import os
import random


def get_filename_ext(filepath):
    basename = os.path.basename(filepath)
    name, ext = os.path.splitext(basename)
    return name, ext


def upload_image_path(instance, filename):
    print('instance', instance)
    print('file', filename)
    new_filename = random.randint(1, 82348238293)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return 'products/{new_filename}/{final_filename}'.format(new_filename=new_filename, final_filename=final_filename)


# Model manager ref: S03L28
class ProductManager(models.Manager):
    def featured(self):
        return self.get_queryset().filter(featured=True)
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=100)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured = models.BooleanField(default=False)

    objects = ProductManager() # It is extending objects which is an inbuilt model manager

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
