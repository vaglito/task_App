from ..domian.ports import TaskRepositoryPort
from ..domian.entity import Task

class TaskService:
    
    def __init__(self, repository: TaskRepositoryPort):
        self.repository = repository
    
    def list_task(self):
        return self.repository.list_task()
    
    def create_task(self, task: Task):
        task = Task(id=None, **task)
        return self.repository.create_task(task)
    
    def get_task(self, task_id: int):
        return self.repository.getTaskById(task_id)
    
    def update_task(self, task_id: int, task: Task):
        task = Task(id=task_id, **task)
        return self.repository.updateTask(task_id, task)
    
    def delete_task(self, task_id: int):
        return self.repository.deleteTask(task_id)
    
    