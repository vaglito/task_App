from abc import ABC, abstractmethod
from typing import List
from .entity import Task

class TaskRepositoryPort(ABC):
    @abstractmethod
    def list_task(self) -> List[Task]:
        pass
    
    @abstractmethod
    def getTaskById(self, task_id: int) -> Task:
        pass
    
    @abstractmethod
    def create_task(self, task: Task) -> Task:
        pass
    
    @abstractmethod
    def updateTask(self, task: Task) -> Task:
        pass
    
    @abstractmethod
    def deleteTask(self, task_id: int) -> Task:
        pass