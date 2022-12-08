from django.db import models

# Create your models here.

class doctor(models.Model):
    name = models.CharField(max_length=150)
    specialization = models.CharField(max_length=150)
    qualification = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class patient(models.Model):
    name = models.CharField(max_length=150)
    birth_year = models.DateField(max_length=10)
    age = models.PositiveBigIntegerField
    gender = models.CharField(max_length=60)
    doctor = models.ForeignKey(doctor,on_delete=models.CASCADE)

    def __str__(self):
        return self.name