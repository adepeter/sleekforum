from django.views.generic import FormView
from .forms import ContactUsForm

class ContactUs(FormView):
    template_name = 'flatpages/contact_us.html'
    form_class = ContactUsForm
