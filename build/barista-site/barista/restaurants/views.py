from django.views.generic import ListView, DetailView
from barista.restaurants.models import Restaurant

def get_eligible_restaurants(restaurant_list):
    eligible_restaurant_list = restaurant_list
    # Do logic magic
    return eligible_restaurant_list

class EligibleRestaurantsListView(ListView):
    queryset = Restaurant.objects.all()
    template_name = "restaurants/list.html"
    context_object_name = "object_list"


    def get_queryset(self):
        queryset = super(EligibleRestaurantsListView, self).get_queryset()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(EligibleRestaurantsListView, self).get_context_data(**kwargs)
        extra_context = {
            'eligible_restaurants' : get_eligible_restaurants(self.queryset)
        }
        context.update(extra_context)
        return context

