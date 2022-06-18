from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    date_of_birth = models.fields.DateField(verbose_name="Date of birth", null=True, blank=True)
    profile_image = models.ImageField(upload_to='movie')
