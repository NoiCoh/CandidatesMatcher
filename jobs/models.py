# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from skills.models import Skill


# Create your models here.
class Job(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    Company = models.CharField(max_length=50)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.title
