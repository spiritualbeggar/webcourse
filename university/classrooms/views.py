from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Campus, Department, RoomType, Room, Equipment, Installation

# Список корпусов
class CampusListView(ListView):
    model = Campus
    template_name = 'classrooms/campus_list.html'
    context_object_name = 'campuses'

# Детали корпуса
class CampusDetailView(DetailView):
    model = Campus
    template_name = 'classrooms/campus_detail.html'
    context_object_name = 'campus'
    
# Список аудиторий
class RoomListView(ListView):
    model = Room
    template_name = 'classrooms/room_list.html'
    context_object_name = 'rooms'

# Детали аудитории
class RoomDetailView(DetailView):
    model = Room
    template_name = 'classrooms/room_detail.html'
    context_object_name = 'room'

# Список оборудования
class EquipmentListView(ListView):
    model = Equipment
    template_name = 'classrooms/equipment_list.html'
    context_object_name = 'equipments'

# Детали оборудования
class EquipmentDetailView(DetailView):
    model = Equipment
    template_name = 'classrooms/equipment_detail.html'
    context_object_name = 'equipment'

# Список установок
class InstallationListView(ListView):
    model = Installation
    template_name = 'classrooms/installation_list.html'
    context_object_name = 'installations'

# Детали установки
class InstallationDetailView(DetailView):
    model = Installation
    template_name = 'classrooms/installation_detail.html'
    context_object_name = 'installation'
