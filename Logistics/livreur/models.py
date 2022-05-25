from django.db import models


class Livreur(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __repr__(self):
        return self.name + ' is added.'


class Vehicule(models.Model):
    name = models.CharField(max_length=255)
    immatriculation = models.CharField(max_length=50)

    def __repr__(self):
        return self.name + ' is added.'


class Circuit(models.Model):
    livruer = models.ForeignKey(Livreur, on_delete=models.CASCADE)
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)


