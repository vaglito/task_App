from abc import ABC, abstractmethod
from typing import List
from .entity import Account

class AccountRepositoryPort(ABC):

    @abstractmethod
    def getAccount(self, account_id: int) -> Account:
        pass

    @abstractmethod
    def createAccount(self, account: Account) -> Account:
        pass