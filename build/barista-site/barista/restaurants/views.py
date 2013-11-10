import json
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, TemplateView, FormView, View
from barista.restaurants.forms import RestaurantFormSet, BaseRestaurantOpinionForm
from barista.restaurants.models import Restaurant
from barista.restaurants.utils import is_lunchtime
from django.forms.models import modelformset_factory



class EligibleRestaurantsListView(FormView):
    template_name = "restaurants/list.html"
    form_class = RestaurantFormSet
    success_url = '.'

    def get_eligible_restaurants(self):
        eligible_restaurant_list = Restaurant.objects.all()

        # Do logic magic
        return eligible_restaurant_list

    def post(self, request, *args, **kwargs):
        print '------> POST HERE'
        form = RestaurantFormSet(data=self.request.POST)
        if form.is_valid():
            print '----------> VALID FORM'
            #for data in form.cleaned_data:
                #print data
        #import pdb; pdb.set_trace()
        return super(EligibleRestaurantsListView, self).post(request, *args, **kwargs)

    def get_form_class(self):

        return super(EligibleRestaurantsListView, self).get_form_class()


    def get_context_data(self, **kwargs):
        context = super(EligibleRestaurantsListView, self).get_context_data(**kwargs)
        extra_context = {
            'opinion_forms' : RestaurantFormSet(),
        }
        #import pdb;pdb.set_trace()
        context.update(extra_context)
        return context


class ResultView(TemplateView):

    template_name = "restaurants/results.html"

