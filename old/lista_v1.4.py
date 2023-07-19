"""
    @Autor: Bruno Rodrigues Moreira
    @Date: 24/11/2022
    Script para limpar a lista dos desenhos
    Utiliza o Pyperclip para extrair o conteúdo da área de transferência do windows
    Script é chamado por uma função LISP dentro do CAD
        (command "sh" <caminho do script>)
"""
import pyperclip

lista_cad = pyperclip.paste().split('\n')
#print(lista_cad)

def CadToTxt(lista_cad):

    lista_itens = []

    for linha in lista_cad:
        linha_atual = lista_cad.index(linha) # Posição do item

        if linha != '':
            #while 
            pass
    return lista_itens

def excluir_item(item):
    lista_excluidos = ['PARAF', 'A. LISA'
    , 'PORCA', 'CONTRAPINO', 'TELA ONDULADA'
    , 'T PERFIL', 'A. PRESSÃO', 'CHUMB.EXP.'
    , 'CABO DE AÇO', 'A. CONICA', 'DEGRAU'
    , 'CONTRAPORCA', 'TUBO OD', 'CURVA OD'
    , 'REBITE', 'TELA ALAMBRADO', 'TELHA AÇO ONDULADA'
    , 'VEDAÇÃO ELASTICA', 'GRAMPO PESADO P/ CABO'
    , 'CUMEIRA']

    #for linha in lista_cad:
    #    
    #    pass

    for lista in lista_excluidos:
        #item[0:4] == 'PESO'
        if item[13:(13+len(lista))] in lista or 'PESO' in item or item.strip() == '':
            return True

    if item[4:7].strip() == '' and item[0:1].strip() != '':
        return True

    return False

def monta_lista(nova_lista):

    lista_formatada = []

    
    # VERIFICAÇÃO DE CONTINUAÇÃO
    for item in nova_lista:
        # verifica se a proxima linha é continuação
        indice_atual = nova_lista.index(item)
        cont_descricao = ''
        
        if indice_atual < (len(nova_lista) - 1):
            prox_indice = indice_atual + 1
            prox_item = nova_lista[prox_indice]

            if prox_item[0:13].strip() == '' and prox_item[13:50].strip() != '':
                cont_descricao = prox_item.strip()

        if item[0:13].strip() == '' and item[13:50].strip() != '':
            continue
        # Fim do teste de continuação da linha

        pos = item[5:8].strip()
        quantidade = item[9:12].strip()
        descricao = item[13:54].strip()
        material = item[54:66].strip()
        novo_item = f'POS.{pos:<3} {quantidade:<2} {descricao}{cont_descricao}  {material}'

        lista_formatada.append(novo_item)

    return lista_formatada
        
def Limpa_lista(lista_cad):
    
    nova_lista = []
    lista_formatada = []
    
    # Verifica linha a linha, para saber se é util na lista
    for item in lista_cad:
        if excluir_item(item):
            continue        
        nova_lista.append(item)

    lista_formatada = monta_lista(nova_lista)

    # Algoritmo para copiar para o clipboard
    texto = ''
    for pos in lista_formatada:
        texto = f'{texto}{pos}\n'

    pyperclip.copy(texto)

    return texto

Limpa_lista(lista_cad)


