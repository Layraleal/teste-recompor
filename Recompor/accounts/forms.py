from django import forms
from django.contrib.auth.models import User  # ou seu model customizado

class CustomPasswordResetForm(forms.Form):
    email = forms.EmailField(label="Seu e-mail", max_length=254)

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("❌ Este e-mail não está cadastrado.")
        return email
