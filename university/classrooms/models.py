from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms


class Campus(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='campus_photos/', blank=True, null=True)
    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class RoomType(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Room(models.Model):
    number = models.CharField(max_length=10, verbose_name="Номер аудитории")
    floor = models.IntegerField(verbose_name="Этаж")
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")
    area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Площадь")
    capacity = models.IntegerField(verbose_name="Вместимость")
    campus = models.ForeignKey('Campus', on_delete=models.CASCADE, verbose_name="Корпус")
    room_type = models.ForeignKey('RoomType', on_delete=models.CASCADE, verbose_name="Тип аудитории")
    department = models.ForeignKey('Department', on_delete=models.CASCADE, verbose_name="Факультет")
    photo = models.ImageField(upload_to='rooms/', verbose_name="Фотография", blank=True, null=True)
    name = models.CharField(max_length=100, default="Default Room")
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"№{self.number}, {self.campus}"


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    supply_date = models.DateField()
    photo = models.ImageField(upload_to='equipment_photos/', blank=True, null=True)
    def __str__(self):
        return self.name

class Installation(models.Model):
    installation_date = models.DateField()
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.equipment.name} в {self.room.number}"

class CustomUser(AbstractUser):
    is_guest = models.BooleanField(default=False)

    # Переопределите поля 'groups' и 'user_permissions' с добавлением related_name
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Уникальное имя для связи с группами
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Уникальное имя для связи с разрешениями
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser',
    )

class RegistrationForm(forms.ModelForm):
    is_guest = forms.BooleanField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['is_guest']:
            user.is_guest = True
        if commit:
            user.save()
        return user