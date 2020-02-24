from django.urls import path
from .views import *
urlpatterns= [
    path ('',think_list, name='thinks_list_url'),
    path ('think/<str:slug>/', ThinkDetail.as_view(),name='think_detail_url' ), #����������� � ���� ���������� ��� ��� ����� ������ ����� � ��� ����� ����������
    path ('create/', ThinkCreate.as_view(), name='think_create_url'),
    path ('think/<str:slug>/update/',ThinkUpdate.as_view(), name='think_update_url'),
    path ('think/<str:slug>/delete/',ThinkDelete.as_view(), name='think_delete_url'),
]