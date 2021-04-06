from django.db import models

# Create your models here.

class students(models.Model):
    name=models.CharField(max_length=50, unique=True)
    classandsec=models.CharField(max_length=5)

    def __str__(self):
        return self.name+'of class'+self.classandsec

class attendance(models.Model):
    name = models.CharField(max_length=50)
    classandsec = models.CharField(max_length=5)
    date =models.DateField()
    def __str__(self):
        return self.name + ' of class ' + self.classandsec
