from rest_framework import serializers
from .models import User

class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('Cin','Name','Email' )