from django.db import models


class Notes(models.Model):
    title = models.CharField(max_length=60)
    notes_content = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, db_index=True)
