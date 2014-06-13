import hashlib
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import EmailField
from django.shortcuts import render, redirect
from django.contrib import messages


def add_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if not valid_email_address(email):
            messages.add_message(request, messages.ERROR, 'Invalid email')
            return redirect('/')

        firstname = request.POST.get('first_name')
        if len(firstname) == 0:
            messages.add_message(request, messages.ERROR, 'First name is required')
            return redirect('/')

        lastname = request.POST.get('last_name')
        username = username_md5(email + firstname + lastname)

        user = User(username=username, email=email, first_name=firstname, last_name=lastname)
        user.save()

        return redirect('/')

    return redirect('/')


def delete_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        User.objects.filter(username=username).delete()

        messages.add_message(request, messages.SUCCESS, 'User deleted')
        return redirect('/')



def edit_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        fname = request.POST.get('edit_first_name')
        lname = request.POST.get('edit_last_name')
        print username, fname, lname, email, len(email), len(fname), len(lname)

        user = User.objects.get(username=username)
        if len(email) is not 0:
            user.email = email
        if len(fname) is not 0:
            user.first_name = fname
        if len(lname) is not 0:
            user.last_name = lname

        user.save()
        messages.add_message(request, messages.SUCCESS, 'User edited successfully')
        return redirect('/')


def username_md5(input):
    """
    MD5 hash the input string and return the first 30 characters of it - used for Django's username field
    """
    return hashlib.md5(input.lower()).hexdigest()[:30]


def valid_email_address(email):
    """
    Verify that the input is in valid email format
    """
    try:
        EmailField().clean(email)
        return True
    except ValidationError:
        return False
