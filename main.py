from flask import Flask, render_template

app = Flask(__name__)


# For render_template pass in name of template and any variables needed
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    import os

    port = 8000

    # Open a web browser pointing at the app.
    os.system('open http://localhost:{0}'.format(port))

    # Set up the development server on port 8000.
    app.debug = True
    app.run(port=port)
