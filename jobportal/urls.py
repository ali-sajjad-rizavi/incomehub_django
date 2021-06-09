from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jobs/', views.JobListView.as_view(), name='jobs'),
    path('jobs/new', views.JobCreateView.as_view(), name='job-create'),
    path('jobs/<int:pk>/', views.JobDetailView.as_view(), name='job'),
    path('jobs/<int:pk>/update', views.JobUpdateView.as_view(), name='job-update'),
    path('jobs/<int:pk>/delete', views.JobDeleteView.as_view(), name='job-delete'),
    path('jobs/<int:job_id>/apply', views.apply_for_job, name='job-apply'),
]
