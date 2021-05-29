from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
  count = models.IntegerField(default=0)
  sold = models.IntegerField(default=0)
  default_price = models.FloatField(default=0.0)
  total_revenue = models.FloatField(default=0.0)
  type = models.CharField(max_length=100)
  admin = models.ForeignKey('userApp.User',
                            related_name='categories',
                            null=True,
                            blank=True,
                            on_delete=models.SET_NULL)
  
  created_at = models.DateTimeField(editable=False)
  updated_at = models.DateTimeField()

  def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Category, self).save(*args, **kwargs)


class Product(models.Model):
  title = models.CharField(max_length=100)
  price = models.FloatField(default=0.0)
  category = models.ForeignKey('Category',
                               related_name='products',
                               on_delete=models.CASCADE)
  # admin = models.ForeignKey('userApp.User',
  #                           related_name='products',
  #                           null=True,
  #                           blank=True,
  #                           on_delete=models.SET_NULL)
  buyer = models.ForeignKey('userApp.User',
                            related_name='bought_products',
                            null=True,
                            blank=True,
                            on_delete=models.SET_NULL)

  purchased_at = models.DateTimeField(null=True)
  created_at = models.DateTimeField(editable=False)
  updated_at = models.DateTimeField()

  def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Product, self).save(*args, **kwargs)

  def to_json(self):
    data = {}
    data['title'] = self.title
    data['price'] = self.price
    data['category'] = self.category.type
    data['buyer'] = self.buyer.username
    data['purchased_at'] = self.purchased_at
    return data


class Settings(models.Model):
  main_system_currency = models.CharField(max_length=3)