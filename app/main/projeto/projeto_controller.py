from flask_restplus import Resource, Namespace, fields
from flask import request
from app.main.projeto.projeto_db import ProjetoDb

api = Namespace('Projeto', description='Manutenção de Projetos')
modelo = api.model('ProjetoModel', {
    'id': fields.String,
    'nome': fields.String,
    'descricao': fields.String,
    'ContatoCliente': fields.String,
    'localizadorJira': fields.String,
    'localizadorSgt': fields.String,
    'localizadorFgt': fields.String,
    'inicioPlanejado': fields.String,
    'fimPlanejado': fields.String,
    'InicioReal': fields.String,
    'fimReal': fields.String,
})


@api.route('/')
class ProjetoController(Resource):
    @api.response(200, "Found with success")
    def get(self):
        return ProjetoDb.obter(), 200

    @api.expect(modelo)
    def post(self):
        return ProjetoDb.adicionar(request.json), 201


@api.route('/<id>')
class ProjetoIdController(Resource):

    @api.response(200, "Busca realizada com sucesso")
    def get(self, id:str):
        return ProjetoDb.obter(str(id)), 200

    @api.response(200, "Elemento deletado com sucesso")
    def delete(self, id: str):
        return ProjetoDb.remover(str(id)), 200


@api.route('/<nome>')
class ProjetoNomeController(Resource):

    @api.response(200, "Busca realizada com sucesso")
    def get(self, nome:str):
        return ProjetoDb.obterProjetoPorNome(str(nome)), 200


@api.route('/<localizadorJira>')
class ProjetoLocalizadorJiraController(Resource):

    @api.response(200, "Busca realizada com sucesso")
    def get(self, localizadorJira:str):
        return ProjetoDb.obterJira(str(localizadorJira)), 200


@api.route('/<localizadorSgt>')
class ProjetoLocalizadorSgtController(Resource):

    @api.response(200, "Busca realizada com sucesso")
    def get(self, localizadorSgt:str):
        return ProjetoDb.obterSgt(str(localizadorSgt)), 200


@api.route('/<localizadorFgt>')
class ProjetoLocalizadorFgtController(Resource):

    @api.response(200, "Busca realizada com sucesso")
    def get(self, localizadorFgt:str):
        return ProjetoDb.obterFgt(str(localizadorFgt)), 200