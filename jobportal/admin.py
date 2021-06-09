from django.contrib import admin
from . import models as mdl

admin.site.register(mdl.Job)
admin.site.register(mdl.JobApplication)
