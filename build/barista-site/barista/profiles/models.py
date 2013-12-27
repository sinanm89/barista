from django.utils.translation import ugettext_lazy as _
from django.contrib.gis.db import models

class ConnectedAccount(models.Model):
    name = models.CharField(_('first name'), max_length=255, blank=True)
    identifier = models.CharField(max_length=100, help_text=_("Example: Facebook ID or Twitter ID"))

    class Meta:
        unique_together = (
            ("name", "identifier"),
        )

