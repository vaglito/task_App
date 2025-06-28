from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from ..application.services import TaskService
from ..infrastructure.repositories import DjangoTaskRepository
from .serializers import TaskSerializer

repo = DjangoTaskRepository()
service = TaskService(repo)

class TaskViewSet(ViewSet):

    def list(self, request):
        tasks = service.list_task()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task = service.create_task(serializer.validated_data)
        return Response(TaskSerializer(task).data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        task = service.get_task(int(pk))
        return Response(TaskSerializer(task).data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task = service.update_task(int(pk), serializer.validated_data)
        return Response(TaskSerializer(task).data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        service.delete_task(int(pk))
        return Response(status=status.HTTP_204_NO_CONTENT)