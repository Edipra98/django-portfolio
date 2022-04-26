from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
import mimetypes
import os
from django.views.generic import TemplateView

# Create your views here.

class HomeTemplate(TemplateView):
	template_name = 'layout/home.html'


class ProjectTemplate(TemplateView):
	template_name = 'layout/projects.html'


class ContactTemplate(TemplateView):
	template_name = 'layout/contact.html'
	
class ThankYouTemplate(TemplateView):
	template_name = 'layout/thank-you.html'