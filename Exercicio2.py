def gera_fibonacci(aux):
    a0 = 0
    a1 = 1

    while a0 <= aux:
        if aux == a0 or aux == a1:
            return f"Número {aux} presente na sequência de Fibonacci."
        a0, a1 = a1, a0 + a1

        print(f"{a0}")

    return f"Número {aux} não está presente na sequência de Fibonacci."

aux = int(input("Informe um número máximo para a sequência de Fibonacci: "))
resultado = gera_fibonacci(aux)

print(resultado)