from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    POSITIONS = (
        ('Cashier', 'Cashier'),
        ('Manager', 'Manager'),
        ('Owner', 'Owner'),
    )
    nickname = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(upload_to="user/user-photo/", max_length=100, null=True, blank=True,
              verbose_name="User profile photo")
    position = models.CharField(max_length=150, choices=POSITIONS, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "User list"
        verbose_name_plural = "User Lists"
        ordering = ['-first_name']
    
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

