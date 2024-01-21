from django.shortcuts import render
from Applications.accounts.models import Permissions
from django.contrib.auth.decorators import user_passes_test


def permissions_check(user):
    try:
        permission = Permissions.objects.filter(
            user__exact=user.id).values_list('trading_access', flat=True)[0]
    except:
        permission = False
    return permission


@user_passes_test(permissions_check, login_url='/unauthorized_access/', redirect_field_name=None)
def trading_view(request):

    context = {}

    return render(request, "trading/trading.html", {'context': context})
