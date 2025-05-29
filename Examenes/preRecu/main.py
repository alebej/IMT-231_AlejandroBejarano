from funciones import divisores, triangulo_letras, primos, fibonacci_inverso

while True:
    print("\n----- MENÚ DE FUNCIONES -----")
    print("1. Suma de divisores propios")
    print("2. Triángulo de letras")
    print("3. N números primos")
    print("4. Fibonacci inversa")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        n = int(input("Ingrese un número: "))
        resultado = divisores(n)
        print("Suma de divisores propios:", resultado)
    elif opcion == "2":
        n = int(input("Ingrese la altura del triángulo: "))
        triangulo_letras(n)
    elif opcion == "3":
        n = int(input("Ingrese cuántos primos mostrar: "))
        primos(n)
    elif opcion == "4":
        n = int(input("Ingrese cuántos términos mostrar: "))
        fibonacci_inverso(n)
    elif opcion == "5":
        print("Gracias por usar el programa.")
        break
    else:
        print("Opción inválida.")
