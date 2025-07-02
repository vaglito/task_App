from django.shortcuts import get_object_or_404
from ...domain.entity import Account
from ...domain.ports import AccountRepositoryPort
from ...profile.models import AccountModel

class AccountRepository(AccountRepositoryPort):

    def get_account(self, account_id: int, account: Account):
        account = get_object_or_404(AccountModel.objects.filter(is_active=True), id=account_id)

        return account
    
    def create_account(self, account: Account):
        account_obj = AccountModel.objects.create(
            name=account.name,
            last_name=account.last_name,
            email=account.email,
            password=account.password,
            year_of_birth=account.year_of_birth
        )

        return account_obj