from  flask import Flask, jsonify, request
from cliente import verificar_cliente

app= Flask(__name__)
@app.route('/cliente', methods=['POST'])
def llamaracliente():
    datos_entrada= request.json.get('user')
    if not datos_entrada or 'ci' not in datos_entrada:
        return jsonify ({"error": "Peticion invalida"}),  400
    cedula= datos_entrada  [ 'ci' ]
    if verificar_cliente (cedula):
        respuesta_exitosa = {
           "accion": "exitoso",
           "codRes": "SIN_ERROR",
           "menRes": "OK",
        }
        return jsonify(respuesta_exitosa) 
    else: 
        respuesta_incorrecta = {
            "accion": "Cliente no esta",
           "codRes": "ERROR",
           "menRes": "Error de cliente",
           "ci": "cedula",
        }
        return jsonify (respuesta_incorrecta)
    def verificar_cliente (ci):
    if ci == "5800422": 
        return {
            "accion": "exitoso",
           "codRes": "SIN_ERROR",
           "menRes": "OK",
           "ci": ci,
           "nombre": "Rosa",
           "apellidos" : "Canete"
        }
    else :
        return {
             "accion": "Cliente no esta",
           "codRes": "ERROR",
           "menRes": "Error de cliente",
           "ci": "cedula",
        }