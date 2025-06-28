from ..domian.ports import TaskRepositoryPort
from ..domian.entity import Task

class TaskService:
    
    def __init__(self, repository: TaskRepositoryPort):
        self.repository = repository
    
    def list_task(self):
        return self.repository.list_task()
    
    def create_task(self, task: Task):
        return self.repository.create_task(task)