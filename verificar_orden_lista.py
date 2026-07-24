#22. Verificar si una lista está ordenada
def continuar_programa():
    continuar = input("\n¿Desea continuar con el programa?, (s/n): ").strip().lower()
    if continuar in ("s", "si"):
        return True
    else:
        print("\nEl programa a finalizado...")
        return False

while True:
    valores_lista = input("\nIngrese los elementos para la lista, por favor: ").strip().lower()

    if not valores_lista:
        print("\nInvalido. La entrada de los elementos no puede estar vacia.")
        continue

    try:
        lista = [n for n in valores_lista.split()]
    except ValueError:
        print("\nError. El valor ingresado es invalido. Intentelo de nuevo.")
        lista = []
        break

    if not lista:
        continue

    print(f"\nLista ingresada: {lista}")

    orden = True
    for valor in range(len(lista) - 1):
        if lista[valor] >= lista[valor+1]:
            orden = False

    print(f"\nLa lista ingresada esta ordenada: {orden}")

    if not continuar_programa():
        break