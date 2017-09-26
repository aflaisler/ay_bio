from flask import Flask, render_template
import numpy as np


app = Flask(__name__)


# For render_template pass in name of template and any variables needed
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/swim')
def swim():
    nbs = []
    for i in range(5):
        x = np.random.randint(100, 1000)
        y = np.random.randint(10, 100)
        z = sum([int(i) for i in str(x * y)])
        nbs.append([x, y, z])
    return render_template('swim.html', nbs=nbs)


if __name__ == '__main__':
    cert = '/etc/letsencrypt/live/aymeric.bio/cert.pem'
    key = '/etc/letsencrypt/live/aymeric.bio/privkey.pem'
    context = (cert, key)
    app.run(host='0.0.0.0', port=443, ssl_context=context,
            threaded=True, debug=True)
    # app.run(host='0.0.0.0', debug=True)
