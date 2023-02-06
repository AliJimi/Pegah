from django.shortcuts import render
from django.views.generic import CreateView

from cafe.models.reservation import Reserve


def reservation_view(request):
    return render(request, 'cafe/reservation.html')


class ReserveCreateView(CreateView):
    model = Reserve
    fields = ['count', 'name']
    context_object_name = 'reserve'
