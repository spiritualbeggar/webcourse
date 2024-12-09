from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Campus, Department, RoomType, Room, Equipment, Installation
from django.shortcuts import render, redirect
from .forms import AddRoomForm
from .forms import AddEquipmentForm
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .forms import CustomAuthenticationForm
from .utils import DataMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.shortcuts import redirect




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
    
class AddRoom(CreateView):
    form_class = AddRoomForm
    template_name = 'rooms/add_room.html'
    login_url = '/login/'  # Перенаправление на страницу входа для неавторизованных пользователей
    success_url = reverse_lazy('room_list')  # Перенаправление после успешного добавления комнаты
    def form_valid(self, form):
        # Сохраняем объект и перенаправляем на страницу списка комнат
        form.save()
        return redirect('room_list')  # или другой маршрут, если требуется
    
class RoomHome(DataMixin, ListView):
    model = Room
    template_name = 'rooms/room_list.html'
    context_object_name = 'rooms'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        auth = self.request.user.is_authenticated  # Проверка авторизации
        c_def = self.get_user_context(title='Список аудиторий', auth=auth)
        return {**context, **c_def}

# views.py
from django.shortcuts import render
from .models import Room

def room_list(request):
    # Получаем все аудитории
    rooms = Room.objects.all()

    # Пример меню
    menu = [
        {'url_name': 'about', 'title': 'О нас'},
        {'url_name': 'contact', 'title': 'Контакты'},
    ]

    # Формируем контекст для передачи в шаблон
    context = {
        'rooms': rooms,
        'title': 'Список аудиторий',
        'auth': request.user.is_authenticated,  # Проверка, аутентифицирован ли пользователь
        'menu': menu,
    }

    # Отправляем данные в шаблон
    return render(request, 'classrooms/room_list.html', context)


    
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomAuthenticationForm
    

class AddEquipment(CreateView):
    form_class = AddEquipmentForm
    template_name = 'rooms/add_equipment.html'
    success_url = reverse_lazy('equipment_list')  # Перенаправление после успешного добавления

    def form_valid(self, form):
        equipment = form.save()
        room_id = self.request.POST.get('room_id')  # Получаем id аудитории, если оно передано
        if room_id:
            room = Room.objects.get(id=room_id)
            room.cost += equipment.cost  # Добавляем стоимость оборудования к аудитории
            room.save()
        return super().form_valid(form)
    
def is_admin(user):
    return user.is_superuser


@login_required
def add_room(request):
    # Проверка, является ли пользователь администратором
    if request.user.is_superuser:
        if request.method == 'POST':
            form = AddRoomForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('room_list')  # Перенаправление на страницу со списком аудиторий
        else:
            form = AddRoomForm()
        return render(request, 'add_room.html', {'form': form})
    else:
        return redirect('room_list')  # Перенаправление на страницу с аудиториями для неадминистраторов

@login_required
def add_equipment(request):
    # Проверка, является ли пользователь администратором
    if request.user.is_superuser:
        if request.method == 'POST':
            form = AddEquipmentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('equipment_list')  # Перенаправление на страницу со списком оборудования
        else:
            form = AddEquipmentForm()
        return render(request, 'classrooms/add_equipment.html', {'form': form})
    else:
        return redirect('equipment_list')  # Перенаправление на страницу с оборудованием для неадминистраторов
    
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def equipment_list(request):
    if request.user.is_superuser:
        # Передаем контекст с возможностью добавлять оборудование
        return render(request, 'equipment/equipment_list.html', {'is_superuser': True})
    else:
        # Только просмотр для обычных пользователей
        return render(request, 'equipment/equipment_list.html', {'is_superuser': False})
    
def custom_logout(request):
    logout(request)
    return redirect('/')