from django.urls import path

from clash.account.views import details_account, search_account

urlpatterns = (
    path('', search_account, name='details account'),
    path('<str:player_tag>/', details_account, name='details account'),
)
