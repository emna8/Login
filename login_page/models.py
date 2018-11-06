from django.db import models
from django.core.validators import RegexValidator

class User (models.Model):
    Cin= models.CharField(primary_key=True, validators=[RegexValidator(regex='^.{8}$', message='Length has to be 8', code='nomatch')],max_length=8)
    Name=models.CharField(max_length=20)
    Email=models.EmailField(max_length=254) 
    #Photo =models.ImageField(null=True)
    
