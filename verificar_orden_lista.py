#22. Verificar si una lista está ordenada
# Versión sin bucle while
valores = input("\nIngrese los elementos para la lista separados por espacios, por favor: ").strip().lower()

if not valores:
    print("\nInvalido. La entrada de los elementos no puede estar vacía.")
    exit()

# try:
lista = [n for n in valores.split()]
# except ValueError:
#     print("\nError. El elemento ingresado para la lista es invalido.")
#     lista = []
#     exit()

print(f"\nLista ingresada: {lista}")

orden = True
for valor in range(len(lista) - 1):
    if lista[valor] >= lista[valor+1]:
        orden = False

print(f"\nLa lista ingresada esta ordenada: {orden}")
#Versión con bucle while
#Función para que el programa pueda continuar por si el usuario lo desea
def continuar_programa():
    continuar = input("\n¿Desea continuar con el programa?, (s/n): ").strip().lower()
    if continuar in ("s", "si"):
        return True
    else:
        print("\nEl programa a finalizado...")
        return False

while True:
    valores_lista = input("\nIngrese los elementos para la lista, por favor: ").strip().lower()

    #Validación para que la entrada no este vacía
    if not valores_lista:
        print("\nInvalido. La entrada de los elementos no puede estar vacía.")
        continue

    lista = [n for n in valores_lista.split()]

    #Verificación por si la lista esta vacía
    if not lista:
        print("\nInvalido. Lista vacía.")
        continue

    print(f"\nLista ingresada: {lista}")

    #Verificador que ayuda a revisar si la lista esta ordenada o no con True o False
    orden = True
    for valor in range(len(lista) - 1):
        if lista[valor] >= lista[valor+1]:
            orden = False

    print(f"\nLa lista ingresada esta ordenada: {orden}")

    if not continuar_programa():
        break