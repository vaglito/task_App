from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email

# Create your models here.

class AccountModel(AbstractUser):
    email = models.EmailField(
        _('Email address'),
        unique=True,
        validators=[validate_email]
    )

    year_of_birth = models.DateField(blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True,
        help_text=_('The groups this user belongs to.'),
        verbose_name=_('groups')
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
        help_text=_('Specific permissions for this user.'),
        verbose_name=_('user permissions')
    )


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []