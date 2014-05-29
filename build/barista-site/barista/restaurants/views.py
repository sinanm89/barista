import json
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView
from barista.restaurants.forms import RestaurantFormSet
from barista.restaurants.models import Restaurant


class EligibleRestaurantsListView(FormView):
    template_name = "restaurants/list.html"
    form_class = RestaurantFormSet
    success_url = '.'

    def set_form_ids(self, restaurant_formset):
        for restaurant in restaurant_formset:
            restaurant['id'] = restaurant['id'].id

        return restaurant_formset

    def post(self, request, *args, **kwargs):
        form = RestaurantFormSet(data=self.request.POST)

        if form.is_valid():
            data_list = []
            for data in form.cleaned_data:
                data_list.append(data)
            data_list = self.set_form_ids(data_list)
            return HttpResponse(json.dumps(data_list), content_type="application/json")

    def get_context_data(self, **kwargs):
        context = super(EligibleRestaurantsListView, self).get_context_data(**kwargs)
        extra_context = {
            'restaurant_forms' : RestaurantFormSet(queryset=Restaurant.objects.all()[:3]),
            'all_restaurants' : Restaurant.objects.all(),
        }
        context.update(extra_context)
        return context

class ResultView(TemplateView):
    template_name = "restaurants/results.html"

