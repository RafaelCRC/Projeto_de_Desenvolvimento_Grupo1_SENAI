class SquadDb:
    items = [
        {
            'id': '1',
            'nome': 'Squad 1',
            'id_projeto': '1',
            'idVagas': [
                '13', '15', '19', '23', '12'
            ]
        },
        {
            'id': '2',
            'nome': 'Squad 2',
            'id_projeto': '2',
            'idVagas': [
                '10', '34', '65', '87', '44'
            ]
        },
        {
            'id': '3',
            'nome': 'Squad 3',
            'id_projeto': '3',
            'idVagas': [
                '99', '98', '97', '96', '95'
            ],
        }
    ]

    @classmethod
    def adicionar(cls, item):
        cls.items.append(item)
        return True

    @classmethod
    def obter(cls, id=None, pagina=None, quantidade=None):
        list = []
        if not pagina:
            pagina = 1
        if id:
            return next(filter(lambda x: x['id'] == id, cls.items), {})
        else:
            for i in cls.items:
                list = cls.items
        if quantidade:
            inicio = (int(pagina) - 1) * int(quantidade)
            fim = int(quantidade) + inicio
            list = list[inicio: fim]
        return list

    @classmethod
    def obterProjeto(cls, id=None):
        if id:
            return next(filter(lambda x: x['idProjeto'] is id, cls.items), {})
        return cls.items

    @classmethod
    def obterIdVaga(cls, id=None):
        if id:
            for i in range(len(['idVagas'])):
                if ['idVagas'].index(i) == id:
                    return cls.items
            return next(filter(lambda x: x['idVagas'] is id, cls.items), {})

    @classmethod
    def remover(cls, id):
        cls.items = list(filter(lambda x: x['id'] != id, cls.items))
        return {"mensagem": f"id {id} deletado com sucesso"}

    @classmethod
    def obterProjetoPorNome(cls, nome):
        if nome:
            return next(filter(lambda x: x['nome'] == nome, cls.items), {})
        return cls.items

    @classmethod
    def alterar(cls, id, novo_item: dict):
        item = next(filter(lambda x: x['id'] == id, cls.items), {})
        index = cls.items.index(item)

        if novo_item.get('nome'):
            item['nome'] = novo_item.get('nome')

        if novo_item.get('id_projeto'):
            item['id_projeto'] = novo_item.get('id_projeto')

        cls.items[index] = item
        return item