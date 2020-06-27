from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from .forms import CustomerRegisterForm, CustomerUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # gender = form.cleaned_data.get('gender')
            messages.success(request, f'Account created successfully! Please login to continue')
            return redirect('login')
    else:
        form = CustomerRegisterForm()
    return render(request, 'customer/register.html', {'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        c_form = CustomerUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if c_form.is_valid() and p_form.is_valid():
            c_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        c_form = CustomerUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)    
        
    context = {
        'c_form' : c_form,
        'p_form' : p_form,
    }

    return render(request, 'customer/profile.html', context)
