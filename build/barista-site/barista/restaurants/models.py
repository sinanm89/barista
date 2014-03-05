from django.db import models
from django.utils import timezone
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext_lazy as _


class Restaurant(models.Model):
    """
    Restaurants
    """
    name = models.CharField(_('Restaurant Name'), max_length = 255, default="Restaurant")
    slug = models.SlugField(_('Slug'), max_length = 255, default="restaurant")
    category = models.ManyToManyField("RestaurantCategory", blank=True, null=True,
                                      verbose_name=_("Categories"),
                                      related_name="category",
                                      help_text="Check all that apply<br />")
    date_created = models.DateTimeField(_("Restaurant Date Created"), default=timezone.now)
    times_chosen = models.IntegerField(_("Times this category has been chosen"), default=0)

    class Meta:
        verbose_name = _('Restaurant')
        verbose_name_plural = _('Restaurants')
        ordering = ["name"]

    def __unicode__(self):
        return smart_unicode(self.name)

class RestaurantCategory(models.Model):
    """
    A Restaurant Category
    """

    name = models.CharField(_("Category Name"), max_length=255)
    order = models.PositiveIntegerField(_("Order"), default=0)
    times_chosen = models.IntegerField(_("Times this category has been chosen"), default=0)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ["order", "-id"]

    def __unicode__(self):
        return smart_unicode(self.name)
