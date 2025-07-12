'''
Crea un programa que pida dos numeros y obtenga como resultado 
cual de ellos es par, o si ambos los son.
#si ambos son pares, mostrar el mensaje "Ambos numeros son pares"
#si uno de ellos es par y el otro impar , mostrar el mensaje "Uno es par y otro impar"
'''
# Pedir dos números al usuario
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

# Verificar si ambos son pares
if numero1 % 2 == 0 and numero2 % 2 == 0:
    print("Ambos números son pares")

# Verificar si uno es par y el otro impar
elif (numero1 % 2 == 0 and numero2 % 2 != 0) or (numero1 % 2 != 0 and numero2 % 2 == 0):
    print("Uno es par y otro impar")

# Si ninguno es par
else:
    print("Ambos números son impares")
