import imp
from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.views.generic import TemplateView


class TemplateVerify(TemplateView):
    template_name = 'verify-email.html'
