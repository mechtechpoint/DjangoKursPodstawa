from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Produkt(models.Model):
    nazwa = models.CharField(max_length=50)
    opis = models.TextField(blank=True)
    cena = models.TextField(blank=True)
    dodane = models.IntegerField(default=0)
    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkt"

class Koszyk(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nazwa_user = models.CharField(max_length=50)
    opis_user = models.TextField(blank=True)
    cena_user = models.TextField(blank=True)
    dodane_user = models.IntegerField(default=0)
    def __str__(self):
        name = str(self.nazwa_user) + " - " + str(self.user)
        return name

    class Meta:
        verbose_name = "Koszyk"
        verbose_name_plural = "Koszyk"


