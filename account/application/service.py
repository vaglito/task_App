from ..domain.ports import AccountRepositoryPort
from ..domain.entity import Account

class AccountService:

    def __init__(self, repository: AccountRepositoryPort):
        self.repository = repository
    
    def get_account(self, account_id: int):
        return self.repository.getAccount(account_id)
    
    def create_account(self, account: Account):
        account = Account(id=None, **account)
        return self.repository.createAccount(account)