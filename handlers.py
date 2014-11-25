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
        
        photos = None
        autor = None
        decada = None
        tag = None
        
        if self.request.GET:
            try:
                autor = self.request.GET['autor']
            except:
                autor = None
            
            try:
                decada = int(self.request.GET['decada'])
            except:
                decada = None
                
            try:
                tag = self.request.GET['tag']
            except:
                tag = None
            
            q = models.Photo.query()
            if autor:
                q = q.filter(models.Photo.proprietario == autor)
            if decada:
                q = q.filter(models.Photo.decada == decada)
            if tag:
                q = q.filter(models.Photo.tags == tag)
            
            photos = q.fetch(400)
            

            
        params = {
            'debug': '',
            'photos': photos or all_photos,
            'autores': autores or '',
            'autor': autor or '',
            'decada': decada or '',
            'tag': tag or ''
        }
        return self.render_template('galeria.html', **params)

class TagsHandler(BaseHandler):

    def get(self):
    
        all_photos = models.Photo.query().fetch(400)
        all_tags = [] #todo add count
        for p in all_photos:
            for t in p.tags:
                if t not in all_tags:
                    all_tags.append(t)
        all_tags.sort()
        params = {
            'debug': '',
            'tags': all_tags
        }
        return self.render_template('tags.html', **params)        
        
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