from django.db import models
from skills.models import Skill
from jobs.models import Job


# Create your models here.
class Candidate(models.Model):
    full_name = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.full_name





