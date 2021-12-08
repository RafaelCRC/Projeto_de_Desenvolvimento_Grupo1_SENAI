from datetime import datetime
from collections import namedtuple

Range = namedtuple('Range', ['start', 'end'])


class CustosDb:
    items = [
        {
            'id': '1',
            'valor': 54.20,
            'dataInicio': "1999-05-20",
            'dataFim': "1999-07-21",
            'descricao': "Custo relativo à aquisição de material para o projeto delta",
            'deletedBy': "",
            'deletedDate': ""
        },
        {
            'id': '2',
            'valor': 175.00,
            'dataInicio': "2003-08-10",
            'dataFim': "2005-07-15",
            'descricao': "Custo relativo ao pagamento dos funcionários do time 2",
            'deletedBy': "",
            'deletedDate': ""
        },
        {
            'id': '3',
            'valor': 700.50,
            'dataInicio': "2010-08-05",
            'dataFim': "2015-10-23",
            'descricao': "Custo da confraternização anual da empresa",
            'deletedBy': "",
            'deletedDate': ""
        }
    ]

    @classmethod
    def adicionar(cls, item):
        cls.items.append(item)
        return item

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
    def buscarData(cls, inicio, fim, qtdItens=None, pagina=None):
        if inicio and fim:
            listResult = []
            startDate = inicio.split("-")
            startDate = [int(convertString) for convertString in startDate]
            endDate = fim.split("-")
            endDate = [int(convertString) for convertString in endDate]
            for x in cls.items:
                itemStartDate = x['dataInicio'].split("-")
                itemStartDate = [int(convertString) for convertString in itemStartDate]
                itemEndDate = x['dataFim'].split("-")
                itemEndDate = [int(convertString) for convertString in itemEndDate]
                r1 = (Range(start=datetime(startDate[0], startDate[1], startDate[2]),
                            end=datetime(endDate[0], endDate[1], endDate[2])))
                r2 = (Range(start=datetime(itemStartDate[0], itemStartDate[1], itemStartDate[2]),
                            end=datetime(itemEndDate[0], itemEndDate[1], itemEndDate[2])))
                latest_start = max(r1.start, r2.start)
                earliest_end = min(r1.end, r2.end)
                delta = (earliest_end - latest_start).days + 1
                overlap = max(0, delta)
                print(overlap)
                if overlap:
                    listResult.append(x)
            if qtdItens:
                if not pagina:
                    pagina = 1
                inicio = (int(pagina) - 1) * int(qtdItens)
                fim = int(qtdItens) + inicio
                listResult = listResult[inicio: fim]
            return listResult

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
    def markAsRemoved(cls, id, user=""):
        item = next(filter(lambda x: x['id'] == id, cls.items), {})
        index = cls.items.index(item)
        if item:
            item['deletedDate'] = str(datetime.today())
            item['deletedBy'] = user
        cls.items[index] = item
        return item

    @classmethod
    def alterar(cls, id, novo_item: dict):
        item = next(filter(lambda x: x['id'] == id, cls.items), {})
        index = cls.items.index(item)

        if novo_item.get('valor'):
            item['valor'] = novo_item.get('valor')

        if novo_item.get('dataInicio'):
            item['dataInicio'] = novo_item.get('dataInicio')

        if novo_item.get('dataFim'):
            item['dataFim'] = novo_item.get('dataFim')

        if novo_item.get('descricao'):
            item['descricao'] = novo_item.get('descricao')

        if novo_item.get('deletedBy'):
            item['deletedBy'] = novo_item.get('deletedBy')

        if novo_item.get('deletedDate'):
            item['deletedDate'] = novo_item.get('deletedDate')

        cls.items[index] = item
        return item
