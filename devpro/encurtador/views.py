from django.http import HttpResponse
from django.shortcuts import render, redirect

from devpro.encurtador.models import UrlRedirect


def redirecionar(request, slug):
    urlRedirect = UrlRedirect.objects.get(slug=slug)
    return redirect(urlRedirect.destino)


def relatorios(requisicao, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    url_reduzida = requisicao.build_absolute_uri(f'/{slug}')
    contexto = {
	    'reduce': url_redirect,
	    'url_reduzida': url_reduzida
    }
    return render(requisicao, 'encurtador/relatorio.html', contexto)