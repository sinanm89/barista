from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views.generic import ListView, DetailView, TemplateView
from barista.restaurants.models import Restaurant
from barista.restaurants.utils import is_lunchtime


class EligibleRestaurantsListView(ListView):
    queryset = Restaurant.objects.all()
    template_name = "restaurants/list.html"
    context_object_name = "object_list"

    def dispatch(self, request, *args, **kwargs):
        if is_lunchtime():
            return HttpResponseRedirect(reverse('lunchtime:results'))
        return super(EligibleRestaurantsListView, self).dispatch(request, *args, **kwargs)


    def get_queryset(self):
        queryset = super(EligibleRestaurantsListView, self).get_queryset()

        return queryset


    def get_eligible_restaurants(self):
        eligible_restaurant_list = self.queryset

        # Do logic magic
        return eligible_restaurant_list

    def get_context_data(self, **kwargs):
        context = super(EligibleRestaurantsListView, self).get_context_data(**kwargs)
        extra_context = {
            'eligible_restaurants' : self.get_eligible_restaurants()
        }
        context.update(extra_context)
        return context

class ResultView(TemplateView):

    template_name = "restaurants/results.html"
