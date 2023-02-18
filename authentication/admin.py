from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
     list_display = ("email", "is_active", "is_student", "is_teacher", "is_verified", "password")

admin.site.register(User, UserAdmin)
