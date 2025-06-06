from django.shortcuts import redirect
from django.contrib.auth import logout

# def home(request):
def logout_view(request):
    logout(request)
    return redirect('/')