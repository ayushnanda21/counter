from django.contrib import admin

# Register your models here.

from .models import CounterModel

admin.site.register(CounterModel)