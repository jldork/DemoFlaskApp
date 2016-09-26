from flask import Flask, request, send_from_directory
import requests
app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/score')
def score():
    metadata = request.args['metadata']
    r = requests.post("http://corpus.kdc.capitalone.com/score", data=metadata)
    return r.text


if __name__ == '__main__': 
    app.run(port=8000, debug=True)