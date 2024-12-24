from django.contrib import admin

from .models import Direction, Car, CheckList

admin.site.register(Direction)
admin.site.register(Car)
admin.site.register(CheckList)
