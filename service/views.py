from django.shortcuts import render
from django.views import View
from .models import Services

# Create your views here.
class ServiceView(View):
    def get(self,request):
        services = Services.objects.all()
        return render(request, 'services/service.html',
                      {'services': services})


class ServiceDetailView(View):
    def get(self, request, service_id):
        detail = Services.objects.get(id=service_id)
        return render(request, 'services/detail.html',
                      {'detail': detail})
