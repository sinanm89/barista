from django import forms
from django.forms import formsets
from django.forms.models import modelformset_factory
from django.utils.translation import ugettext_lazy as _
from barista.restaurants.models import Restaurant

class BaseRestaurantOpinionForm(forms.ModelForm):
    """
        Restaurant choice form
            meh:
                informal
                exclamation
                1.
                expressing a lack of interest or enthusiasm.
                "meh, I'm not impressed so far"
    """
    opinion = forms.ChoiceField(label=_("You want this restaurant?"),
                                choices=(('yes', 'yes'), ('no', 'no'), ('meh', 'meh')),
                                required=False,
                                widget=forms.RadioSelect(attrs={'class':'unstyled'}),
                                initial='meh',
                                )

    class Meta:
        model = Restaurant
        fields = ['name', 'opinion']



    def __init__(self, *args, **kwargs):
        super(BaseRestaurantOpinionForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['name'].widget.attrs ['readonly'] = True
        self.fields['name'].widget.attrs ['class'] = 'unstyled'

        #self.fields['name'].widget.attrs['class'] = 'lead'

    def clean_name(self):
        """
        Override the clean method so others can't force POST a name for the restaurant
        Taken from post:
        http://stackoverflow.com/questions/324477/in-a-django-form-how-to-make-a-field-readonly-or-disabled-so-that-it-cannot-b
        """
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.name
        else:
            return self.cleaned_data['name']
RestaurantFormSet = modelformset_factory(Restaurant, BaseRestaurantOpinionForm, extra=0)
