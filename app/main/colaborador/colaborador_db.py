class ColaboradorDb:
    items = [
        {
            'id': "1",
            'cpf': "99988877766",
            'nome': "Gleice Lisbino",
            'matricula': "001",
            'telefone': "5581999999999",
            'emailPessoal': "gleice@gmail.com",
            'emailInstitucional': "gleice@unicap.com",
            'lattes': "gleice"
        },
        {
            'id': "2",
            'cpf': "99988877766",
            'nome': "Jose Rodolfo",
            'matricula': "002",
            'telefone': "5581988888888",
            'emailPessoal': "jose@gmail.com",
            'emailInstitucional': "jose@unicap.com",
            "lattes": "jose"
        },
        {
            'id': "3",
            'cpf': "99988877766",
            "nome": "Joao Coelho",
            'matricula': "003",
            'telefone': "558177777777",
            'emailPessoal': "joao@gmail.com",
            'emailInstitucional': "joao@unicap.com",
            "lattes": "joao"
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
    def querySearch(cls, query):
        if query:
            return "busca da query"
