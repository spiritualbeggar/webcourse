from django import forms
from .models import Room
from .models import Equipment
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class AddRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['number', 'floor', 'cost', 'area', 'capacity', 'campus', 'room_type', 'department', 'photo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['campus'].empty_label = 'Выберите корпус'
        self.fields['room_type'].empty_label = 'Выберите тип аудитории'
        self.fields['department'].empty_label = 'Выберите подразделение'
        
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Логин', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Введите логин'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))

class AddEquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'cost', 'supply_date', 'photo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        
        if password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают")
        return cleaned_data