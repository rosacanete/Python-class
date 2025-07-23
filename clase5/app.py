#-*- coding :utf-8 -*-
#carateres especiales

from flask import Flask, jsonify, request
from login import login
app = Flask(__name__)
## Se expone el blueprint de login
app.register_blueprint(login)
@app.route ('/',methods=['GET'] )
def unida():
    return 'Server Flask is running on port 5000'

if __name__ == '__main__':
    app.run(debug=True,port=5000, host='0.0.0.0')
    '''
    El 0.0.0.0  es un comodin que permite que la aplicacion sea accesible desde cualquier direccion IP de la red local.
    '''