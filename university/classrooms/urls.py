from django.urls import path
from . import views

urlpatterns = [
    path('campuses/', views.CampusListView.as_view(), name='campus_list'),
    path('campuses/<int:pk>/', views.CampusDetailView.as_view(), name='campus_detail'),
    path('rooms/', views.RoomListView.as_view(), name='room_list'),
    path('rooms/<int:pk>/', views.RoomDetailView.as_view(), name='room_detail'),
    path('equipments/', views.EquipmentListView.as_view(), name='equipment_list'),
    path('equipments/<int:pk>/', views.EquipmentDetailView.as_view(), name='equipment_detail'),
    path('installations/', views.InstallationListView.as_view(), name='installation_list'),
    path('installations/<int:pk>/', views.InstallationDetailView.as_view(), name='installation_detail'),
]
