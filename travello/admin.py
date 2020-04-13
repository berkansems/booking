from django.contrib import admin

# Register your models here.

from travello.models import Destination, Customer,Order

admin.site.register(Destination)
admin.site.register(Order)
admin.site.register(Customer)
