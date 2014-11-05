# -*- coding: utf-8 -*-
from google.appengine.ext import ndb

class Photo(ndb.Model):
    
    filename =  ndb.StringProperty()
    proprietario = ndb.StringProperty()
    legenda = ndb.StringProperty()
    tags = ndb.StringProperty(repeated=True)
    processo = ndb.StringProperty()
    decada = ndb.IntegerProperty()
    data_vaga = ndb.StringProperty()
    data_precisa = ndb.DateProperty()
    local = ndb.StringProperty()
    flickr_title = ndb.StringProperty()
    flickr_id = ndb.StringProperty()
    flickr_owner = ndb.StringProperty()
    flickr_secret = ndb.StringProperty()
    flickr_server = ndb.StringProperty()
    flickr_farm = ndb.StringProperty()
    flickr_originalsecret = ndb.StringProperty()
