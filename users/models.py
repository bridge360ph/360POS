from django.db import models
from django.contrib.auth.models import AbstractUser

from gasolinestation.models import GasolineStation


class CustomUser(AbstractUser):
    POSITIONS = (
        ('Cashier', 'Cashier'),
        ('Manager', 'Manager'),
        ('Owner', 'Owner'),
    )
    full_name = models.CharField(max_length=150, null=True, blank=True)
    nickname = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(upload_to="user/user-photo/", max_length=100, null=True, blank=True,
              verbose_name="User profile photo")
    position = models.CharField(max_length=150, choices=POSITIONS, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    gas_station_assigned = models.ForeignKey(GasolineStation, null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "User list"
        verbose_name_plural = "User Lists"
        ordering = ['-first_name']

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def combine_name(self):
        get_full_name = self.first_name + ' ' + self.last_name
        return get_full_name
    
    def save(self, *args, **kwargs):
        self.full_name = self.combine_name()
        super().save(*args, **kwargs)

