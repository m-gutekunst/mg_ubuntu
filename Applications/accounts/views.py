from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from Applications.accounts.forms import AccountAuthenticationForm, AccountUpdateForm


def logout_view(request):
    logout(request)
    return redirect('mainpage')


def login_view(request):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('mainpage')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('mainpage')

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'accounts/login.html', context)


def account_view(request):

    if not request.user.is_authenticated:
        return redirect("login")

    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "first_name": request.POST['first_name'],
                "last_name": request.POST['last_name'],
            }
            form.save()
            context['success_message'] = "Updated"
    else:
        form = AccountUpdateForm(
            initial={
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
            }
        )
    context['account_form'] = form

    return render(request, 'accounts/account.html', context)


def must_authenticate_view(request):
    return render(request, 'accounts/must_authenticate.html', {})
