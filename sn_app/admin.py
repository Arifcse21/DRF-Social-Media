from django.contrib import admin
from sn_app.models import User, Profile
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "username",
        "uuid",
        "is_active",
        "is_staff",
        "is_superuser"
    ]

    list_display_links = ["username",]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "created_at",
        "modified_at"
    ]

    list_display_links = ["user",]