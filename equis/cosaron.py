def corazon_con_nombre(nombre):
    nombre = nombre.strip()
    if not nombre:
        print("Por favor, escribe un nombre válido.")
        return

    letras = list(nombre.upper())
    largo = len(letras)
    i = 0  # índice de la letra actual

    patron = [
        "  ***     ***  ",
        " *****   ***** ",
        "******* *******",
        "***************",
        " ************* ",
        "  ***********  ",
        "   *********   ",
        "    *******    ",
        "     *****     ",
        "      ***      ",
        "       *       "
    ]

    print("\n💖 Tu corazón personalizado 💖\n")
    for fila in patron:
        linea = ""
        for c in fila:
            if c == "*":
                linea += letras[i % largo]
                i += 1
            else:
                linea += " "
        print(linea)

# Programa principal
if __name__ == "__main__":
    nombre = input("Escribe el nombre de tu persona especial: 💌 ")
    corazon_con_nombre(nombre)
