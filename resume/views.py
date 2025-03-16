from django.shortcuts import render
from django.views import View
from .models import Skills, Education

# Create your views here.
class ResumeView(View):
    def get(self, request):
        skill = Skills.objects.all()
        education = Education.objects.all()
        return render(request, 'resume/resume.html',
                      {'skill': skill,
                       'education': education})

