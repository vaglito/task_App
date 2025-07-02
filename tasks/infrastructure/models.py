from django.db import models
from account.profile.models import AccountModel


class TaskModel(models.Model):
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(null=True, default=True)
    user = models.ForeignKey(
        AccountModel,
        on_delete=models.CASCADE,
        related_name='users'
    )
    description = models.TextField(blank=True)
    state = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['title']
    
    def __str__(self):
        return self.title