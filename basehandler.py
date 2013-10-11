# -*- coding: utf-8 -*-
import webapp2
from webapp2_extras import jinja2
from webapp2_extras import sessions


class BaseHandler(webapp2.RequestHandler):
    """
        BaseHandler for all requests

        Holds the auth and session properties so they
        are reachable for all requests
    """

    def dispatch(self):
        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

            
    @webapp2.cached_property
    def session_store(self):
        return sessions.get_store(request=self.request)

        
    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()

        
    @webapp2.cached_property
    def messages(self):
        return self.session.get_flashes(key='_messages')

        
    def add_message(self, message, level=None):
        self.session.add_flash(message, level, key='_messages')

    
    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)
 
 
    def render_template(self, filename, **kwargs):
        kwargs.update({
            'current_url': self.request.url,
            'path': self.request.path,
            })
        if self.messages:
            kwargs['messages'] = self.messages[0][0]
            kwargs['level'] = self.messages[0][1]
        self.response.headers.add_header('X-UA-Compatible', 'IE=Edge,chrome=1')
        self.response.write(self.jinja2.render_template(filename, **kwargs))