# class ReportThread(CreateView):
#     model = Thread
#     form_class = ThreadViolationForm
#     query_pk_and_slug = True
#     template_name = f'{TEMPLATE_URL}/report_thread.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['thread'] = self.get_object()
#         return context
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs['object'] = self.get_object()
#         kwargs['request'] = self.request
#         return kwargs
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         return qs.filter(category__slug__iexact=self.kwargs['category_slug'])
