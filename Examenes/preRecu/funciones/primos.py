def primos(n):
    contador = 0
    numero = 2
    while contador < n:
        es_primo = True
        for i in range(2, numero):
            if numero % i == 0:
                es_primo = False
                break
        if es_primo:
            print(numero)
            contador += 1
        numero += 1