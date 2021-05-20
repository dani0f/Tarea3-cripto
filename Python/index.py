from flask import Flask, render_template   
from base64 import b64encode
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad

app = Flask(__name__)


# routes
@app.route('/')
def Index():
    data = b"secret"
    varKey='llave'
    key=varKey.encode('utf-8')
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    ct_bytes = cipher.encrypt(pad(data, Blowfish.block_size))
    ct = b64encode(ct_bytes).decode('utf-8')
    return render_template('index.html', hash = ct)


if __name__ == '__main__':
    app.run(debug=True)