from django.contrib import admin
from accounts.models import Customer, Vendor

admin.site.register(Vendor)
admin.site.register(Customer)
