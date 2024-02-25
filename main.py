from flask import Flask, render_template, request, redirect, url_for
from threading import Thread
import bot

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/run', methods=['GET', 'POST'])
def run():
    if request.method == 'POST':
        token = request.form['token']
        prefix = request.form['prefix']
        bot.PREFIX = prefix
        t = Thread(target=bot.start, kwargs={'token': token, 'PREFIX': prefix})
        t.start()
        return render_template("running.html")

if __name__ == '__main__':
    app.run(debug=True)
