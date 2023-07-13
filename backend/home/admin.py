from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(Photo)
admin.site.register(Services)
admin.site.register(team)
admin.site.register(Services_heading)