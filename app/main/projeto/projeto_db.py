class ProjetoDb:
    items = [
        {
            'id': '1',
            'nome': 'Projeto 1',
            'descricao': 'Esse é o projeto 1',
            'contatoCliente': 'aaaaa@qwe.com',
            'localizadorJira': 'qweqd',
            'localizadorSgt': 'qwasf',
            'localizadorFgt': 'gfvd',
            'inicioPlanejado': '15/07/2000',
            'fimPlanejado': '15/07/2001',
            'InicioReal': '01/08/2000',
            'fimReal': '02/10/2001',
        },
        {
            'id': '2',
            'nome': 'Projeto 2',
            'descricao': 'Esse é o projeto 2',
            'contatoCliente': '81 921313142',
            'localizadorJira': 'uhqgw',
            'localizadorSgt': 'efsqw',
            'localizadorFgt': 'wrfsa',
            'inicioPlanejado': '07/10/2007',
            'fimPlanejado': '07/08/2008',
            'InicioReal': '01/12/2007',
            'fimReal': '01/12/2008',
        },
        {
            'id': '3',
            'nome': 'Projeto 3',
            'descricao': 'Esse é o projeto 3',
            'contatoCliente': 'jrqwsa@refs.com',
            'localizadorJira': 'hgutn',
            'localizadorSgt': 'ituhn',
            'localizadorFgt': 'urifn',
            'inicioPlanejado': '17/01/2015',
            'fimPlanejado': '17/01/2016',
            'InicioReal': '17/07/2016',
            'fimReal': '01/07/2017',

        }
    ]

    @classmethod
    def adicionar(cls, item):
        cls.items.append(item)
        return True

    @classmethod
    def obterJira(cls, localizadorJira=None):
        if localizadorJira:
            return next(filter(lambda x: x['localizadorJira'] == localizadorJira, cls.items), {})
        return cls.items

    @classmethod
    def obterSgt(cls, localizadorSgt=None):
        if localizadorSgt:
            return next(filter(lambda x: x['localizadorSgt'] == localizadorSgt, cls.items), {})
        return cls.items

    @classmethod
    def obterFgt(cls, localizadorFgt=None):
        if localizadorFgt:
            return next(filter(lambda x: x['localizadorFgt'] == localizadorFgt, cls.items), {})
        return cls.items

    @classmethod
    def obter(cls, id=None, pagina=None, quantidade=None):
        list= []
        if not pagina:
            pagina= 1
        if id:
            return next(filter(lambda x: x['id'] == id, cls.items), {})
        else:
            for i in cls.items:
                list= cls.items
        if quantidade:
            inicio = (int(pagina) - 1) * int(quantidade)
            fim = int(quantidade) + inicio
            list = list[inicio: fim]
        return list

    @classmethod
    def obterProjetoPorNome(cls, nome):
        if nome:
            return next(filter(lambda x: x['nome'] == nome, cls.items), {})
        return cls.items

    @classmethod
    def remover(cls, id):
        cls.items = list(filter(lambda x: x['id'] != id, cls.items))
        return {"mensagem": f"id {id} deletado com sucesso"}

    @classmethod
    def atualizar(cls, id, novo_item:dict):
        item = next(filter(lambda x: x['id'] == id, cls.items), {})
        index = cls.items.index(item)

        if novo_item.get('nome'):
            item['nome'] = novo_item.get('nome')

        if novo_item.get('descricao'):
            item['descricao'] = novo_item.get('descricao')

        if novo_item.get('contatoCliente'):
            item['contatoCliente'] = novo_item.get('contatoCliente')

        if novo_item.get('localizadorJira'):
            item['localizadorJira'] = novo_item.get('localizadorJira')

        if novo_item.get('localizadorSgt'):
            item['localizadorSgt'] = novo_item.get('localizadorSgt')

        if novo_item.get('localizadorFgt'):
            item['localizadorFgt'] = novo_item.get('localizadorFgt')

        if novo_item.get('inicioPlanejado'):
            item['inicioPlanejado'] = novo_item.get('inicioPlanejado')

        if novo_item.get('fimPlanejado'):
            item['fimPlanejado'] = novo_item.get('fimPlanejado')

        if novo_item.get('InicioReal'):
            item['InicioReal'] = novo_item.get('InicioReal')

        if novo_item.get('fimReal'):
            item['fimReal'] = novo_item.get('fimReal')

        cls.items[index] = item
        return item