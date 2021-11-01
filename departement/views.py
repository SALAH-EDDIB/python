from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)

from .forms import DepartementModelForm
from .models import Departement


class DepartementCreateView(CreateView):
    template_name = 'departement/departement_create.html'
    form_class = DepartementModelForm
    queryset = Departement.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('departement:departement-list')


class DepartementListView(ListView):
    def get(self, request):
        queryset = Departement.objects.all()
        context = {
            'object_list': queryset
        }
        template_name = 'departement/departement_list.html'
        group = request.user.groups.all()[0].name
        if group == 'checker':
            template_name = 'departement/departementMachine_list.html'
        return render(request, template_name, context)


class DepartementDetailView(DetailView):
    template_name = 'departement/departement_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Departement, id=id_)


class DepartementUpdateView(UpdateView):
    template_name = 'departement/departement_create.html'
    form_class = DepartementModelForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Departement, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('departement:departement-list')


class DepartementDeleteView(DeleteView):
    template_name = 'departement/departement_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Departement, id=id_)

    def get_success_url(self):
        return reverse('departement:departement-list')
