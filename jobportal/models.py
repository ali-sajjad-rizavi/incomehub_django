from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Job(models.Model):
    JOB_CATEGORIES = [
        ('other', 'Other'),
        ('it', 'IT and Software'),
        ('data_entry', 'Data Entry'),
        ('graphic_design', 'Graphic Design'),
        ('teaching', 'Teaching'),
        ('home_tuition', 'Home Tuition'),
    ]

    JOB_TYPE = [
        ('full_time', 'Full time'),
        ('part_time', 'Part time'),
        ('contract', 'Contract'),
    ]

    LOCATION_CHOICES = [
        ('lahore', 'Lahore'),
        ('karachi', 'Karachi'),
        ('islamabad', 'Islamabad'),
    ]

    title = models.CharField(max_length=100)
    image = models.ImageField(default='job-picture.jpg', upload_to='job-images')
    type = models.CharField(max_length=50, choices=JOB_TYPE)
    description = models.TextField()
    company_name = models.CharField(max_length=100)
    company_description = models.TextField()
    salary = models.IntegerField()

    category = models.CharField(max_length=50, choices=JOB_CATEGORIES)
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('job', kwargs={'pk': self.pk})


class JobApplication(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='job-application-resumes')
    cover_letter = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application: '{self.applicant.username}' applied to '{self.job.title}'"
