# Problema 1: Números divisibles por 7 y múltiplos de 5 entre 1500 y 2700
for num in range(1500, 2701):  # Recorrer el rango 1500 a 2700
    if num % 7 == 0 and num % 5 == 0:  # Verificar si es divisible por 7 y múltiplo de 5
        print(num)

# Problema 2: Patrón de pirámide
n = 5
# Patrón ascendente
for i in range(1, n + 1):
    print('* ' * i)
# Patrón descendente
for i in range(n - 1, 0, -1):
    print('* ' * i)

# Problema 3: Contar pares e impares
pares = 0
impares = 0
numeros = []

while True:
    decision = input("¿Desea ingresar un número? (SI/NO): ").strip().lower()
    if decision == "no":
        break
    num = int(input("Ingrese el número: "))
    numeros.append(num)
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Números ingresados: {numeros}")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")

# Problema 4: Ingresar estudiantes y sus calificaciones
alumnos = []
n = int(input("Ingrese el número de alumnos: "))

for i in range(n):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = int(input(f"Ingrese la nota {j+1} del alumno {nombre}: "))
        notas.append(nota)
    alumnos.append({"Alumno": nombre, "Notas": notas})

# Mostrar el listado de alumnos
for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")

# Problema 5: Suma de todos los números primos menores que 100
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

suma_primos = sum(num for num in range(100) if es_primo(num))
print(f"La suma de los números primos menores que 100 es: {suma_primos}")

# Problema 6: Serie de Fibonacci entre 0 y 50
a, b = 0, 1
while a <= 50:
    print(a, end=", ")
    a, b = b, a + b

# Problema 6: Serie de Fibonacci entre 0 y 50
a, b = 0, 1
while a <= 50:
    print(a, end=", ")
    a, b = b, a + b

# Problema 7: Encontrar números perfectos menores que 1000
def es_perfecto(num):
    suma_divisores = sum(i for i in range(1, num) if num % i == 0)
    return suma_divisores == num

for num in range(1, 1000):
    if es_perfecto(num):
        print(f"Número perfecto: {num}")

# Problema 8: Calcular el factorial de un número
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un número: "))
print(f"El factorial de {numero} es: {factorial(numero)}")

# Problema 9: Eliminar vocales de una cadena de texto
def eliminar_vocales(texto):
    vocales = "aeiouAEIOU"
    return ''.join([letra for letra in texto if letra not in vocales])

cadena = input("Ingrese una cadena de texto: ")
print(f"Texto sin vocales: {eliminar_vocales(cadena)}")

# Problema 10: Convertir fechas al formato AAAA-MM-DD
from datetime import datetime

def convertir_fecha(fecha):
    try:
        # Si el formato es MM/DD/AAAA
        fecha_obj = datetime.strptime(fecha, "%m/%d/%Y")
    except ValueError:
        # Si el formato es "Mes día, año"
        fecha_obj = datetime.strptime(fecha, "%B %d, %Y")
    return fecha_obj.strftime("%Y-%m-%d")

fecha_input = input("Ingrese una fecha (MM/DD/AAAA o 'Mes día, año'): ")
print(f"Fecha en formato AAAA-MM-DD: {convertir_fecha(fecha_input)}")

