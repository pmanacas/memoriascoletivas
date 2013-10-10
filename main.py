#!/usr/bin/env python

import webapp2
import config
import routes
import os

app = webapp2.WSGIApplication(
    debug = os.environ['SERVER_SOFTWARE'].startswith('Dev'),
    config=config.webapp2_config
 )
routes.add_routes(app)
