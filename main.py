from flask import flask,jsonify,request
from cliente import verificar_cliente
app = flask (__name__)

app.register_blueprint (verificar_cliente)
@app.route('/', methods=['GET'])
def iniciar () :
    return 'Server Flask is runnig on port 500'
if __name__ == '__main__':
    app.run (debug=True,port=5000, host= '0.0.0.0')