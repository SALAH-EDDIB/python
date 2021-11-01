
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator

from django.views.generic import (

    ListView,

)
from .forms import CreateUserForm
# Create your views here.
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only


@login_required(login_url='login')
@admin_only
def home_page(request, *args, **kwargs):
    return redirect('users')


@method_decorator(admin_only, name='dispatch')
class UserListView(ListView):
    template_name = 'user_list.html'
    queryset = User.objects.all()


@unauthenticated_user
def loginPage(request, *args, **kwargs):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'Username OR password is incorrect')

    return render(request, "login.html", {})


@admin_only
def UserCreate(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('users')

    context = {'form': form}
    return render(request, 'user_create.html', context)


@admin_only
def userUpadte(request, id=id):

    obj = get_object_or_404(User, id=id)
    form = CreateUserForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('users')

    context = {'form': form}
    return render(request, 'user_create.html', context)


@admin_only
def UserDelete(request, id):
    obj = get_object_or_404(User, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "user_delete.html", context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def About_page(request, *args, **kwargs):
    context = {
        "title": "this is about is",
        "number": 123,
        "list": [1, 2, 3]
    }
    print(request)
    return render(request, "about.html", context)
