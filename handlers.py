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
            proprietario = self.request.GET['proprietario']
            if proprietario == '':
                raise
            q = q.filter(models.Photo.proprietario == proprietario)
        except:
            proprietario = None
        
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

        except:
            logging.error("exception raised:")
            tag = None
        else:
            tag_list = tag.split(",")
            q = q.filter(models.Photo.tags.IN(tag_list))
            logging.error("filterd on tag")
        
        photos = q.fetch(400)
        count = len(photos)
            
        
        proprietarios = []
        decadas = []
        all_tags = []
        
        for p in photos:
            if p.proprietario not in proprietarios and p.proprietario != '':
                proprietarios.append(p.proprietario)
            
            if p.decada not in decadas and p.decada is not None:
                decadas.append(p.decada)
            
            all_tags.extend(p.tags)
                
        if proprietario is not None and proprietario not in proprietarios:
            proprietarios.append(proprietario)
        proprietarios.sort()
        
        if decada is not None and decada not in decadas:
            decadas.append(decada)
        decadas.sort()
        
        tags = defaultdict(int)
        for t in all_tags:
            tags[t] += 1
        
        tags = sorted(tags.iteritems(), key=itemgetter(1), reverse=True)
        
        params = {
            'debug': count,
            'photos': photos,
            'proprietarios': proprietarios or '',   
            'decadas': decadas or '',
            'tags': tags or '',
            'proprietario': proprietario or '',
            'decada': decada or '',
            'tag': tag,
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
        
        
        try:
            proprietario = self.request.GET['proprietario']
        except:
            proprietario = ''
        
        try:
            decada = int(self.request.GET['decada'])
        except:
            decada = ''
        
        
        params = {
            'debug': '',
            'tags': tags,
            'proprietario': proprietario,
            'decada': decada,
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