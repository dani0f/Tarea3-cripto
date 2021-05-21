from flask import Flask, render_template   
from base64 import b64encode
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad

app = Flask(__name__)


# routes
@app.route('/')
def Index():
    varKey='llave'   #Aqui va la llave
    varData="secret" #Aqui va el mensaje
    data=varData.encode('utf-8')
    key=varKey.encode('utf-8')
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)#Blowfish ECB recibe solo llave como parametrro
    ct_bytes = cipher.encrypt(pad(data, Blowfish.block_size))#Se encripta el mensaje con la llave
    ct = b64encode(ct_bytes).decode('utf-8')
    return render_template('index.html', hash = ct) #resultado es hash en base64


if __name__ == '__main__':
    app.run(debug=True)