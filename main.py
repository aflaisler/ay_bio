from flask import Flask, render_template


app = Flask(__name__)


# For render_template pass in name of template and any variables needed
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    cert = '/etc/letsencrypt/live/aymeric.bio/cert.pem'
    key = '/etc/letsencrypt/live/aymeric.bio/privkey.pem'
    context = (cert, key)
    app.run(host='0.0.0.0',port=443, ssl_context=context, threaded=True, debug=True)
   # app.run(host='0.0.0.0', debug=True)
