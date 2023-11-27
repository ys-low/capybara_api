from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api import models

# Register your models here
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Capybara)
admin.site.register(models.Location)