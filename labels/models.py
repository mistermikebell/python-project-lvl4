from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Label(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Name'))
    description = models.TextField(blank=True, null=True,
                                   verbose_name=_('Description'))
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, related_name='labels',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.name
