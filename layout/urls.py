from django.urls import path
from .views import HomeTemplate, ProjectTemplate, ContactTemplate, ThankYouTemplate
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'layout'

urlpatterns = [
	path('', HomeTemplate.as_view(), name='home'),
	path('projects/', ProjectTemplate.as_view(), name='projects'),
	path('contact/', ContactTemplate.as_view(), name='contact'),
	path('thank-you/', ThankYouTemplate.as_view(), name='thank-you'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)