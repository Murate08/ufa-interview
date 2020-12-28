from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




#create user
class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'input'}))

    class Meta:
        model = User
        fields = [
            'username' ,
            'email',
            
            
        ]
        widgets={
            'username' : forms.TextInput(attrs={'class': 'input'}),
        }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False) 
        user.email =  self.cleaned_data['email']

        if commit:
            user.save()

        return User    




