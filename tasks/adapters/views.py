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

    def partial_update(self, request, pk=None):
        task = service.get_task(int(pk))
        data = request.data

        current_data = {
            "title": task.title,
            "state": task.state,
            "description": task.description
        }

        current_data.update(data)

        serializer = TaskSerializer(data=current_data)
        serializer.is_valid(raise_exception=True)

        update_task = service.update_task(int(pk), serializer.validated_data)
        return Response(TaskSerializer(update_task).data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        task = service.get_task(int(pk))
        service.delete_task(task.id)
        return Response({"detail": "Tarea correctamente eliminada."}, status=status.HTTP_204_NO_CONTENT)
