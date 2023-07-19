import pyperclip

def clear_space(lista): # exclui linhas vazias
    cleaned_list = []
    for i in lista:
        if i.strip() == '':
            continue
        else:
            cleaned_list.append(i)
    return cleaned_list

def arrange_list(lista): # Rearranja as linhas 
    arranged_list = []

    for i in lista:
        if (lista.index(i) + 1) < len(lista):
            current_pos = 1
            next_index = lista[(lista.index(i) + current_pos)]
            print(next_index)

            while next_index[0:13].strip() == '' and next_index[13:50].strip() != '':
                print('continuação:   ', i)
                current_pos = current_pos + 1
                next_index = lista[(lista.index(i) + current_pos)]

    return arranged_list

def main():
    with open('utils/lista_de_exemplo.txt', 'r', encoding='UTF-8') as f:
        txt = f.readlines()
        texto = ''
        for i in txt:
            texto = texto + i + '\n'
        pyperclip.copy(texto)

    lista_cad = pyperclip.paste().split('\n')

    lista_cad = clear_space(lista_cad)

    lista_cad = arrange_list(lista_cad)
    '''
    for i in lista_cad:
        print(i)
    '''

if __name__ == "__main__":
    main()
