from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from jobportal.models import Job, JobApplication


def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Account registered for {username} successfully! You can login.')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', context={'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account information has ben updated!')
            return redirect('user-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'user_update_form': u_form, 'profile_update_form': p_form}
    return render(request, 'users/profile.html', context=context)


@login_required
def posted_jobs(request):
    job_list = Job.objects.filter(author=request.user).order_by('-created_at')
    paginator = Paginator(job_list, 10)
    page_obj = paginator.get_page(request.GET.get('page'))
    context = {
        'page_obj': page_obj,
        'list_count': len(page_obj.object_list),
    }
    return render(request, 'users/current-user-jobs.html', context=context)


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    context_object_name = 'user_'
    template_name = 'users/user-detail.html'


@login_required
def user_jobs(request, user_id):
    job_list = Job.objects.filter(author_id=user_id).order_by('-created_at')
    paginator = Paginator(job_list, 10)
    context = {
        'page_obj': paginator.get_page(request.GET.get('page')),
        'user_': User.objects.get(id=user_id),
    }
    return render(request, 'users/user-jobs.html', context=context)


@login_required
def all_users(request):
    if 'search' in request.GET and request.GET['search']:
        search_query = request.GET['search']
        user_list = User.objects.all().filter(username__contains=search_query).order_by('-date_joined')
    else:
        user_list = User.objects.all().order_by('-date_joined')
    paginator = Paginator(user_list, 10)
    context = {'page_obj': paginator.get_page(request.GET.get('page'))}
    return render(request, 'users/all-users.html', context=context)


@login_required
def notifications(request):
    my_job_posts = Job.objects.filter(author=request.user)
    job_application_list = JobApplication.objects.filter(job__in=my_job_posts).order_by('-created_at')
    paginator = Paginator(job_application_list, 10)
    context = {'page_obj': paginator.get_page(request.GET.get('page'))}
    return render(request, 'users/notifications.html', context=context)
