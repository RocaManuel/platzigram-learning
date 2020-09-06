"""Platzigram views. """

#Django
from django.http import JsonResponse

# Utilities
from datetime import datetime

def health_check(request):
    """Checks heatlh status"""
    return JsonResponse({
        'success': True,
        'time': datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    })