from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for


webRe = Flask(__name__)


@webRe.route('/')
def index():
    return render_template('form.html')


@webRe.route('/registered', methods=['POST', 'GET'])
def Registration():
    fullname = request.form.get('fullname')
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    return render_template('success.html', fullname=fullname, email=email, username=username, password=password, datetime=datetime.now())



if __name__ == '__main__':    
    webRe.run(debug=True)