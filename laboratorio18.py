nombre = input("Ingrese nombre: ")
edad = int(input("Ingrese edad: "))
altura = float(input("Ingrese altura en metros: "))
es_estudiante = input("¿Eres estudiante? (True/False): ").strip().lower() == "true"

print("\n-- Variables Capturadas --")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Altura: {altura} m")
print(f"Es estudiante: {es_estudiante}")

numero1 = int(input("\nIngrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

print("\n-- Operaciones Matemáticas --")
print(f"Suma: {numero1 + numero2}")
print(f"Resta: {numero1 - numero2}")
print(f"Multiplicación: {numero1 * numero2}")
print(f"División: {numero1 / numero2 if numero2 != 0 else 'Indefinido (división por cero)'}")

frase1 = input("\nIngrese la frase 1: ")
frase2 = input("Ingrese la frase 2: ")

frase_completa = frase1 + " " + frase2
print("\n-- Manipulación de Cadenas --")
print(f"Frase concatenada: {frase_completa}")

print(f"Frase usando f-strings: {frase1} {frase2}")

lista = [42, "texto", 3.14, True, None, "Python", -7, "cadena", 0.5, False]

print("\n-- Listas --")
print(f"Lista original: {lista}")
lista[1] = "modificado"
print(f"Lista después de modificar el segundo elemento: {lista}")

lista.append("nuevo_elemento")
print(f"Lista después de agregar un nuevo elemento: {lista}")

lista.pop(3)  
print(f"Lista después de eliminar el cuarto elemento: {lista}")

persona = {
    "nombre": "Carlos",
    "edad": 28,
    "ciudad": "Bogotá",
    "profesión": "Ingeniero"
}

print("\n-- Diccionario --")
print(f"Diccionario original: {persona}")
persona["edad"] = 32
print(f"Diccionario después de modificar la edad: {persona}")

persona["hobby"] = "Leer"
print(f"Diccionario después de agregar un nuevo par clave-valor: {persona}")