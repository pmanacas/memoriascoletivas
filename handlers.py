# -*- coding: utf-8 -*-
from basehandler import BaseHandler
import logging


class HomePageHandler(BaseHandler):

    def get(self):
        params = {
            'debug': '',
        }
        return self.render_template('home.html', **params)
        
        
class ProjetoHandler(BaseHandler):

    def get(self):
        return self.render_template('projeto.html')

class HistoriaHandler(BaseHandler):

    def get(self):
        return self.render_template('historia.html')         

        
class NoJavascriptHandler(BaseHandler):

    def get(self):
        return self.render_template('sem_javascript.html')