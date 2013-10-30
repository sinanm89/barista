from django.views.generic import TemplateView
from barista import settings


class BaristaHomeView(TemplateView):
    template_name = "base.html"
    # template_name = "examples/grid/index.html"
    # def get(self, request, *args, **kwargs):
    #
    #     context = self.get_context_data(**kwargs)
    #     # return render_to_response('example.html',{},context_instance=RequestContext(request))
    #     return self.render_to_response(context)
