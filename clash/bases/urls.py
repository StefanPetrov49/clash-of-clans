from django.urls import path

from clash.bases.views import show_all_townhalls

urlpatterns = (
    path('', show_all_townhalls, name='show all townhalls'),
)