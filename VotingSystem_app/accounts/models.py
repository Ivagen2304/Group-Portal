from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    is_moderator = models.BooleanField(default=False)
    warnings = models.PositiveSmallIntegerField(default=0)
    suspension_until = models.DateTimeField(null=True, blank=True)

    def is_suspended(self):
        if self.suspension_until:
            return timezone.now() < self.suspension_until
        return False
