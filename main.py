#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.api import mail

import os

class MainHandler(webapp.RequestHandler):
    def get(self):
        self.redirect('/pixellife/')

class PixelLifeHandler(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
       
        self.response.out.write(template.render(path, {}))
        
class emailHandler(webapp.RequestHandler):
    def post(self):
        email=self.request.get("email")
        
        if mail.is_email_valid(email):
            subject=self.request.get("topic")
            body=self.request.get("message")
            name=self.request.get("name")
            body=body+"\n\n"+name
            # send feedback email
            mail.send_mail(email, "feedback@omegamuse.com", subject,body)    
            # send confirmation email
            mail.send_mail("feedback@omegamuse.com",email,"Feedback received","Thank you for your feedback!  We will review your email and get back to you as soon as possible.  Cheers, OmegaMuse Team.")
            
        self.redirect('/pixellife/')
        
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
                                            ('/email',emailHandler),
                                            ('/pixellife/email',emailHandler),
                                            ('/pixellife/iPad.html',PixelLifeHandler)],debug=True)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
