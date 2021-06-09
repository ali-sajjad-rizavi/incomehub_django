from django import forms
from . import models as mdl


class JobApplicationForm(forms.ModelForm):

    class Meta:
        model = mdl.JobApplication
        fields = ['resume', 'cover_letter']
