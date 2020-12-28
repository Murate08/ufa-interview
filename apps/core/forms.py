from django import forms
from django.core.exceptions import ValidationError








class RegisterForms(forms.ModelForm):    
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        field  = ['username', 'email']



    def clean_password(self):
        cd = self.clean_data
        if cd['password2'] != cd['password']:
            raise ValidationError("Password dont match")


        return cd['password']








