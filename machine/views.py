from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)

from .forms import MachineModelForm
from .models import Machine
from departement.models import Departement


class MachineCreateView(CreateView):
    template_name = 'machine/machine_create.html'
    form_class = MachineModelForm
    queryset = Machine.objects.all()

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.checker = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('machine:machine-list')


class MachineListView(ListView):
    template_name = 'machine/machine_list.html'
    queryset = Machine.objects.all()


def machineBydepartement_list(request, id):
    departement = Departement.objects.get(id=id)
    machines = departement.machine_set.filter(status=False)
    context = {
        "object_list": machines
    }
    return render(request, "machine/machine_by_list.html", context)


class MachineDetailView(DetailView):
    template_name = 'machine/machine_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Machine, id=id_)


class MachineUpdateView(UpdateView):
    template_name = 'machine/machine_create.html'
    form_class = MachineModelForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Machine, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('machine:machine-list')


class MachineDeleteView(DeleteView):
    template_name = 'machine/machine_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Machine, id=id_)

    def get_success_url(self):
        return reverse('machine:machine-list')


def machineCheckView(request, id):
    obj = get_object_or_404(Machine, id=id)
    form = MachineModelForm(request.POST or None, instance=obj)
    if request.method == "POST":

        form.instance.status = True
        form.instance.nextCheckDate = request.POST.get('nextCheckDate')
        form.instance.description = request.POST.get('description')

        obj.save()

        return redirect('../../../machine/'+str(obj.departement.id))

    context = {
        "object": obj,
        "form": form
    }
    return render(request, "machine/machine_check.html", context)
