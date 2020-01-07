from flask import Flask, request, jsonify, Response
from flask_mail import Mail, Message
import os
EMAIL_USER = os.getenv("EMAIL")
EMAIL_PW = os.getenv("PW")
app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ['EMAIL_USER'],
    "MAIL_PASSWORD": os.environ['EMAIL_PW'],
    "MAIL_MAX_EMAIL": 5,
    "MAIL_MAX_EMAILS": 'khalilsaboor1@gmail.com'
}
app.config.update(mail_settings)
mail = Mail(app)


@app.route('/', methods=['POST'])
def send_email():
    data = request.json
    try:
        msg = Message(data.message, recipients=[data.recipient])
        msg.body = data.message
        mail.send(msg)
        return jsonify(status=200, message='Mail sent!')
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run()
