from ..domian.entity import Task
from ..domian.ports import TaskRepositoryPort
from .models import TaskModel

class DjangoTaskRepository(TaskRepositoryPort):

    def list_task(self):
        return [Task(**task.__dict__) for task in TaskModel.objects.all()]
    
    def create_task(self, task: Task):
        task_obj = TaskModel.objects.create(
            title=task.title,
            description=task.description,
            state=task.state
        )
        return Task(**task_obj.__dict__)