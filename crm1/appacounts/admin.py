from django.contrib import admin

# Register your models here.
from  .models import custumer
from  .models import product
from  .models import Tag
from  .models import orders

admin.site.register(custumer)
admin.site.register(product)
admin.site.register(Tag)
admin.site.register(orders)