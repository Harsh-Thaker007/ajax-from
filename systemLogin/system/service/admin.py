from django.contrib import admin
from .models import Profile
# Register your models here.
class Profile_Admin(admin.ModelAdmin):
    list_display = ['username', 'password']


admin.site.register(Profile, Profile_Admin)
