class Item:
    def __init__(self, linha_lista, itens_ignorados):
        self.item = linha_lista[0:3]
        self.pos = linha_lista[4:8]
        self.quantidade = linha_lista[9:12]
        self.descricao = linha_lista[13:54]
        self.material = linha_lista[55:66]
        self.peso = linha_lista[67:72]

        if self.item.strip() == '':
            self.tipo = 'Continuação'
        elif self.pos.strip() == '' and self.material.strip() == '':
            self.tipo = 'Titulo'
        elif self.item.strip() == 'P':
            self.tipo = 'Parafuso'
        else:
            self.tipo = 'Item'

        for i in itens_ignorados:
            if self.descricao[0:(len(i)-1)] in i:
                self.tipo = 'Comprado'

    def get_lista(self) -> str:
        """
            Metodo para gerar uma String do Item
        """
        if self.tipo == 'Item':
            return f'POS. {self.pos.strip()}   {self.quantidade.strip()} {self.descricao.strip()}  {self.material.strip()}'
