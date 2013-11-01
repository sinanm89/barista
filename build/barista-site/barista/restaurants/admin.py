from django.contrib import admin
from barista.restaurants.models import Restaurant


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "date_created", "times_chosen")
    prepopulated_fields = {
        "slug" : ("name",),
        }

admin.site.register(Restaurant, RestaurantAdmin)
