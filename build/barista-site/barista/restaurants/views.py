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

    def get_eligible_restaurants(self, data):
        eligible_restaurant_list = Restaurant.objects.all()
        for obj in data:
            obj['id'] = obj['id'].id
        # Do logic magic
        return data

    def post(self, request, *args, **kwargs):
        print '------> POST HERE'
        form = RestaurantFormSet(data=self.request.POST)

        if form.is_valid():
            data_list = []
            print '----------> VALID FORM'
            for data in form.cleaned_data:
                print data
                data_list.append(data)
            data_list = self.get_eligible_restaurants(data_list)
            print data_list
            return HttpResponse(json.dumps(data_list), content_type="application/json")

        #import pdb; pdb.set_trace()
        #return super(EligibleRestaurantsListView, self).post(request, *args, **kwargs)

    def form_valid(self, form):

        return HttpResponseRedirect()

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

