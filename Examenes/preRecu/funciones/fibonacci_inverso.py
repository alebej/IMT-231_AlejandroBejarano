def fibonacci_inverso(n):
    a = 0
    b = 1
    lista = []

    for i in range(n):
        lista.append(a)
        temp = a
        a = b
        b = temp + b

    lista.reverse()

    for num in lista:
        print(num)
