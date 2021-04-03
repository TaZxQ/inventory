# django imports
from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .managers import UserManager


class UserAccount(AbstractBaseUser):
    """Database model for users in the system"""
    email = models.EmailField(verbose_name="email", max_length=80, unique=True, null=False)
    first_name = models.CharField(max_length=30, unique=False, null=True)
    middle_name = models.CharField(max_length=30, unique=False, null=True)
    last_name = models.CharField(max_length=30, unique=False, null=True)
    city = models.CharField(max_length=60, unique=False, null=True)
    state = models.CharField(max_length=60, unique=False, null=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        """Return string representation of our user"""
        return self.email

    class Meta:
        db_table = 'user_account'
