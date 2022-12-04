from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import traceback

from modules.viewhelper import ViewHelper, FormHelper
from modules._webbase import wb

vh = ViewHelper("_site", ["base"])
fh = FormHelper(vh)

def main(request):
    request.session, l = vh.handle_requestdata(request)
    
    params = {"title": "Netscraper Dashboard"}

    params["d"] = wb.lr.get_complete_stats()

    return render(request, "main.html", vh.build_params(["main"], params, l))

def log(request):
    request.session, l = vh.handle_requestdata(request)
    
    params = {"title": "Netscraper Dashboard"}

    params["log"] = wb.lr.get_whole_jsonlog()

    return render(request, "log.html", vh.build_params(["main"], params, l))

