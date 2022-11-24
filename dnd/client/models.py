from django.contrib.auth.models import AbstractUser
from django.db import models

RACE_CHOICES = (
    ('human', 'HUMAN'),
    ('orc', 'ORC'),
    ('elf', 'elf'),
)

CLASS_CHOICES = (
    ('warrior', 'WARRIOR'),
    ('wizard', 'WIZARD'),
)


class CustomClient(AbstractUser):
    race = models.CharField(max_length=10, choices=RACE_CHOICES, default='human')
    # слово class зарезервированно в python
    class_name = models.CharField(max_length=10, choices=CLASS_CHOICES, default='warrior')
    money = models.IntegerField(default=0)
    profile_avatar = models.ImageField(null=True, blank=True, upload_to="images/profile/",
                                       default='images/deafult-profile-image.png')   # нужно скачать аву по умолчанию
