from django.shortcuts import redirect, render

from .models import User
from .forms import UserForm
from django.contrib import messages

# Create your views here.
def registerUser(req):
    if req.method == 'POST':
        form =  UserForm(req.POST)
        if form.is_valid():
            # for testing an learning purpose
            # Create the user using the form
            # password = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.role = User.CUSTOMER
            # user.set_password(password)
            # user.save()

            # Create the user using the create_user method
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
            )
            user.role = User.CUSTOMER
            user.phone_number = phone_number[0] if len(phone_number) > 0 else ''
            user.save()
            messages.success(req, 'Your account has been registered sucessfully!')
            return redirect('registerUser')
        else:
            print(form.errors)
    else:
        form = UserForm()
    ctx = {
        'form': form
    }
    return render(req, 'accounts/registerUser.html', ctx)
