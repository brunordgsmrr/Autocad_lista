import os
import shutil
import tkinter
import autocad_lista_class as lista
import pyperclip
from tkinter import filedialog as fd

LISTA = []
OUTPUT_OBJ = []
OUTPUT_TEXT = ''
USER = os.getenv('USERPROFILE')
PCP_PATH = f'{USER}/Documents/pcp_cad'

try:
    try:
        with open(f'{PCP_PATH}/config.txt', 'r', encoding='utf-8') as file:
            itens_ignorados = file.readlines()
    except Exception as err:
        print(f'Falha no script\n{err}')
        print('Pressione qualquer tecla para procurar o arquivo "config.txt"')
        input()
        filetypes = (('Text', '*.txt'), ('All files', '*.*'))

        root = tkinter.Tk()
        config_path = fd.askopenfilename(title='Open config file', initialdir=f'{USER}/Documents', filetypes=filetypes)
        root.destroy()
        root.mainloop()

        file_name = os.path.basename(config_path)
        try:
            os.makedirs(PCP_PATH)
        except FileExistsError:
            print('\nPasta já existe\n')

        shutil.copyfile(config_path, f'{PCP_PATH}/{file_name}')

        print(f'Arquivo selecionado: {config_path}')
        print('Pressione qualquer tecla para prosseguir...')
        input()
    finally:
        with open(f'{PCP_PATH}/config.txt', 'r', encoding='utf-8') as file:
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

except Exception as err:
    print(f'Falha no script\n{err}')
    input()
