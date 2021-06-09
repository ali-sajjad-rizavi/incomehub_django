from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import jobportal.models as mdl
from jobportal.forms import JobApplicationForm


def index(request):
    context = {'featured_job_list': mdl.Job.objects.order_by('-created_at')[:3]}
    return render(request, 'jobportal/index.html', context=context)


# TODO(Ali): Filter Jobs
class JobListView(ListView):
    model = mdl.Job
    context_object_name = 'job_list'
    template_name = 'jobportal/jobs.html'
    ordering = ['-created_at']
    paginate_by = 6


class JobDetailView(DetailView):
    model = mdl.Job
    context_object_name = 'job'
    template_name = 'jobportal/job-detail.html'


class JobCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = mdl.Job
    fields = ['title', 'image', 'type', 'description', 'company_name', 'company_description', 'salary', 'category',
              'location']
    # Template is "jobportal/job_form.html"
    success_message = "Your job post is now live!"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = mdl.Job
    fields = ['title', 'image', 'type', 'description', 'company_name', 'company_description', 'salary', 'category',
              'location']
    # Template is "jobportal/job_form.html"
    success_message = "Job details updated successfully!"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().author


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = mdl.Job

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        messages.success(self.request, "Job post deleted successfully!")
        return self.request.META["HTTP_REFERER"]


@login_required
def apply_for_job(request, job_id):
    job_to_apply_on = mdl.Job.objects.get(id=job_id)

    # A person cannot apply to his own posted job
    if job_to_apply_on.author == request.user:
        return redirect('jobs')

    if len(mdl.JobApplication.objects.filter(job_id=job_id, applicant=request.user)) > 0:
        messages.warning(request, 'You have already applied for this job once!')
        return redirect('job', job_id)

    if request.method == "POST":
        job_application_form = JobApplicationForm(request.POST, request.FILES)
        job_application_form.instance.job = job_to_apply_on
        job_application_form.instance.applicant = request.user

        if job_application_form.is_valid():
            job_application_form.save()
            messages.success(request, 'You have applied for this job!')
            return redirect('job', job_id)
    else:
        job_application_form = JobApplicationForm()

    context = {'form': job_application_form, 'job': job_to_apply_on}
    return render(request, 'jobportal/jobapplication_form.html', context=context)
