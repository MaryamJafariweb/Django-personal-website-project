from django.shortcuts import render
from django.views import View
from .models import Portfolio

# Create your views here.
class PortfolioView(View):
    template_name = 'portfolio/portfolio.html'

    def get(self, request):
        portfolio = Portfolio.objects.all()
        return render(request,self.template_name,{'portfolio': portfolio} )


class PortfolioDetailView(View):
    template_name = 'portfolio/detail.html'

    def get(self, request, portfolio_id):
        detail = Portfolio.objects.get(id=portfolio_id)
        return render(request, self.template_name, {'detail': detail})
