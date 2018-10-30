from django.conf.urls import re_path
from . import views
from .views import ContactView, Success

urlpatterns = [
    re_path('', ContactView.as_view(), name='contact'),
    re_path('success/', Success.as_view(), name='success'),
]