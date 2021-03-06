class VagasDB:
    items = [
        {
            'id': '1',
            'status': 'preenchida',
            'descricao': 'Essa é a vaga 1',
            'idCusto': '1',
            'idColaborador': '10',
        },
        {
            'id': '2',
            'status': 'vazia',
            'descricao': 'Essa é a vaga 2',
            'idCusto': '2',
            'idColaborador': ' ',
        },
        {
            'id': '3',
            'status': 'preenchida',
            'descricao': 'Essa é a vaga 3',
            'idCusto': '13',
            'idColaborador': '67',

        }
    ]

    @classmethod
    def adicionar(cls, item):
        cls.items.append(item)
        return True

    @classmethod
    def obter(cls, id=None, pagina=None, quantidade= None):
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
    def obterProjetoPorStatus(cls, status, pagina=None, quantidade=None):
        list = []

        for i in cls.items:
            if status in i['status']:
                list.append(i)
        if not pagina:
            pagina = 1

        if quantidade:
            inicio = (int(pagina) - 1) * int(quantidade)
            fim = int(quantidade) + inicio
            list = list[inicio: fim]
        return list


