import os
from django.views.generic import TemplateView


class BaristaHomeView(TemplateView):
    template_name = "base.html"

    def get(self, request, *args, **kwargs):
        print os.path.join(os.path.realpath(os.path.dirname(__file__)))
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
