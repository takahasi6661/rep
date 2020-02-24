from django.shortcuts import render
from .models import Partner

# Create your views here.
def partner_list(request):
  partners=Partner.objects.all()
  return render(request, 'partners/index.html', context={'partners':partners})



def partner_detail (request, slug):
    partner=Partner.objects.get(slug__iexact=slug)
    return render(request, 'partners/partner_detail.html', context={'partner':partner})