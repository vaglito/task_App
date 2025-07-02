from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from ...application.service import AccountService
from ...profile.serializers import AccountSerializer
from ..out.repository import AccountRepository

repo = AccountRepository()
service = AccountService(repo)

class AccountViewSet(ViewSet):

    def create(self, request):
        serializer = AccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        account = service.create_account(serializer.validated_data)

        return Response(
            AccountSerializer(account).data,
            status=status.HTTP_201_CREATED
        )
    
    def retrieve(self, request, pk=None):
        account = service.get_account(int(pk))

        return Response(
            AccountSerializer(account).data,
            status=status.HTTP_200_OK
        )