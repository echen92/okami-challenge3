from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.

def index(request):
    """
    Renders the homepage
    """

    # Get all Users and exclude my admin account
    context = {'userlist': list(User.objects.all().exclude(username='erik'))}

    return render(request, 'website/index.html', context)