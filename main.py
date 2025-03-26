# Lista para almacenar la información de las personas
personas = []

# Pedir la cantidad de personas a registrar
cantidad = int(input("¿Cuántas personas deseas registrar? "))

# Capturar los datos de cada persona
for _ in range(cantidad):
    nombre = input("Ingrese el nombre de la persona: ")
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    nota = float(input(f"Ingrese la nota de {nombre}: "))

    # Agregar los datos a la lista
    personas.append([nombre, edad, nota])

# Mostrar la lista tal como fue ingresada
print("\nDatos ingresados:")
for persona in personas:
    print(persona)

# Ordenar por nota de mayor a menor sin usar lambda
def obtener_nota (persona):
    return persona[2]  # Retorna la nota (tercer elemento de la lista)

# Usar la función `obtener_nota` para ordenar
personas.sort(key=obtener_nota, reverse=True)

# Mostrar la lista ordenada
print("\nDatos ordenados por nota (de mayor a menor):")
for persona in personas:
    print(persona)
