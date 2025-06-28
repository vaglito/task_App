from typing import List
from .entity import Task

class TaskRepositoryPort:
    
    def list_task(self) -> List[Task]:
        raise NotImplementedError
    
    def get_task(self, task_id: int) -> Task:
        raise NotImplementedError
    
    def create_task(self, task: Task) -> Task:
        raise NotImplementedError
    
    def update_task(self, task: Task) -> Task:
        raise NotImplementedError
    
    def delete_task(self, task_id: int) -> Task:
        raise NotImplementedError