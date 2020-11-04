import cgi
import model
import json,sys


def output(content):
    print("Recieved AJAX Call.....")
    sys.stdout.write('content-Type:text/plain\n\n')
    sys.stdout.write(content)

form = cgi.FieldStorage()

id = form.getvalue('id')

msg = model.studentIdvalidation(id)
output(msg)