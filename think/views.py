from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import View 
from django.shortcuts import get_object_or_404
from .models import Think
from .utils import *
from .forms import ThinkForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator 

# Create your views here.
def think_list(request):
 
 
 thinks = Think.objects.all()  
 paginator = Paginator(thinks, 2)
 page_number = request.GET.get('page',1)
 page = paginator.get_page(page_number)

 is_paginated = page.has_other_pages()
 if page.has_previous():
      prev_url = '?page={}'.format(page.previous_page_number())
 else:
      prev_url = ''
 if page.has_next():
      next_url = '?page={}'.format(page.next_page_number())
 else:
      next_url = ''

 context = {
      'page_object':page,
      'is_paginated':is_paginated,
      'next_url':next_url,
      'prev_url':prev_url
      }
 return render(request, 'think/index.html', context=context)

def think_detail (request, slug):
    think=Think.objects.get(slug__iexact=slug)
    return render(request, 'think/think_detail.html', context={'think':think})

class ThinkCreate(ObjectCreateMixin,View):
    model_form=ThinkForm
    template='think/think_create_form.html'
   # def get(self,request):
          #  form=PostForm()
         #   return render (request,'blog/post_create_form.html', context={'form':form})
    #def post(self,request):
     #   bound_form=PostForm(request.POST)
     #   if bound_form.is_valid():
         #   new_post=bound_form.save()
        #    return redirect(new_post)
      #  return render(request, 'blog/post_create_form.html', context={'form':bound_form})
class ThinkUpdate(ObjectUpdateMixin,View):
    model= Think
    model_form=ThinkForm
    template='think/think_update_form.html'

class ThinkDelete(ObjectDeleteMixin,View):
    model=Think
    redirect_url='thinks_list_url'
    template='think/think_delete_form.html'

class ThinkDetail (ObjectDetailMixin, View):
    model = Think
    template='think/think_detail.html'
