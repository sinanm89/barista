from django.contrib.gis.db import models
from django.utils import timezone
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext_lazy as _


class Restaurant(models.Model):
    """
    User Streams
    """
    name = models.CharField(_('Restaurant Name'), max_length = 255, default='Restaurant')
    # profile = models.ForeignKey("profiles.CustomUser", related_name="streams")

    date_created = models.DateTimeField(_("Stream Date Created"), default=timezone.now)

    def __unicode__(self):
        return smart_unicode(self.name)

    class Meta:
        verbose_name = _('Restaurant')
        verbose_name_plural = _('Restaurants')
        ordering = ["name"]