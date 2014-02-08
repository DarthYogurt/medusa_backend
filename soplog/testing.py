'''
Created on Feb 2, 2014

@author: cyrano821
'''
from email.mime.text import MIMEText
import smtplib

#from soplog.models import *

def emailUser(logBoolNotify):
    # Open a plain text file for reading.  For this example, assume that
    # the text file contains only ASCII characters.
    
    user = logBoolNotify.user
    server = 'admin@darthyogurt.com'
    #fp = open(textfile, 'rb')
    # Create a text/plain message
    msg = MIMEText(logBoolNotify.logBool.addText)
    #fp.close()
    
    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = 'Notification for: ' + logBoolNotify.logBool.step.name
    msg['From'] = server
    msg['To'] = user.email
    
    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP('localhost')
    s.sendmail(server, [user.email], msg.as_string())
    s.quit()
    
    return "email complete"

def testEmail():
    # Open a plain text file for reading.  For this example, assume that
    # the text file contains only ASCII characters.
    
    to = 'raytochina@gmail.com'
    server = 'admin@darthyogurt.com'
    #fp = open(textfile, 'rb')
    # Create a text/plain message
    msg = MIMEText("Testing text")
    #fp.close()
    
    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = 'Notification for: ' 
    msg['From'] = server
    msg['To'] = to
    
    
    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP('localhost')
    s.sendmail(server, [to], msg.as_string())
    s.quit()
    
    return "email complete"


#a = LogBoolNotify.objects.get(id=1)
#print testEmail()
# 
# import views
# from models import *
# 
# LogBoolNotify.objects.all()


#views.emailUser()
