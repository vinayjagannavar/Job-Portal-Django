from django.shortcuts import render
from job.models import Job, ApplyJobs

def home(request):
    return render(request, 'website/home.html')

def job_listings(request):
    jobs = Job.objects.filter(is_available = True).order_by('-timestamp')
    context = {'jobs':jobs}
    return render(request, 'website/job_listing.html', context)

def job_details(request, pk):
    if ApplyJobs.objects.filter(user=request.user, job=pk).exists():
        has_applied = True
    else:
        has_applied = False
    job = Job.objects.get(pk=pk)
    context={'job':job,
             'has_applied' : has_applied}
    return render(request, "website/job_details.html", context)