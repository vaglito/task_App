from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from ..application.services import TaskService
from ..infrastructure.repositories import DjangoTaskRepository
from .serializers import TaskSerializer

class TaskViewSet(ViewSet):
    service = TaskService(DjangoTaskRepository())

    def list(self, request):
        tasks = self.service.list_task()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)