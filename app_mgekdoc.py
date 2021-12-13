from flask import Flask
from flask import render_template
from docs import data_docs

app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    return render_template('index.html', docs=data_docs)


@app.route('/<string:name>.md')
def doc(name):
    return render_template('doc.html', name=name)


@app.route('/about/')
def doc_about():
    name = "about"
    return render_template('doc.html', name=name)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=10089, debug=True)
