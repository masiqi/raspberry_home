#-*-coding:utf8;-*-
from django.http import HttpResponse
from tenjin_shortcuts import render_to_response

def index(request, template_name="www/index.html"):
    rt = render_to_response(template_name, {
    }, context_instance=request)
    return HttpResponse(rt)
