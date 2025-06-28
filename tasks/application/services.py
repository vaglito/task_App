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
        return self.repository.get_task(task_id)
    
    def update_task(self, task_id: int, task: Task):
        task = Task(id=task_id, **task)
        return self.repository.update_task(task_id, task)
    
    def delete_task(self, task_id: int):
        return self.repository.delete_task(task_id)
    
    