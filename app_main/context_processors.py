from .models import Account

def global_settings(request):
    if request.user.is_authenticated:
        accounts = Account.objects.filter(user=request.user)
    else:
        accounts = Account.objects.none()

    return {
        "accounts": accounts
    }
