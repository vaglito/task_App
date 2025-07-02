from rest_framework import serializers
from .models import AccountModel

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountModel
        fields = '__all__'
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'year_of_birth': {'required': True},
        }