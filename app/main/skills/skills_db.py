class SkillsDb:
    items = [
        {
            'id': "1",
            'descricao': "Teste"
        },
        {
            'id': "2",
            'descricao': "Teste1"
        },
        {
            'id': "3",
            'descricao': "Teste2"
        }
    ]

    @classmethod
    def colaboradorSkill(cls, id):
        if id:
            return "Skill do Colaborador"

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
