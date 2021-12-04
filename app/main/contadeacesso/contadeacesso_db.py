class ContaDB:
    items = [
        {
            'id': '1',
            'nome': 'Nome 1',
            'email': 'mail@mail.com',
            'senha': 'senha1',
            'idColaborador': '12',
        },
        {
            'id': '2',
            'nome': 'Nome 2',
            'email': 'mail2@mail.com',
            'senha': 'senha2',
            'idColaborador': '45',
        },
        {
            'id': '3',
            'nome': 'Nome 3',
            'email': 'mail3@mail.com',
            'senha': 'senha3',
            'idColaborador': '123',

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
    def obterContaPorNome(cls, nome):
        if nome:
            return next(filter(lambda x: x['nome'] == nome, cls.items), {})
        return cls.items

    @classmethod
    def obterContaPorEmail(cls, email):
        if email:
            return next(filter(lambda x: x['email'] == email, cls.items), {})
        return cls.items