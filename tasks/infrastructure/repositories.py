from django.shortcuts import get_object_or_404
from ..domian.entity import Task
from ..domian.ports import TaskRepositoryPort
from .models import TaskModel

# Use ORM DJANGO

class DjangoTaskRepository(TaskRepositoryPort):

    def list_task(self):
        return [self._to_entity(t) for t in TaskModel.objects.all()]
    
    def create_task(self, task: Task):
        task_obj = TaskModel.objects.create(
            title=task.title,
            description=task.description,
            state=task.state
        )
        return self._to_entity(task_obj)
    
    def getTaskById(self, task_id: int):
        task = get_object_or_404(TaskModel, id=task_id)
        return task
    
    def updateTask(self, task_id: int, task: Task):
        task_obj = TaskModel.objects.get(id=task_id)
        task_obj.title = task.title
        task_obj.description = task.description
        task_obj.state = task.state
        task.obj.save()
        return self._to_entity(task_obj)
    
    def deleteTask(self, task_id: int):
        return TaskModel.objects.get(id=task_id).delete()
    
    def _to_entity(self, model: TaskModel):
        return Task(
            id=model.id,
            title=model.title,
            description=model.description,
            state=model.state,
        )