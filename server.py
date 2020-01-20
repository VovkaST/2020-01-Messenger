import json
from datetime import datetime
from flask import Flask, render_template

__author__ = 'vovka.steel911@mail.ru'

app = Flask(__name__)
TITLE = 'SkillBox Python intensive'
START_TIME = datetime.now()


@app.route('/')
def hello():
    hello = 'Это мой первый опыт в web На Python.Flask'
    return render_template('template_index_body.html', title=TITLE, body=hello)


@app.route('/status')
def status():
    info = {'Admin': __author__,
            'Server time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'Server name': TITLE,
            'Server start time:': START_TIME.strftime('%Y-%m-%d %H:%M:%S'),
            'Server working': str(datetime.now() - START_TIME)}
    return render_template('template_status_body.html', title=TITLE, body=json.dumps(info, indent=4))


@app.route('/name')
def name():
    return __name__


app.run()
