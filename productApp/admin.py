from django.contrib import admin
from productApp.models import (
  Category,
  Product,
  Settings
)

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Settings)
