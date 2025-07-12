#-*- coding :utf-8 -*-
#carateres especiales

from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route ('/',methods=['GET'] )
def unida():
    return 'Hola desde la Unida'

if __name__ == '__main__':
    app.run(debug=True,port=5000, host='0.0.0.0')
    '''
    El 0.0.0.0  es un comodin que permite que la aplicacion sea accesible desde cualquier direccion IP de la red local.
    '''