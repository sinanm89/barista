from django.db import models
from django.utils import timezone
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext_lazy as _


class Restaurant(models.Model):
    """
    User Streams
    """
    name = models.CharField(_('Restaurant Name'), max_length = 255, default='Restaurant')
    slug = models.CharField(_('Slug'), max_length = 255, default='Restaurant')
    # profile = models.ForeignKey("profiles.CustomUser", related_name="streams")
    category = models.ManyToManyField("RestaurantCategory", blank=True, null=True, verbose_name=_("Restaurant Categories"), related_name="category",
                help_text="Check all that apply<br />")
    date_created = models.DateTimeField(_("Restaurant Date Created"), default=timezone.now)
    times_chosen = models.IntegerField(_("Times this category has been chosen"), default=0)

    def __unicode__(self):
        return smart_unicode(self.name)

    class Meta:
        verbose_name = _('Restaurant')
        verbose_name_plural = _('Restaurants')
        ordering = ["name"]

class RestaurantCategory(models.Model):
    """
    A Restaurant Category
    """

    name = models.CharField(_("Category Name"), max_length=255)
    order = models.PositiveIntegerField(_("Order"), default=0)
    times_chosen = models.IntegerField(_("Times this category has been chosen"), default=0)

    class Meta:
        verbose_name = _("Restaurant Category")
        verbose_name_plural = _("")
        ordering = ["order", "-id"]

    def __unicode__(self):
        return smart_unicode(self.name)
