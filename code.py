def texto_para_binario(texto):
    lista_binaria = []
    for caractere in texto:
        #caractere_binario = Converte o caractere em seu valor ordinal (valor numérico na tabela ASCII)
        # e formata-o como uma representação binária de 8 bits.
        caractere_binario = format(ord(caractere), '08b')
        lista_binaria.append(caractere_binario)
    return lista_binaria

def xor_cifrar(mensagem, chave):
    mensagem_binaria = texto_para_binario(mensagem)
    chave_binaria = texto_para_binario(chave)
    chave_combinada = ''.join(chave_binaria)
    mensagem_cifrada = []
    for caractere_binario in mensagem_binaria:
        caractere_cifrado_binario = ''.join(chr(int(caractere_binario[i]) ^ int(chave_combinada[i]) + 48) for i in range(8))
        mensagem_cifrada.append(caractere_cifrado_binario)
    texto_cifrado = ''.join(chr(int(caractere_cifrado_binario, 2)) for caractere_cifrado_binario in mensagem_cifrada)
    return texto_cifrado

def transposicao(texto, rodadas):
    lista_texto = [str(char) for char in texto]

    for _ in range(rodadas):
        ultimo_caractere = lista_texto[-1]
        for i in range(len(lista_texto) - 1, 0, -1):
            lista_texto[i] = lista_texto[i - 1]
        lista_texto[0] = ultimo_caractere

    texto_cifrado = ''.join(lista_texto)
    return texto_cifrado


def transposicao_inversa(texto_cifrado, rodadas):
    lista_texto = [str(char) for char in texto_cifrado]

    for _ in range(rodadas):
        primeiro_caractere = lista_texto[0]
        for i in range(0, len(lista_texto) - 1):
            lista_texto[i] = lista_texto[i + 1]
        lista_texto[-1] = primeiro_caractere

    texto_decifrado = ''.join(lista_texto)
    return texto_decifrado


def cifrar_xor(mensagem, chave):
    rodadas = int(chave[-2:])
    cifrado = transposicao(mensagem, rodadas)
    xor_cifrado = xor_cifrar(cifrado, chave)
    return xor_cifrado

def decifrar_xor(texto_cifrado, chave):
    rodadas = int(chave[-2:])
    xor_decifrado = xor_cifrar(texto_cifrado, chave)
    decifrado = transposicao_inversa(xor_decifrado, rodadas)
    return decifrado