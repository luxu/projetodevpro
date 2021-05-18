from django.http import HttpResponse
from django.shortcuts import render, redirect

from devpro.encurtador.models import UrlRedirect


def redirecionar(request, slug):
    urlRedirect = UrlRedirect.objects.get(slug=slug)
    # return HttpResponse(f'Olá Django: {slug}')
    return redirect(urlRedirect.destino)