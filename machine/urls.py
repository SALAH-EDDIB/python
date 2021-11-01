from django.urls import path
from .views import (
    MachineCreateView,
    MachineDeleteView,
    MachineDetailView,
    MachineListView,
    MachineUpdateView,
    machineBydepartement_list,

    machineCheckView


)

app_name = 'machine'
urlpatterns = [
    path('', MachineListView.as_view(), name='machine-list'),
    path('create/', MachineCreateView.as_view(), name='machine-create'),
    path('<int:id>/', machineBydepartement_list, name='machine-detail'),
    path('<int:id>/update/', MachineUpdateView.as_view(),
         name='machine-update'),
    path('<int:id>/check/', machineCheckView,
         name='machine-check'),

    path('<int:id>/delete/', MachineDeleteView.as_view(),
         name='machine-delete'),
]
