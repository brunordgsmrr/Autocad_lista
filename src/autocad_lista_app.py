import autocad_lista_class as lista
import pyperclip

LISTA = []
OUTPUT_OBJ = []
OUTPUT_TEXT = ''

try:
    with open('./config.txt', 'r', encoding='utf-8') as file:
        itens_ignorados = file.readlines()
    #with open('utils/lista_de_exemplo.txt', 'r', encoding='utf-8') as file:
    #    conteudo = file.readlines()
    #    for i in conteudo:
    #        if i.strip() == '' or 'PESO' in i:
    #            continue
    #        LISTA.append(lista.Item(i, itens_ignorados))
    lista_cad = pyperclip.paste().split('\n')
    for i in lista_cad:
        if i.strip() == '' or 'PESO' in i:
            continue
        LISTA.append(lista.Item(i, itens_ignorados))
    for i, obj in enumerate(LISTA):
        if obj.tipo == 'Item':
            OUTPUT_OBJ.append(obj)
        if obj.tipo == 'Continuação' and LISTA[(i-1)].tipo == 'Item':
            OUTPUT_OBJ[-1].descricao = OUTPUT_OBJ[-1].descricao.strip() + ' ' + obj.descricao.strip()
    for i in OUTPUT_OBJ:
        OUTPUT_TEXT = f'{OUTPUT_TEXT}{i.get_lista()}\n'
    pyperclip.copy(OUTPUT_TEXT)

except ValueError:
    print("Falha no script")
    input()
