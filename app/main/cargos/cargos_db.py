class CargosDb:
    items = [
        {
            'id': "1",
            'nome': "Programador Java Back-End",
            'descricao': "Sênio com pelo menos 5 anos de experiência",
            'funcao': "Ajudar as equipes de desenvolvimento em diversos projetos diferentes"
        },
        {
            'id': "2",
            'nome': "Designer",
            'descricao': "Designer com mais de 3 anos de experiência",
            "funcao": "Fazer várias artes bonitas"
        },
        {
            'id': "3",
            'nome': "Programador Front-End",
            "descricao": "Júnior ou estagiário com mais de 6 meses de trabalho",
            "funcao": "Fazer um front end massa"
        }
    ]

    @classmethod
    def adicionar(cls, item):
        cls.items.append(item)
        return True

    @classmethod
    def obter(cls, id=None, nome=None, qtdItens=None, skill=None, pagina=None, titulo=False):
        list_result = []
        if titulo:
            for x in cls.items:
                list_result.append(x['nome'])
            return list_result
        if not pagina:
            pagina = 1
        if id:
            return next(filter(lambda y: y['id'] == id, cls.items), {})
        else:
            if nome:
                for x in cls.items:
                    if nome in x['nome']:
                        list_result.append(x)
            else:
                list_result = cls.items
        if qtdItens:
            inicio = (int(pagina) - 1) * int(qtdItens)
            fim = int(qtdItens) + inicio
            list_result = list_result[inicio: fim]
        return list_result

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
        if novo_item.get('descricao'):
            item['descricao'] = novo_item.get('descricao')
        if novo_item.get('funcao'):
            item['funcao'] = novo_item.get('funcao')
        cls.items[index] = item
        return item

    @classmethod
    def querySearch(cls, query):
        if query:
            return "busca da query"
