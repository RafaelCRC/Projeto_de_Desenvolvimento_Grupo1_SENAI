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
            'status': 'não preenchida',
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
    def obter(cls, id=None):
        if id:
            return next(filter(lambda x: x['id'] is id, cls.items), {})
        return cls.items

    @classmethod
    def remover(cls, id):
        cls.items = list(filter(lambda x: x['id'] != id, cls.items))
        return {"mensagem": f"id {id} deletado com sucesso"}
