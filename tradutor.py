def isnumber(value):
    try:
         float(value)
    except ValueError:
         return False
    return True

def tratar_string(valor):
    array = valor.split()
    return array

def verificar(textos):
    tokens = []
    cont_linha = 1

    for linha in textos:
        cont_palavras = 1
        new_linha = tratar_string(linha)

        for palavras in new_linha:

            number = isnumber(palavras)

            if number == True:
                tokens.append(str(f"number_{cont_linha}_{cont_palavras}_{palavras}"))

            elif palavras == "input":
                tokens.append(str(f"input_{cont_linha}_{cont_palavras}_{palavras}"))

            elif palavras == "output":
                tokens.append(str(f"output_{cont_linha}_{cont_palavras}_{palavras}"))

            else:
                tokens.append(str(f"variaveis:{cont_linha}_{cont_palavras}_{palavras}"))

            cont_palavras += 1

        cont_linha += 1
    return tokens

def leitor(caminho):
    vet_arquivo = []
    with open(f"{caminho}") as file:
        for i in file:
           vet_arquivo.append(str.strip(i))
    return vet_arquivo


def orquestrador():
    arquivo = leitor(input("caminho do arquivo: "))
    tokens = verificar(arquivo)
    print('')
    print("arquivo:")
    for i in arquivo:
        print(i)
    print('')
    print("tokens:")
    for i in tokens:
        print(i)
    print('')

if __name__ == '__main__':
    orquestrador()

