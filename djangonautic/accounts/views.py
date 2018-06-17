from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.db import transaction

def signup_view(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #log the user in
            login(request, user)
            return  redirect('articles:article_list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.htm', {'form': form})

def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user in
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:article_list')
            return redirect('articles:article_list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.htm', {'form': form})

def logout_view(request):
    if request.method =='POST':
        logout(request)
        return redirect('articles:article_list')

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
