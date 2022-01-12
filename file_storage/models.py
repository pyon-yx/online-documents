from django.db import models
from django.utils.translation import ugettext as _

from .utility import TimestampedModel
from users.models import User


# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / documents/<code>/<filename>
    return 'documents/{0}/{1}'.format(instance.user.code, filename)


class UserDocuments(TimestampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents')
    name = models.CharField(max_length=255)
    size = models.IntegerField(default=0)
    ext = models.CharField(max_length=255)
    file = models.FileField(upload_to=user_directory_path)

    def __str__(self):
        return f'{self.user.username} - {self.name}'

    class Meta(object):
        verbose_name = _('User Document')
        verbose_name_plural = _('User Documents')
        unique_together = [['user', 'name']]
