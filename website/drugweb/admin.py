from django.contrib import admin

# Register your models here.
from .models import Cure, Drugdetails

admin.site.register(Cure)
admin.site.register(Drugdetails)
