from django.contrib.gis.db import models
from django.utils import timezone
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext_lazy as _
from tweetboard.streams.constants import DURATION_CHOICES


class Stream(models.Model):
    """
    User Streams
    """
    name = models.CharField(_('Stream Name'), max_length = 255, default='Default Stream')
    # profile = models.ForeignKey("profiles.CustomUser", related_name="streams")

    excerpt = models.TextField(blank=True, null=True, db_column="entry_excerpt")
    text = models.TextField(blank=True, null=True, db_column="entry_text")

    date_created = models.DateTimeField(_("Stream Date Created"), default=timezone.now)
    start_date = models.DateTimeField(_("Stream Start Date"), default=timezone.now)
    end_date = models.DateTimeField(_("Stream End Date"), default=timezone.now)


    class Meta:
        verbose_name = _('Stream')
        verbose_name_plural = _('Streams')
        ordering = ["-date_created"]

    def __unicode__(self):
        return smart_unicode(self.name)

    @property
    def duration(self):
