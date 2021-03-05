from django.shortcuts import render
from .models import Candidate as CandidateModel
from jobs.models import Job
from skills.models import Skill


# Create your views here.
def index(request):
    candidates = CandidateModel.objects.all()
    jobs = Job.objects.all()
    search_input = request.GET.get('search-area', None)
    if search_input:
        candidates_match = CandidateFinder(search_input)
        candidates = candidates.filter(full_name__in=candidates_match)
    return render(request, 'index.html', {'candidates': candidates, 'jobs': jobs})


def CandidateFinder(search_input):
    # Title Match
    job_title = Job.objects.get(id=search_input).title
    candidates = CandidateModel.objects.filter(title=job_title)
    # Having as many skill matches as possible.
    max_skills_match = 0
    candidates_match = set()
    skills = Job.objects.get(id=search_input).skills.all()
    for candidate in candidates:
        skill_match = len(skills.intersection(candidate.skills.all()))
        if max_skills_match < skill_match:
            candidates_match.clear()
            max_skills_match = skill_match
            candidates_match.add(candidate.full_name)
        if max_skills_match == skill_match:
            candidates_match.add(candidate.full_name)
    return candidates_match
