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
        photos = models.Photo.query().fetch(400)
        params = {
            'debug': '',
            'photos': photos,
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