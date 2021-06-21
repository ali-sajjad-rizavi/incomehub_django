from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.all_users, name='all-users'),
    path('register/', views.register, name='register'),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='users/login.html',
            redirect_authenticated_user=True
        ),
        name='login'
    ),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', views.profile, name='user-profile'),
    path('profile/<int:pk>/', views.UserDetailView.as_view(), name='user'),
    path('my-job-posts/', views.posted_jobs, name='current-user-jobs'),
    path('<int:user_id>/jobs/', views.user_jobs, name='user-jobs'),
    path('my-notifications/', views.notifications, name='notifications'),
    path('my-applications/', views.my_job_applications, name='current-user-job_applications'),
]
