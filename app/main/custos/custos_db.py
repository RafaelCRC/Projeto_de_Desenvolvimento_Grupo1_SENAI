from datetime import datetime


class CustosDb:
    items = [
        {
            'id': "1",
            'valor': 54.20,
            'dataInicio': "1999-05-20",
            'dataFim': "1999-07-21",
            'periodo': 2.5,
            'descricao': "Custo relativo à aquisição de material para o projeto delta",
            'deletedBy': "",
            'deletedDate': ""
        },
        {
            'id': "2",
            'valor': 175.00,
            'dataInicio': "2003-08-10",
            'dataFim': "2005-07-15",
            'periodo': 20,
            'descricao': "Custo relativo ao pagamento dos funcionários do time 2",
            'deletedBy': "",
            'deletedDate': ""
        },
        {
            'id': "3",
            'valor': 700.50,
            'dataInicio': "2010-08-05",
            'dataFim': "2015-10-23",
            'periodo': 36,
            'descricao': "Custo da confraternização anual da empresa",
            'deletedBy': "",
            'deletedDate': ""
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
    def buscarData(cls, inicio, fim):
        if inicio or fim:
            return "custos no periodo entre as datas"

    @classmethod
    def querySearch(cls, query):
        if query:
            return "busca da query"

    @classmethod
    def projectCost(cls, id):
        if id:
            return "custo do projeto"

    @classmethod
    def cargoCost(cls, id):
        if id:
            return "custos do cargo"

    @classmethod
    def remover(cls, id):
        cls.items = list(filter(lambda x: x['id'] != id, cls.items))
        return {"mensagem": f"id {id} deletado com sucesso"}

    @classmethod
    def alterar(cls, id, novo_item:dict):
        item = next(filter(lambda x: x['id'] == id, cls.items), {})
        index = cls.items.index(item)

        if novo_item.get('valor'):
            item['valor'] = novo_item.get('valor')

        if novo_item.get('dataInicio'):
            item['dataInicio'] = novo_item.get('dataInicio')

        if novo_item.get('dataFim'):
            item['dataFim'] = novo_item.get('dataFim')

        if novo_item.get('periodo'):
            item['periodo'] = novo_item.get('periodo')

        if novo_item.get('lozalizadorSgt'):
            item['lozalizadorSgt'] = novo_item.get('lozalizadorSgt')

        if novo_item.get('descricao'):
            item['descricao'] = novo_item.get('descricao')

        if novo_item.get('deletedBy'):
            item['deletedBy'] = novo_item.get('deletedBy')

        if novo_item.get('deletedDate'):
            item['deletedDate'] = novo_item.get('deletedDate')

        cls.items[index] = item
        return item