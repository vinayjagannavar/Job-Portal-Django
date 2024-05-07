from django.db import models
from users.models import User
from company.models import Company

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.PositiveIntegerField(default=50000)
    requirements = models.TextField()
    ideal_candidates = models.TextField()
    is_available = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ApplyJobs(models.Model):
    status_choices = (
        ('Accepted','Accepted'),
        ('Declined','Declined'),
        ('Pending','Pending'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=status_choices)