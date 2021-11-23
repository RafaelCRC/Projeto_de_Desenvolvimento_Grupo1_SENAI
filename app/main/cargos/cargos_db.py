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
