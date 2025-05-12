from django.db import models
from django.contrib.auth.models import AbstractUser

class Profile(AbstractUser):
    SEX_CHOICES=((1,'F'),
                 (2,'M'))
    
    BLOOD_TYPES=((1,'A+'),(2,'A-')
                 (3,'B+'),(4,'B-')
                 (5,'AB+'),(6,'AB-'),
                 (7,'O+'),(8,'O-'))
    name=models.CharField(max_length=144)
    email=models.EmailField(max_length=255,unique=True)
    username=None
    sex=models.IntegerField(choices=SEX_CHOICES)
    weigth=models.DecimalField(decimal_places=2,max_digits=5)
    heigth=models.DecimalField(decimal_places=2,max_digits=3)
    emergency_phone_number=models.CharField(10)
    blood_type=models.IntegerField(choices=BLOOD_TYPES)
    USERNAME_FIELD=email
    REQUIRED_FIELDS=[]


class Allergy(models.Model):
    name=models.CharField(max_length=144)
    allergy_type=models.IntegerField(default=1)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)