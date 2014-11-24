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
        
        all_photos = models.Photo.query().fetch(400)
        autores = []
        for p in all_photos:
            if p.proprietario not in autores and p.proprietario != "":
                autores.append(p.proprietario)
        autores.sort()
        
        if self.request.GET:
            if self.request.GET['autor']:
                autor = self.request.GET['autor']
            else:
                autor = None
            
            if self.request.GET['decada']:
                decada = int(self.request.GET['decada'])
            else:
                decada = None
                
            if self.request.GET['tag']:
                tag = self.request.GET['tag']
            else:
                tag = None
            
            q = models.Photo.query()
            if autor:
                q = q.filter(models.Photo.proprietario == autor)
            if decada:
                q = q.filter(models.Photo.decada == decada)
            if tag:
                q = q.filter(models.Photo.tags == tag)
            
            photos = q.fetch(400)
            
        else:
            photos = all_photos
            autor = None
            decada = None
            
        params = {
            'debug': '',
            'photos': photos,
            'autores': autores,
            'autor': autor,
            'decada': decada
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