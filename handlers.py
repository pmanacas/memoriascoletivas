# -*- coding: utf-8 -*-
from basehandler import BaseHandler
import models
import logging

class HomePageHandler(BaseHandler):

    def get(self):
        params = {
            'debug': '',
        }
        return self.render_template('home.html', **params)


class GaleriaHandler(BaseHandler):

    def get(self):
        # photos = models.Photo.query().order(models.Photo.decada).fetch(400)
        
        all_photos = models.Photo.query().fetch(400)
        autores = []
        for p in all_photos:
            if p.proprietario not in autores and p.proprietario != "":
                autores.append(p.proprietario)
        autores.sort()
        
        if self.request.GET:
            photos = models.Photo.query(models.Photo.proprietario == self.request.GET['autor']).fetch(400)
            autor = self.request.GET['autor']
        else:
            photos = all_photos
            autor = None
        params = {
            'debug': '',
            'photos': photos,
            'autores': autores,
            'autor': autor
        }
        return self.render_template('galeria.html', **params)
        
        
class ProjetoHandler(BaseHandler):

    def get(self):
        return self.render_template('projeto.html')

class HistoriaHandler(BaseHandler):

    def get(self):
        return self.render_template('historia.html')         

class ContatosHandler(BaseHandler):

    def get(self):
        return self.render_template('contatos.html')  
        
class NoJavascriptHandler(BaseHandler):

    def get(self):
        return self.render_template('sem_javascript.html')