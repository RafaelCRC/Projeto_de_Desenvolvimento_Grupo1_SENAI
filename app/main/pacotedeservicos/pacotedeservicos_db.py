class PacoteDeServicosDb:
    items = [
        {
            'id': '1',
            'descricao': 'Esse é o pacote de servicos 1',
            'dataInicio': '10/08/2021',
            'dataFim': '10/09/2021',
            'idSquadContratada': '1',
            'idSquadContratante': '2',
            'idProjeto': '1'
        },
        {
            'id': '2',
            'descricao': 'Esse é o pacote de servicos 2',
            'dataInicio': '01/05/2021',
            'dataFim': '16/06/2021',
            'idSquadContratada': '2',
            'idSquadContratante': '1',
            'idProjeto': '2'

        },
        {
            'id': '3',
            'descricao': 'Esse é o pacote de servicos 3',
            'dataInicio': '12/02/2021',
            'dataFim': '11/03/2021',
            'idSquadContratada': '1',
            'idSquadContratante': '3',
            'idProjeto': '3'

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
    def remover(cls, id):
        cls.items = list(filter(lambda x: x['id'] != id, cls.items))
        return {"mensagem": f"id {id} deletado com sucesso"}

   @classmethod
    def alterar(cls, id, novo_item:dict):
        item = next(filter(lambda x: x['id'] == id,cls.items),{})
        index = cls.items.index(item)

        if novo_item.get('nome'):
            item['nome'] = novo_item.get('nome')

        if novo_item.get('descricao'):
            item['descricao'] = novo_item.get('descricao')

        if novo_item.get('dataInicio'):
            item['dataInicio'] = novo_item.get('dataInicio')

        if novo_item.get('dataFim'):
            item['dataFim'] = novo_item.get('dataFim')

        if novo_item.get('idSquadContratada'):
            item['idSquadContratada'] = novo_item.get('idSquadContratada')

        if novo_item.get('idSquadContratante'):
            item['idSquadContratante'] = novo_item.get('idSquadContratante')

        if novo_item.get('idProjeto'):
            item['idProjeto'] = novo_item.get('idProjeto')

        cls.items[index] = item
        return item