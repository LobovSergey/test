from django.db import models
from datetime import datetime


class File(models.Model):
    file = models.FileField(upload_to="files/")
    uploaded_at = models.DateTimeField(default=datetime.now)
    processed = models.BooleanField(default=False)

    class Meta:
        ordering = ["uploaded_at"]
