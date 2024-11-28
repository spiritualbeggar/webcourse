from django.contrib import admin
from .models import Campus, Department, RoomType, Room, Equipment, Installation

admin.site.register(Campus)
admin.site.register(Department)
admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(Equipment)
admin.site.register(Installation)
