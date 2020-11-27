from flask import render_template, request, current_app
from . import main
import requests


@main.route('/')
def index():
    return render_template("templates/index.html")


@main.route('/link')
def get_link():

    url = request.args.get('url')

    params = {'video': True,
              'audio': True,
              'screenshot': False}

    if request.args.get('iframe'):
        params['iframe'] = True

    headers = {'x-api-key': current_app.config['MICROLINK_API_KEY']}
    m_url = 'https://pro.microlink.io?url={}'.format(url)
    r = requests.get(m_url, headers=headers, params=params)

    return r.json(), 200