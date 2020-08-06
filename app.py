import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/mirror')
def get_article():
    try:
        url = request.args.get('url').rstrip('/')
        print(url)
        # data = r.json()['payload']['value']['content']['bodyModel']['paragraphs']
        return render_template('article.html', url=url)
    except Exception as e:
        return str(e)

@app.route('/media')
def get_iframe():
    src = request.args.get('src')
    return render_template('gist.html', src=src)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT') or 5000)