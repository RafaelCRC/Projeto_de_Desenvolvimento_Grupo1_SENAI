from flask_restplus import Resource, Namespace, fields
from flask import request
from app.main.pacotedeservicos.pacotedeservicos_db import PacoteDeServicosDb

api = Namespace('Pacote de Serviços',description='Manutenção dos pacotes')
modelo = api.model('PacoteModel', {
    'id': fields.String,
    'descricao': fields.String,
    'dataInicio': fields.String,
    'dataFim': fields.String,
    'idSquadContratada': fields.String,
    'idSquadContratante': fields.String,
    'idProjeto': fields.String
})

@api.route('/')
class PacoteController(Resource):
    @api.response(200, "Found with success")
    def get(self):
        pagina = None
        quantidade = None
        if request.method == 'GET':
            if 'pagina' in request.args:
                pagina = request.args['pagina']
            if 'quantidade' in request.args:
                quantidade = request.args['quantidade']

        return PacoteDeServicosDb.obter(pagina, quantidade), 200

    @api.expect(modelo)
    def post(self):
        return PacoteDeServicosDb.adicionar(request.json), 201


@api.route('/<id>')
class PacoteIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id:str):
        return PacoteDeServicosDb.obter(str(id)), 200

    @api.response(200, "Elemento atualizado com sucesso")
    @api.expect(modelo)
    def put(self, id: str):
        return PacoteDeServicosDb.alterar(str(id), request.json), 200

    def delete(self, id:str):
        return PacoteDeServicosDb.remover(str(id)), 200


@api.route('/SquadContratada/<idSquadContradada>')
class PacoteIdSquadContratante(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, idSquadContradada:str):
        return PacoteDeServicosDb.obterPacotePorIdSquadContratada(str(idSquadContradada)), 200


@api.route('/SquadContratante/<idSquadContratante>')
class PacoteIdSquadContratada(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, idSquadContratante:str):
        return PacoteDeServicosDb.obterPacotePorIdSquadContratante(str(idSquadContratante)), 200

@api.route('/Projeto/<idProjeto>')
class PacoteProjetoSquad(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, idProjeto:str):
        return PacoteDeServicosDb.obterPacotePorIdProjeto(str(idProjeto)), 200





