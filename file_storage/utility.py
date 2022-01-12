from django.db import models


class TimestampedModel(models.Model):
    """
    Timestamped Model 
    """
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
