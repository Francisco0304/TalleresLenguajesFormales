def verificar_email_afd(correo):
    estado = 0
    i = 0
    n = len(correo)

    while i < n:
        char = correo[i]
        if estado == 0:
            # Primer carácter: letra minúscula
            if char.islower():
                estado = 1
            else:
                return False, "El correo debe comenzar con una letra minúscula."
        elif estado == 1:
            # Parte local: letras minúsculas o dígitos
            if char.islower() or char.isdigit():
                estado = 1
            elif char == '@':
                estado = 2
            else:
                return False, "La parte local solo puede tener letras minúsculas o dígitos."
        elif estado == 2:
            # Verificar que el resto sea exactamente 'uptc.edu.co'
            if correo[i:] == 'uptc.edu.co':
                estado = 3  # Estado de aceptación
                i = n - 1  # Saltar al final
            else:
                return False, "El dominio debe ser exactamente '@uptc.edu.co'."
        i += 1

    if estado == 3:
        return True, "Correo válido."
    else:
        return False, "El correo no terminó en estado de aceptación."


# Entrada por teclado
while True:
    correo = input("Introduce un correo electrónico: ")
    valido, mensaje = verificar_email_afd(correo)
    if valido:
        print(f"La cadena '{correo}' es aceptada.")
    else:
        print(f"La cadena '{correo}' no es aceptada. {mensaje}")
    
    continuar = input("¿Quieres verificar otro correo? (s/n): ").strip().lower()
    if continuar != 's':
        break
