from django.urls import path
from .views import (
    DepartementCreateView,
    DepartementDeleteView,
    DepartementDetailView,
    DepartementListView,
    DepartementUpdateView,


)

app_name = 'departement'
urlpatterns = [
    path('', DepartementListView.as_view(), name='departement-list'),
    path('create/', DepartementCreateView.as_view(), name='departement-create'),
    path('<int:id>/', DepartementDetailView.as_view(), name='departement-detail'),
    path('<int:id>/update/', DepartementUpdateView.as_view(),
         name='departement-update'),
    path('<int:id>/delete/', DepartementDeleteView.as_view(),
         name='departement-delete'),
]
