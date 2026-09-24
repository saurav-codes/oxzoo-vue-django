from django.db import models


class Heartbeat(models.Model):
    # One row per beat tick; /api/stats counts them to prove postgres works end to end.
    line = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
