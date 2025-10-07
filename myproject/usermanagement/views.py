from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.cache import cache_control , never_cache
from django.db.models import Q
from .forms import SignUpForm, LoginForm, UserUpdateForm
from .models import User 
from django.core.paginator import Paginator
from django.contrib import messages

#signup view
@never_cache
def signup(request):
    if request.user.is_authenticated: 
        return redirect('home')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

#login view
@never_cache
def login_view(request): 
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid username or password")
                return render(request, 'login.html', {'form': form})
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

#user dashboard view
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def home(request):
    if request.user.is_admin:
        return redirect('admin_dashboard')
    return render(request, 'home.html', {'user': request.user})

#adminlogin view
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_login(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            return redirect('admin_dashboard')
        return redirect('home')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                form.add_error(None, "Invalid admin credentials")
                return render(request, 'admin_login.html', {'form': form})
        else:
            return render(request, 'admin_login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'admin_login.html', {'form': form})

#admin dashboard view
@login_required(login_url='admin_login')
@user_passes_test(lambda u: u.is_admin, login_url='admin_login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_dashboard(request):
    query = request.GET.get('q', '')
    users = User.objects.filter(is_active=True, is_admin = False).order_by('-id')


    if query:
        users = users.filter(Q(username__icontains=query) | Q(email__icontains=query))

    paginator = Paginator(users, 10) 
    page_number = request.GET.get('page')
    users_page = paginator.get_page(page_number)
    return render(request, 'admin_dashboard.html', {
        'users': users_page,
        'query': query
    })

@login_required
@user_passes_test(lambda u: u.is_admin, login_url='admin_login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully!")
            return redirect('admin_dashboard')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SignUpForm()

    return render(request, 'add_user.html', {'form': form})

#view for edit user through admin dashboard
@login_required
@user_passes_test(lambda u: u.is_admin, login_url='admin_login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
        else:
            return render(request, 'edit_user.html', {'form': form, 'user': user})
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'edit_user.html', {'form': form, 'user': user})

#view for delete the user
@login_required
@user_passes_test(lambda u: u.is_admin, login_url='admin_login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def soft_delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_active = False
    user.save()
    return redirect('admin_dashboard')

#logout view
@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def admin_logout(request):
    logout(request)
    return redirect('admin_login')

