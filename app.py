from flask import Flask, request, send_from_directory
import requests
import json
app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/score', methods=["GET","POST"])
def score():
    if not request.form:
        metadata = ""
    else:
        metadata = list(request.form.keys())[0]

    r = requests.post("http://corpus.kdc.capitalone.com/score", data=metadata)
    output = json.loads(r.text)
    return output["percentile"]


if __name__ == '__main__':
    app.run(port=8000, debug=True)