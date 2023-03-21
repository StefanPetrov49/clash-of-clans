from django.shortcuts import render

from clash.bases.models import TownhallSelection


# Create your views here.

def show_all_townhalls(request):
    all_townhalls = TownhallSelection.objects.all()

    context = {
        'all_townhalls': all_townhalls
    }

    return render(request, 'bases/base-selection.html', context)
