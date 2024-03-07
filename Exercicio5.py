def inverte_string(minha_string):
    string_invertida = ""

    for i in range(len(minha_string)):
        string_invertida += minha_string[len(minha_string) - 1 - i]

    return string_invertida


minha_string = input("Informe uma string para inverter: ")
resultado = inverte_string(minha_string)
print("String original:", minha_string)
print("String invertida:", resultado)
