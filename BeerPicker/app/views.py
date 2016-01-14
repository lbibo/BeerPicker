"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import *

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    user = request.user
    try:
        user_profile = User_Profile.objects.get(id = user.id)
    except:
        user_profile = user
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Beer Recommender',
            'year':datetime.now().year,
            'user_profile':user_profile,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'Beer Recommender: About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )
