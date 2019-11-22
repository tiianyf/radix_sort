LINHAS = 0


def algoritmo_de_contagem(vetor, casa_decimal):
    tamanho = len(vetor)
    resultado = [0] * tamanho
    ocorrencias = [0] * 10

    global LINHAS
    LINHAS += 4

    # contando ocorrências para cada fileira de dígitos
    for i in range(tamanho):
        indice = vetor[i]//casa_decimal
        ocorrencias[indice % 10] += 1
        LINHAS += 2

    LINHAS += 1

    # contando/armazenando ocorrencias menores ou iguais
    for i in range(1, 10):
        ocorrencias[i] += ocorrencias[i-1]
        LINHAS += 1

    i = tamanho-1
    LINHAS += 2
    while i >= 0:
        indice = vetor[i]//casa_decimal
        resultado[ocorrencias[indice % 10]-1] = vetor[i]
        ocorrencias[indice % 10] -= 1
        i -= 1
        LINHAS += 4

    i = 0
    LINHAS += 2
    for i in range(len(vetor)):
        vetor[i] = resultado[i]
        LINHAS += 1


def radix_sort(vetor):
    maior_valor = max(vetor)
    casa_decimal = 1

    global LINHAS
    LINHAS += 3

    while maior_valor//casa_decimal > 0:
        algoritmo_de_contagem(vetor, casa_decimal)
        casa_decimal *= 10

        LINHAS += 2


if __name__ == "__main__":

    # receber vetor via arquivo txt

    vetor = [1, 99, 456, 8523, 74185, 5, 2525, 654321, 10]
    radix_sort(vetor)
    LINHAS += 1
    print("Número de linhas executadas: ", LINHAS)


