# Definimos la palabra secreta que el jugador debe adivinar.
palabra_secreta = "python"

# Pedimos al usuario que ingrese una letra y la convertimos a minúsculas.
letra1 = input("Ingresa una letra: ").lower()

# Verificamos si la primera letra ingresada está en la palabra secreta.
if letra1 in palabra_secreta:
    print("¡Bien hecho! La letra está en la palabra.")  # Mensaje si la letra es correcta.
elif letra1 == "":  
    print("No ingresaste ninguna letra.")  # Mensaje si el usuario no ingresó nada.
else:
    print("Letra incorrecta. Te quedan 5 intentos.")  # Mensaje si la letra es incorrecta.

# Pedimos otra letra al usuario.
letra2 = input("Ingresa otra letra: ").lower()

# Verificamos si la segunda letra ingresada está en la palabra secreta.
if letra2 in palabra_secreta:
    print("¡Bien hecho! La letra está en la palabra.")
elif letra2 == "":
    print("No ingresaste ninguna letra.")
else:
    print("Letra incorrecta. Te quedan 4 intentos.")

# Pedimos otra letra más al usuario.
letra3 = input("Ingresa otra letra: ").lower()

# Verificamos si la tercera letra ingresada está en la palabra secreta.
if letra3 in palabra_secreta:
    print("¡Bien hecho! La letra está en la palabra.")
elif letra3 == "":
    print("No ingresaste ninguna letra.")
else:
    print("Letra incorrecta. Te quedan 3 intentos.")

# Mensaje final indicando que el programa ha terminado.
print("Fin del juego.")