from django.contrib import admin

# Register your models here.

from .models import Produkt, Koszyk
admin.site.register(Produkt)
admin.site.register(Koszyk)

