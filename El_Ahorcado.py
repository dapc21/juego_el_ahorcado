from random import choice


# Lista de palabras posibles
palabras = ["manzana", "elefante", "murcielago", "programa", "futbol", "avion"]

# Selección aleatoria
palabra_secreta = choice(palabras)

def mostrar_palabra(palabra, letras_adivinadas):
    resultado = []  # Lista para construir la palabra visible

    for letra in palabra:
        if letra in letras_adivinadas:
            resultado.append(letra)  # Si fue adivinada, se muestra la letra
        else:
            resultado.append("_")    # Si no, se muestra un guion bajo

    return " ".join(resultado)  # Se unen los elementos separados por espacios


def letra_valida(letra, letras_usadas):
    # Aca validamos que se ha ingresado un solo caracter o sea una letra, que sea letra y que de paso no esté en las letras que ya se han ingresado
    return len(letra) == 1 and letra.isalpha() and letra not in letras_usadas

def palabra_completa(palabra, letras_adivinadas):
    # Esta función devuelve True si TODAS las letras de la palabra
    # han sido adivinadas (es decir, si cada letra de la palabra
    # se encuentra en el conjunto letras_adivinadas).
    #
    # Utiliza la función all(), que devuelve True solo si
    # TODAS las condiciones del generador son verdaderas.
    #
    # En este caso, la condición es que cada letra de la palabra
    # esté dentro del conjunto de letras que ya fueron adivinadas.
    #
    # Ejemplo:
    # palabra = "hola"
    # letras_adivinadas = {'h', 'o', 'l', 'a'}
    # → retorna True
    # Si letras_adivinadas = {'h', 'o'} → retorna False
    return all(letra in letras_adivinadas for letra in palabra)


vidas = 6
letras_usadas = set()
letras_adivinadas = set()

print("¡Bienvenido al juego del Ahorcado!")
print(f"La palabra tiene {len(palabra_secreta)} letras.")
print(mostrar_palabra(palabra_secreta, letras_adivinadas))

while vidas > 0 and not palabra_completa(palabra_secreta, letras_adivinadas):
    letra = input("Elige una letra: ").lower()

    if not letra_valida(letra, letras_usadas):
        print("Entrada inválida o ya usada. Intenta con otra letra.")
        continue

    letras_usadas.add(letra)

    if letra in palabra_secreta:
        letras_adivinadas.add(letra)
        print("¡Bien! Letra encontrada.")
    else:
        vidas -= 1
        print(f"Letra incorrecta. Te quedan {vidas} vidas.")

    print(mostrar_palabra(palabra_secreta, letras_adivinadas))
    print("Letras usadas:", ", ".join(sorted(letras_usadas)))
    print("-" * 40)

# Resultado final (ganaste o perdiste, pero el juego termina)
if palabra_completa(palabra_secreta, letras_adivinadas):
    print("¡Felicidades! Has adivinado la palabra:", palabra_secreta)
else:
    print("¡Perdiste! La palabra era:", palabra_secreta)
