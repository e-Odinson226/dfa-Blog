from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CostumUser


class CostumUserChangeForm(UserChangeForm):
    class Meta:
        model = CostumUser
        fields = UserChangeForm.Meta.fields


class CostumUserCreationForm(UserCreationForm):
    class Meta:
        model = CostumUser
        fields = UserCreationForm.Meta.fields + ("name",)
