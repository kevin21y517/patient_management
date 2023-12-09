from django import forms
from .models import HStaff
from django.contrib.auth import authenticate

class CustomAuthenticationForm(forms.ModelForm):
    class Meta:
        model = HStaff
        fields = ['username', 'password']

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        self.user = authenticate(username=username, password=password)  # 認證使用者
        if not self.user:
            raise forms.ValidationError("Invalid username or password.")  # 驗證失敗，拋出錯誤
        return self.cleaned_data

    def get_user(self):
        return self.user

class LoginForm(forms.Form):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )