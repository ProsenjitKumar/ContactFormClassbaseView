from django import forms
from django.conf import settings
from django.core.mail import send_mail

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    def send_mail(self):
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        # subject = 'From Prosnjit Localhost'
        # message = '%s %s' % (comment, name)
        emailFrom = self.cleaned_data['email']
        cc_myself = self.cleaned_data['cc_myself']
        emailTo = ['prosenjitearnkumar@gmail.com']
        send_mail(subject, message, emailFrom, emailTo, fail_silently=False,)

