from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

import json

def home_view(request):

    return render(request, "home/portfolio_home.html", {})
