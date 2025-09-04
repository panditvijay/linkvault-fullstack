from django.db import models

# Create your models here.

import uuid

class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField(max_length=500)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    # This is the crucial field. It's just an integer, NOT a ForeignKey.
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title