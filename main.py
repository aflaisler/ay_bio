from flask import Flask, render_template
import numpy as np
import pandas as pd


app = Flask(__name__)


# For render_template pass in name of template and any variables needed
@app.route('/')
def index():
    return render_template('index.html')


def rand_nb():
    x = np.random.randint(100, 1000)
    y = np.random.randint(10, 100)
    z = sum([int(i) for i in str(x * y)])
    return x, y, z


@app.route('/swim')
def swim():
    return render_template('swim.html') + str([rand_nb() for i in range(5)])


if __name__ == '__main__':
    # cert = '/etc/letsencrypt/live/aymeric.bio/cert.pem'
    # key = '/etc/letsencrypt/live/aymeric.bio/privkey.pem'
    # context = (cert, key)
    # app.run(host='0.0.0.0', port=443, ssl_context=context,
    #         threaded=True, debug=True)
    app.run(host='0.0.0.0', debug=True)
