from django.shortcuts import render
from .forms import UserForm

# Create your views here.
def registerUser(req):
    form = UserForm()
    ctx = {
        'form': form
    }
    return render(req, 'accounts/registerUser.html', ctx)
