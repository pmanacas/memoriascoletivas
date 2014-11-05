# -*- coding: utf-8 -*-
from webapp2_extras.routes import RedirectRoute

_routes = [
    RedirectRoute(
                    '/sem-javascript/', 
                    'handlers.NoJavascriptHandler', 
                    name='sem-javascript', strict_slash=True),
    RedirectRoute(
                    '/', 
                    'handlers.HomePageHandler', 
                    name='home', strict_slash=True),
    RedirectRoute(
                    '/galeria', 
                    'handlers.GaleriaHandler', 
                    name='galeria', strict_slash=True),
    RedirectRoute(
                    '/projeto', 
                    'handlers.ProjetoHandler', 
                    name='projeto', strict_slash=True),
    RedirectRoute(
                    '/historia', 
                    'handlers.HistoriaHandler', 
                    name='historia', strict_slash=True),
    RedirectRoute(
                    '/contatos', 
                    'handlers.ContatosHandler', 
                    name='contatos', strict_slash=True),
]

def get_routes():
    return _routes

def add_routes(app):
    for r in _routes:
        app.router.add(r)
