
from django.views.generic import FormView, TemplateView
from .forms import ContactForm


class ContactView(FormView):
    template_name = 'contact/contact_me.html'
    form_class = ContactForm
    success_url = '/success/'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        #context["testing_out"] = "this is a new context var"
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #form.send_email()
        #print "form is valid"

        form.send_mail()
        print("Form Is Valid")
        return super(ContactView, self).form_valid(form)


class Success(TemplateView):
    template_name = "contact/success.html"


