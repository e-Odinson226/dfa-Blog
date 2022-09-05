from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CostumUser


class CostumUserChangeForm(UserChangeForm):
    class Meta:
        model = CostumUser
        fields = UserChangeForm.Meta.fields + ("name",)


class CostumUserCreationForm(UserCreationForm):
    class Meta:
        model = CostumUser
        fields = UserChangeForm.Meta.fields + ("name",)
