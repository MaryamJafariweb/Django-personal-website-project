from django.shortcuts import render, redirect
from django.views import View
import os
from django.http import FileResponse
from django.contrib import messages
from .models import PersonalInfo

# Create your views here.

class HomeView(View):
    def get(self, request):
        personal = PersonalInfo.objects.all()
        file_path = os.path.join('media', 'resume.pdf')
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                response = FileResponse(f, as_attachment=True, filename='resume.pdf')
                return response
        else:
            messages.error(request, 'بارگذاری انجام نشد ، مجدد تلاش کنید!', 'error')
            # return redirect('home:home')
        return render(request, 'home/home.html', {'personal': personal})


