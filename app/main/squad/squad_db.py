class SquadDb:
    items = [
        {
            'id': 1,
            'nome': 'Squad 1',
            'id_projeto': 1
        },
        {
            'id': 2,
            'nome': 'Squad 2',
            'id_projeto': 2
        },
        {
            'id': 3,
            'nome': 'Squad 3',
            'id_projeto': 3
        }
    ]

    @classmethod
    def adicionar(cls, item):
        cls.items.append(item)
        return True

    @classmethod
    def obter(cls, id=None):
        if id:
            return next(filter(lambda x: x['id'] == id, cls.items), {})
        return cls.items

    @classmethod
    def remover(cls, id):
        cls.items = list(filter(lambda x: x['id'] != id, cls.items))
        return {"mensagem": f"id {id} deletado com sucesso"}

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