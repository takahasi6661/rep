from django.urls import path
from .views import *
urlpatterns= [
    path ('',partner_list, name='partner_list_url'),
    path ('partner/<str:slug>/',partner_detail, name='partner_detail_url')
]