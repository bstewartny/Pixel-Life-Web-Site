#!/usr/bin/env python

from google.appengine.dist import use_library
use_library('django', '0.96')

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util
#from google.appengine.api import mail

import os

class MainHandler(webapp.RequestHandler):
    def get(self):
        self.redirect('/pixellife/')

class PixelLifeHandler(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
       
        self.response.out.write(template.render(path, {}))
        
 
        
def main():
    application = webapp.WSGIApplication([('/',MainHandler),
                                            ('/pixellife', MainHandler),
                                            ('/pixellife/', PixelLifeHandler),
                                            ('/pixellife/index.html',PixelLifeHandler),
                                            ('/pixellife/iphone',PixelLifeHandler),
                                            ('/pixellife/iphone.html',PixelLifeHandler),
                                            ('/pixellife/iPhone',PixelLifeHandler),
                                            ('/pixellife/iPhone.html',PixelLifeHandler),
                                            ('/pixellife/ipad',PixelLifeHandler),
                                            ('/pixellife/ipad.html',PixelLifeHandler),
                                            ('/pixellife/iPad',PixelLifeHandler),
                                            ('/pixellife/iPad.html',PixelLifeHandler)],debug=True)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
