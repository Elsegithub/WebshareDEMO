from django.contrib import admin
from . import models
# Register your models here.
from .models import test,textvue

admin.site.register(test)
admin.site.register(textvue)