from django.contrib import admin

# Register your models here.

from .models import Ping

admin.site.register(Ping)