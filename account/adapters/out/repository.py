from django.shortcuts import get_object_or_404
from ...domain.entity import Account
from ...domain.ports import AccountRepositoryPort
from ...profile.models import AccountModel

class AccountRepository(AccountRepositoryPort):

    def getAccount(self, account_id: int):
        account = get_object_or_404(AccountModel.objects.filter(is_active=True), id=account_id)

        return account
    
    def createAccount(self, account: Account):
        account_obj = AccountModel(
            first_name=account.first_name,
            last_name=account.last_name,
            username=account.username,
            email=account.email,
            password=account.password,
            year_of_birth=account.year_of_birth
        )

        account_obj.set_password(account.password)
        account_obj.save()

        return account_obj