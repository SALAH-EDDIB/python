"""cfehome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import home_page
from pages.views import About_page
from pages.views import loginPage
from pages.views import logoutUser
from pages.views import UserListView
from pages.views import UserCreate
from pages.views import userUpadte
from pages.views import UserDelete

from django.urls import include, path

urlpatterns = [

    path('departement/', include('departement.urls')),
    path('machine/', include('machine.urls')),
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('about/', About_page),

    path('login/', loginPage, name='login'),
    path('user/', UserListView.as_view(), name='users'),
    path('logout/', logoutUser, name='logout'),
    path('user/create/', UserCreate, name='user_crete'),

    path('user/<int:id>/update/', userUpadte, name='user_update'),
    path('user/<int:id>/delete/', UserDelete, name='user_delete'),

]
