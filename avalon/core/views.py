import logging

from django.shortcuts import render
from django.conf import settings

# Create your views here.

LOGGER = logging.getLogger(__name__)


def root(request):
    context = {
        'STATIC_ASSET_URL': settings.DEBUG and settings.STATIC_ASSET_URL or settings.STATIC_URL
    }
    return render(request, 'index.html', context=context)
