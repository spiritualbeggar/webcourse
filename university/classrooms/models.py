from django.db import models

class Campus(models.Model):
    name = models.CharField(max_length=255)
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
    number = models.CharField(max_length=50)
    floor = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return f"Аудитория {self.number} на этаже {self.floor}"

class Equipment(models.Model):
    name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    supply_date = models.DateField()
    def __str__(self):
        return self.name

class Installation(models.Model):
    installation_date = models.DateField()
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.equipment.name} в {self.room.number}"
