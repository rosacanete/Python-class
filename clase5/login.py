from flask import Blueprint
from  flask import Flask, jsonify, request


login= Blueprint('login', __name__)

@login.route('/login', methods=['POST'])
def llamarServicioSet():
    user= request.json.get('user')
    password= request.json.get('password')
    print ( "User enviado: " ,user, "Pass enviado " , password)
    codRes,menRes, accion = inicializarVariables(user, password)
    salida = {
        'codRes': codRes,
        'menRes': menRes,
        'user': user,
        'accion': accion 
    }
    return jsonify(salida) 
def inicializarVariables(user, password):
    codRes = 'SIN_ERROR'
    menRes = "OK"
    accion = "Login exitoso"

    return codRes, menRes, accion