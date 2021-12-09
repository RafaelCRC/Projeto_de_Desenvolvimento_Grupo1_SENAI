class SkillsDb:
    items = [
        {
            'id': "1",
            'descricao': "Skill de id 1"
        },
        {
            'id': "2",
            'descricao': "Skill de id 2"
        },
        {
            'id': "3",
            'descricao': "Skill de id 3"
        }
    ]

    @classmethod
    def colaboradorSkill(cls, id):
        if id:
            return next(filter(lambda x: x['id'] == id, cls.items), {})

    @classmethod
    def adicionar(cls, item):
        cls.items.append(item)
        return True

    @classmethod
    def obter(cls, id=None, descricao=None, qtdItens=None, pagina=None):
        listResult = []
        if not pagina:
            pagina = 1
        if id:
            return next(filter(lambda y: y['id'] == id, cls.items), {})
        else:
            if descricao:
                for x in cls.items:
                    if descricao in x['descricao']:
                        listResult.append(x)
                '''next(filter(lambda x: descricao in x['descricao'], cls.items), {})'''
            else:
                listResult = cls.items
        if qtdItens:
            inicio = (int(pagina) - 1) * int(qtdItens)
            fim = int(qtdItens) + inicio
            listResult = listResult[inicio: fim]
        return listResult

    @classmethod
    def alterar(cls, id, novo_item: dict):
        item = next(filter(lambda x: x['id'] == id, cls.items), {})
        index = cls.items.index(item)
        if novo_item.get('descricao'):
            item['descricao'] = novo_item.get('descricao')
        cls.items[index] = item
        return item

    @classmethod
    def remover(cls, id):
        cls.items = list(filter(lambda x: x['id'] != id, cls.items))
        return {"mensagem": f"id {id} deletado com sucesso"}
