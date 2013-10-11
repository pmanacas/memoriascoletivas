# -*- coding: utf-8 -*-
import webapp2

webapp2_config = {}

webapp2_config['webapp2_extras.sessions'] = {
    'secret_key': 'v5mwS2pHkYnMaTeK4Re954Uz',
    }

webapp2_config['webapp2_extras.jinja2'] = {
    'template_path': 'templates',
    'globals': {
        'uri_for': webapp2.uri_for,
    },
}