from django.contrib import admin
from barista.restaurants.models import Restaurant, RestaurantCategory


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "date_created", "times_chosen")
    prepopulated_fields = {
        "slug" : ("name",),
        }


class RestaurantCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "times_chosen")

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(RestaurantCategory, RestaurantCategoryAdmin)
