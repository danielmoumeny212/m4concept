
import threading
from django.core.mail import send_mail , EmailMessage, EmailMultiAlternatives


class EmailThread(threading.Thread):
    
    
    def __init__(self,  subject,message, sender,html_content, recipient_list:list, attachement: tuple = None):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        self.sender = sender
        self.message = message
        self.attachement = attachement
        
        threading.Thread.__init__(self)
        self.status = ""

    def run(self):
        try: 
          email = EmailMultiAlternatives(self.subject, self.message ,  self.sender, self.recipient_list)
          email.attach_alternative(self.html_content, 'text/html')
          if self.attachement is not None:
              email.attach(*self.attachement)
          email.send()
          
          self.status = 'success'
          return self.status
        except Exception as error: 
            self.status = "failed"
            return self.status 
       
       
