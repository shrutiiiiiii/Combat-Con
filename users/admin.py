from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *
from .forms import MyUserCreationForm

class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm

admin.site.register(Host)
admin.site.register(Athlete)
admin.site.register(MyUser, MyUserAdmin)
