from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ..adapters.views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
]