from django.db import models
from django.utils import timezone
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext_lazy as _


class Opinion(models.Model):
    opinion = models.TextField()
    created_by = models.ForeignKey()
    date_created = models.DateTimeField(_("Restaurant Date Created"), default=timezone.now)


class OpinionVote(models.Model):
    """
    Profiles upvoting and downvoting being stored.
    Opinionvote.objects.filter(opinion__id=123)
    """
    upvote = models.IntegerField(_("Number of times upvoted"), default=1)
    downvote = models.IntegerField(_("Number of times downvoted"), default=0)
    comment = models.ForeignKey(Opinion,_("Number of times downvoted"), default=0)
    upvoters = models.ForeignKey()
    date_created = models.DateTimeField(_("Restaurant Date Created"), default=timezone.now)

    class Meta:
        verbose_name = _('Restaurant')
        verbose_name_plural = _('Restaurants')
        ordering = ["name"]

    def __unicode__(self):
        return smart_unicode(self.name)
