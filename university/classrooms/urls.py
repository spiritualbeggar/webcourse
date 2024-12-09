from django.urls import path
from . import views
from .views import AddRoom, RoomHome, add_room
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import AddEquipment
from .views import custom_logout




urlpatterns = [
    path('', RoomHome.as_view(), name='home'),
    path('campuses/', views.CampusListView.as_view(), name='campus_list'),
    path('campuses/<int:pk>/', views.CampusDetailView.as_view(), name='campus_detail'),
    path('rooms/', views.RoomListView.as_view(), name='room_list'),
    path('rooms/<int:pk>/', views.RoomDetailView.as_view(), name='room_detail'),
    path('equipments/', views.EquipmentListView.as_view(), name='equipment_list'),
    path('equipments/<int:pk>/', views.EquipmentDetailView.as_view(), name='equipment_detail'),
    path('installations/', views.InstallationListView.as_view(), name='installation_list'),
    path('installations/<int:pk>/', views.InstallationDetailView.as_view(), name='installation_detail'),
    path('add_room/', AddRoom.as_view(), name='add_room'),
    path('add_quipment/', AddEquipment.as_view(), name='add_equipment'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', custom_logout, name='logout'),
    path('register/', views.register, name='register'),
]
