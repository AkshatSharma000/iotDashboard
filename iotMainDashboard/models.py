from django.db import models

# Create your models here.
class device_info(models.Model):
    username = models.CharField(default='Akshat',max_length=20)
    details = models.JSONField()

    def __str__(self):
        return self.username


