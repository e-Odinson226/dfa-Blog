from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CostumUser
from .forms import CostumUserChangeForm, CostumUserCreationForm


class CostumUserAdmin(UserAdmin):
    add_form = CostumUserCreationForm
    form = CostumUserCreationForm
    model = CostumUser
    list_display = [
        "name",
        "email",
        "username",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),)


admin.site.register(CostumUser, CostumUserAdmin)
