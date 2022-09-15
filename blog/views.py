from django.views import generic

from .forms import InquiryForm

class IndexView(generic.TemplateView):
    template_name = "index2.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm