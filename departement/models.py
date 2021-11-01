from django.db import models
from django.urls import reverse
# Create your models here.


class Departement(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("departement:departement-detail", kwargs={"id": self.id})
