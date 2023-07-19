import pyperclip

# @Autor: Bruno Rodrigues Moreira
# @Date: 24/11/2022
# Script para limpar a lista dos desenhos
# Utiliza o Pyperclip para extrair o conteúdo da área de transferência do windows
# Script é chamado por uma funçao LISP dentro do CAD
#    (command "sh" <caminho do script>)


def limpa_lista():
    lista_original = pyperclip.paste().split("\n")
    nova_lista = []
    lista_formatada = []

    # Regras para pular item, digitar apenas os 5 primeiros caracteres
    # regras = ['PARAF','PORCA','A. LI','T PER','CONTR']
    # Verifica linha a linha, para saber se é util na lista
    for item in lista_original:
        if item.strip() == "":
            continue

        if item.strip()[0:4] == "PESO":
            continue

        if item.strip()[1:11].strip() == "":
            continue
        # for regra in regras:
        #   if item[13:18] == regra:
        #   break

        if (
            item[13:18] == "PARAF"
            or item[13:18] == "PORCA"
            or item[13:18] == "A. LI"
            or item[13:18] == "T PER"
            or item[13:18] == "CONTR"
        ):
            continue

        nova_lista.append(item)

    for item in nova_lista:
        # verifica se a proxima linha é continuaçao
        indice_atual = nova_lista.index(item)
        cont_descricao = ""

        if indice_atual < (len(nova_lista) - 1):
            prox_indice = indice_atual + 1
            prox_item = nova_lista[prox_indice]

            if prox_item[0:13].strip() == "" and prox_item[13:50].strip() != "":
                cont_descricao = prox_item.strip()

        if item[0:13].strip() == "" and item[13:50].strip() != "":
            continue
        # Fim do teste de continuaçao da linha

        if item[13:21] == "TELA OND" and prox_item != "":
            continue

        pos = item[5:7] + "  "
        quantidade = item[9:12] + " "
        descricao = item[13:54].strip()
        material = "  " + item[54:66].strip()
        novo_item = "POS." + "".join(
            [pos, quantidade, descricao, cont_descricao, material]
        )

        lista_formatada.append(novo_item)
    # for item in lista_formatada:
    #    print(item)
    # Algoritmo para copiar para o clipboard
    texto = ""
    for pos in lista_formatada:
        texto = texto + "\n" + pos

    pyperclip.copy(texto)

    return True


limpa_lista()
