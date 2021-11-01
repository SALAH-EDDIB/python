from django.db import models
from django.contrib.auth.models import User
from departement.models import Departement
from django.urls import reverse

# Create your models here.


class Machine(models.Model):
    name = models.CharField(max_length=120)
    status = models.BooleanField(null=True, blank=True, default=False)
    lastCheckDate = models.DateField(null=True, blank=True)
    nextCheckDate = models.DateField(null=True, blank=True)
    departement = models.ForeignKey(
        Departement, default=None, on_delete=models.CASCADE)
    checker = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True, default='')

    def get_absolute_url(self):
        return reverse("machine:machine-detail", kwargs={"id": self.id})
