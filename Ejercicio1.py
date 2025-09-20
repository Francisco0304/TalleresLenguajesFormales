def verificar_afn(cadena):
    # Conjunto de estados posibles
    estados = {0}  # q0 = inicio
    contiene_digito = False  # Para saber si hay al menos un dígito

    for char in cadena:
        nuevos_estados = set()
        for estado in estados:
            if estado == 0:  # q0: primer carácter
                if char.isupper():  # Letra mayúscula
                    nuevos_estados.add(1)  # Ir a q1
            elif estado == 1:  # q1: parte intermedia
                if char.islower():  # Letra minúscula
                    nuevos_estados.add(1)
                elif char.isdigit():  # Dígito
                    nuevos_estados.add(1)
                    contiene_digito = True
        if not nuevos_estados:
            return False, "La contraseña no cumple el formato (primer carácter o parte intermedia inválida)."
        estados = nuevos_estados

    # La contraseña es aceptada si termina en q1 y contiene al menos un dígito
    if 1 in estados and contiene_digito:
        return True, "Contraseña válida."
    else:
        return False, "La contraseña debe contener al menos un dígito."


# Entrada por teclado
while True:
    cadena = input("Introduce una contraseña: ")
    es_valida, mensaje = verificar_afn(cadena)

    if es_valida:
        print(f"La contraseña '{cadena}' es aceptada.")
    else:
        print(f"La contraseña '{cadena}' no es aceptada. {mensaje}")

    continuar = input("¿Quieres verificar otra contraseña? (s/n): ").strip().lower()
    if continuar != 's':
        break