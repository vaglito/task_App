from rest_framework import serializers
from ..infrastructure.models import TaskModel
from account.profile.serializers import AccountSerializer

class TaskSerializer(serializers.ModelSerializer):
    user = AccountSerializer()
    class Meta:
        model = TaskModel
        fields = '__all__'