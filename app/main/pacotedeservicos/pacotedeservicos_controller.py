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
        return PacoteDeServicosDb.obter(), 200
    @api.expect(modelo)
    def post(self):
        return PacoteDeServicosDb.adicionar(request.json), 201


@api.route('/<id>')
class PacoteIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id:str):
        return PacoteDeServicosDb.obter(str(id)), 200

    def delete(self, id:str):
        return PacoteDeServicosDb.remover(str(id)), 200
