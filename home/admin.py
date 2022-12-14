from django.contrib import admin
from .models import Offers 
# Register your models here.


@admin.register(Offers)
class OffersAdmin(admin.ModelAdmin):
  pass 