from django.shortcuts import render
from .models import UserInfo


def show_results(request):
    show = UserInfo.objects.order_by('-score_user')
    return render(request, 'users/results.html', {'show': show})
