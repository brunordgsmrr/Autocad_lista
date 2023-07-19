import pyperclip

'''
    @Autor: Bruno Rodrigues Moreira
    @Date: 24/11/2022
    Script para limpar a lista dos desenhos
    Utiliza o Pyperclip para extrair o conteÃºdo da Ã¡rea de transferÃªncia do windows
    Script Ã© chamado por uma funÃ§Ã£o LISP dentro do CAD

    (defun c:lista()
        (command "sh" <caminho do script>)    
    )
'''

def Limpa_lista():

    # Copia da Ã¡rea de transferÃªncia
    lista_antiga = pyperclip.paste().split('\n')
    nova_lista = []
    
    for item in lista_antiga:
        if (item[5:7] == '  '):
            continue

        if (item[0:0] == 'P ' and item[13:18] != 'B. RO'):
            continue

        if (item[0:4] == 'PESO' or item[13:17] == 'PARA'):
            continue

        pos = item[5:7] + '  '
        quantidade = item[9:12] + ' '
        descricao = item[13:54].strip() + '  '
        material = item[54:66].strip()
        novo_item = 'POS.' + ''.join([pos,quantidade,descricao,material])
        nova_lista.append(novo_item)

    texto = ''
    for pos in nova_lista:
        texto = texto + '\n' + pos

    pyperclip.copy(texto)

    return True

Limpa_lista()


