from django.http import HttpResponse
from django.shortcuts import redirect
def redr(request):
    return redirect('/report')