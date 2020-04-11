from django.contrib import admin

# Register your models here.

from travello.models import Destination, Customer,Orders

admin.site.register(Destination)
admin.site.register(Orders)
admin.site.register(Customer)
