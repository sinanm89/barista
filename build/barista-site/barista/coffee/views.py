
class StreamListView(ListView):
    """
    List the Streams of the User
    """
    model = Stream
    template_name = 'streams/stream_list.html'
    paginate_by = 10

    def get_queryset(self):
        # queryset = super(StreamListView, self).get_queryset()
        queryset = self.request.user.streams.all()
        return queryset

class StreamDetailView(DetailView):
    """
    List the Streams entries

    Pagination is disabled, to enable uncomment.
    """
    model = Stream
    template_name = 'streams/stream_detail.html'
    slug_field = 'id'
    # paginate_by = 20
    # paginator_class = Paginator
    # page_kwarg = 'page'

    def get_context_data(self, **kwargs):
        """
        Get the Stream object and entries into seperate objects. also paginate if necessary
        """
        context = super(StreamDetailView, self).get_context_data(**kwargs)
        stream = self.get_object()
        stream_entries = stream.entries.all()
        # self.request.user also goes to the template
        # paginator, page, entry_set, is_paginated = self.paginate_queryset(stream_entries, page_size=self.paginate_by)
        extra_context = {
            'entry_set' : stream_entries,
        #     'paginator' : paginator,
        #     'page_obj' : page,
        #     'is_paginated' : is_paginated,
        }
        context.update(extra_context)
        return context

    # def paginate_queryset(self, queryset, page_size):
    #         """
    #         Paginate the queryset, if needed.
    #         """
    #         paginator = self.paginator_class(queryset,self.paginate_by)
    #         page_kwarg = self.page_kwarg
    #         page = self.request.GET.get(page_kwarg) or 1
    #
    #         try:
    #             page_number = int(page)
    #
    #         except ValueError:
    #             if page == 'last':
    #                 page_number = paginator.num_pages
    #             else:
    #                 raise Http404(_("Page is not 'last', nor can it be converted to an int."))
    #         try:
    #             page = paginator.page(page_number)
    #             return (paginator, page, page.object_list, page.has_other_pages())
    #         except InvalidPage as e:
    #             raise Http404(_('Invalid page (%(page_number)s): %(message)s') % {
    #                                 'page_number': page_number,
    #                                 'message': str(e)
    #             })
