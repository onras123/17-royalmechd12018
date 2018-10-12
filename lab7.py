
"""The first step is to create an SMTP object, each object is used for connection 
with one server."""

import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
#Next, log in to the server
server.login("surironcmr@gmail.com", "sureshsuri7")

#Send the mail
msg = "hello"
 # The /n separates the message from the headers"
server.sendmail("surironcmr@gmail.com", "sureshsuri0154@gmail.com", msg)


#Next, log in to the server
server.quit()