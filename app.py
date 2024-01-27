import os

from markupsafe import escape
from flask import (
    Flask,
    render_template,
    url_for,
    request,
    session,
    redirect
)

from whois.query import Whois
import config


app = Flask(__name__)
app.secret_key = os.getenv('API_KEY')

@app.route('/lookup', methods=['POST'])
def whois_lookup():
    dname = request.form.get('dname')

    session['errors'] = ''
    session['whoisInfo'] = ''

    if not dname:
        return redirect(url_for('index'), code=302)
    
    whois = Whois(dname)

    try:
        data = whois.request()
    except Exception:
        data = ''

    if not data:
        session['errors'] = config.WRONG_DATA
    else:
        session['whoisInfo'] = data

    return redirect(url_for('index'), code=302)

@app.route('/', methods=['GET'])
def index():
    static = url_for('static', filename='style.css')
    js_script = url_for('static', filename='main.js')

    data = {
        'static': static,
        'script': js_script,
        'result': session
    }

    return render_template('index.html', **data)

if __name__ == '__main__':
    app.run(debug=True)