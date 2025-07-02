from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ..adapters.inp.views import AccountViewSet


router = DefaultRouter()
router.register(r'', AccountViewSet, basename='accounts')

urlpatterns = [
    path('', include(router.urls))
]

