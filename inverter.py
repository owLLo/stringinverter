def inverte_string(s):
    #converte a string para uma lista de caracteres
    lista_caracteres = list(s)

    #inverte a ordem dos caracteres na lista
    for i in range(len(lista_caracteres)//2):
        temp = lista_caracteres[i]
        lista_caracteres[i] = lista_caracteres[len(lista_caracteres)-1-i]
        lista_caracteres[len(lista_caracteres)-1-i] = temp

    #converte a lista de volta para uma string
    string_invertida = ''.join(lista_caracteres)

    return string_invertida

#exemplo de uso
entrada_usuario = input("Digite uma string: ")
resultado = inverte_string(entrada_usuario)

print("String original:", entrada_usuario)
print("String invertida:", resultado)
