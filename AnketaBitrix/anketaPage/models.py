from django.db import models

# Create your models here.

class PlaceOfRegistrationForLead(models.Model):
    region = models.CharField(max_length=110,verbose_name="Регион проживания Лид")
    idRegion = models.IntegerField(max_length=7,verbose_name="ID региона")

    class Meta:
        verbose_name_plural = ("ЛИД Регион прописки")


class PlaceOfResidenceForLead(models.Model):
    region = models.CharField(max_length=110,verbose_name="Место жительства Лид")
    idRegion = models.IntegerField(max_length=7,verbose_name="ID региона")

    class Meta:
        verbose_name_plural = ("ЛИД Место жительства")

class PlaceOfRegistrationForDeal(models.Model):
    region = models.CharField(max_length=110,verbose_name="Регион проживания Сделка")
    idRegion = models.IntegerField(max_length=7,verbose_name="ID региона")

    class Meta:
        verbose_name_plural = ("СДЕЛКА Регион прописки")

class PlaceOfResidenceForDeal(models.Model):
    region = models.CharField(max_length=110,verbose_name="Место жительства Сделка")
    idRegion = models.IntegerField(max_length=7,verbose_name="ID региона")

    class Meta:
        verbose_name_plural = ("СДЕЛКА Место жительства")