import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView

from cafe.models.reservation import Reserve


def reservation_view(request):
    return render(request, 'cafe/reservation.html')


@login_required
def reservation_today_view(request):
    return render(request, 'cafe/reservation-list.html')


@login_required
def reservation_today_api(request):
    reserves = Reserve.objects.filter(
        created_at__gte=datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    )

    return JsonResponse([reserve.to_json() for reserve in reserves], safe=False)


class ReserveCreateView(CreateView):
    model = Reserve
    fields = ['count', 'name']
    context_object_name = 'reserve'
