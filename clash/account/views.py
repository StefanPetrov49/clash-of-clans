from django.shortcuts import render

from clash.account.utils import get_user


# Create your views here.

def details_account(request, player_tag):
    player_tag = player_tag
    print(player_tag)
    user_info = get_user(player_tag)
    context = {
        'name': user_info[0],
        'trophies': user_info[1],
        'icon': user_info[2],
    }
    return render(request, 'account/details-account.html', context)


def search_account(request):
    query_dict = request.GET
    player_tag = query_dict.get('player')
    user_info = get_user(player_tag)
    context = {
        'name': user_info[0],
        'trophies': user_info[1],
        'icon': user_info[2],
    }
    return render(request, 'account/details-account.html', context)