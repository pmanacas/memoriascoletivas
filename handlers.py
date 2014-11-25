# -*- coding: utf-8 -*-
from basehandler import BaseHandler
from collections import defaultdict
from operator import itemgetter
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

        q = models.Photo.query()
        
        try:
            autor = self.request.GET['autor']
            if autor == '':
                raise
            q = q.filter(models.Photo.proprietario == autor)
        except:
            autor = None
        
        try:
            decada = int(self.request.GET['decada'])
            if decada == '':
                raise
            q = q.filter(models.Photo.decada == decada)
        except:
            decada = None

        try:
            tag = self.request.GET['tag']
            if tag == '':
                raise
            q = q.filter(models.Photo.tags == tag)
        except:
            tag = None
        
        photos = q.fetch(400)
        count = len(photos)
            
        
        autores = []
        for p in photos:
            if p.proprietario not in autores and p.proprietario != "":
                autores.append(p.proprietario)
        if autor and autor not in autores:
            autores.append(autor)
        autores.sort()
            
        params = {
            'debug': count,
            'photos': photos,
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
            all_tags.extend(p.tags)
        

        tags = defaultdict(int)
        for t in all_tags:
            tags[t] += 1
        
        tags = sorted(tags.iteritems(), key=itemgetter(1), reverse=True)
        
        params = {
            'debug': '',
            'tags': tags
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