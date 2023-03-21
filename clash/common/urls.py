from django.urls import path

from clash.common.views import index

urlpatterns = (
    path('', index, name='index'),
)