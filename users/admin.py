from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    model = CustomUser

    list_display = (
        "id",
        "email",
        "phone_number",
        "is_staff"
    )

    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),

        ("Personal info", {
            "fields": ("phone_number",)
        }),

        ("Permissions", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            ),
        }),

        ("Important dates", {
            "fields": ("last_login",)
        }),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),

                "fields": (
                    "email",
                    "phone_number",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )

    search_fields = ("email",)