import django_filters
from job.models import Job

class Jobfilter(django_filters.FilterSet):
    class Meta:
        model = Job
        fields = ['title', 'state', 'job_type', 'industry']