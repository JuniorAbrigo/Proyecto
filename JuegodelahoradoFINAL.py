print("Bienvenido al juego del ahorcado!")
print("Vamos a empezar!")   
print("¡Buena suerte!")
import random

# Lista de palabras almacenadas el juego 
palabras = ["descubrir", "explorar", "aventura", "misterio" , "descubrimiento", "progreso"]

# Seleccionamos una palabra al azar de la lista
palabra_secreta = random.choice(palabras)
longitud = len(palabra_secreta)

# inicio del juego
palabra_mostrada = ["_"] * longitud  # Representación oculta de la palabra
letras_adivinadas = ""  # Almacena las letras que el usuario ya intentó
errores = 0  # Contador de errores
max_errores = 6  # Número máximo de intentos antes de perder

print("¡Bienvenido al juego del ahorcado!")

# Bucle principal del juego, se ejecuta hasta que se acaben los intentos o se adivine la palabra
while errores < max_errores and "_" in palabra_mostrada:
    print("Estoy pensando en una Palabra: ", " ".join(palabra_mostrada))  # Muestra el estado actual de la palabra
    letra = input("Adivina una letra: ").lower()  # Solicita una letra y la convierte a minúscula
    
    if letra in letras_adivinadas:  # Verifica si la letra ya fue ingresada
        print("Ya intentaste con esa letra.")
        continue  # Salta al siguiente ciclo sin procesar la letra nuevamente
    
    letras_adivinadas += letra  # Agrega la letra a la lista de intentos
    
    if letra in palabra_secreta:  # Si la letra está en la palabra secreta
        for i in range(longitud):  # Recorre la palabra para revelar las coincidencias
            if palabra_secreta[i] == letra:
                palabra_mostrada[i] = letra
        print("¡Bien hecho!")
    else:  # Si la letra no está en la palabra secreta
        errores += 1  # Aumenta el contador de errores
        print(f"Incorrecto. Intentos restantes: {max_errores - errores}")

# Verifica si el jugador ganó o perdió
if "_" not in palabra_mostrada:
    print("¡Felicidades! Adivinaste la palabra:", "".join(palabra_mostrada))  # Mensaje de victoria
else:
    print("¡Has perdido! La palabra era:", palabra_secreta)  # Mensaje de intentos agotados y muestra la palabra secreta