from datetime import datetime
from unicodedata import name
from flask import Flask, render_template, request, url_for, redirect
import os
import smtplib


app = Flask(__name__)

host = "mail.stackxsolutions.in"
sender_email = "info@stackxsolutions.in"
email_pass = "StackX@123"

def send_email(user, pwd, recipient, subject, body):


    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body
    
    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    with smtplib.SMTP_SSL(host="mail.stackx.online") as smtp:
        smtp.login(user,pwd)
        smtp.sendmail(user,TO,message)
        smtp.quit()




@app.route('/')
def home():
    return render_template('index.html')


@app.route('/form_mail', methods=['POST'])
def form_mail():

    email = request.form['email']
    mail_type = request.form['mail_type']

    if mail_type == "query-mail":
        subject = request.form['subject'] 
        message = request.form['message']
        name = request.form['name']
        print(subject)
        print(message)
        send_email(sender_email, email_pass, email, "Thankyou for contacting us","Our representative will reach to you soon.\nTeam Stackx")
        send_email(sender_email, email_pass, 'stackxsolutions@gmail.com', "A new Query with subject {0}".format(subject),"Name: {1}\nEmail: {0}\nQuery: {2}".format(email,name,message))
        
    else:
        send_email(sender_email, email_pass, email, "ThankYou", "Thankyou For subscribing Our NewsLetter\nTeam StackX")
    return render_template('index.html')





if __name__ == '__main__':
    app.run(debug=True)

