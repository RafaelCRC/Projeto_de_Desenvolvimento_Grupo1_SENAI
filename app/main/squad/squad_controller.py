from flask_restplus import Resource, Namespace, fields
from flask import request
from app.main.squad.squad_db import SquadDb

api = Namespace('Squads',description='Manutenção de Squads')
modelo = api.model('SquadModel', {
    'id': fields.Integer,
    'nome': fields.String,
    'id_projeto': fields.Integer
})

@api.route('/')
class PessoaController(Resource):
    @api.response(200, "Found with success")
    def get(self):
        return SquadDb.obter(), 200
    @api.expect(modelo)
    def post(self):
        return SquadDb.adicionar(request.json), 201

@api.route('/<id>')
class PessoaIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id:int):
        return SquadDb.obter(int(id)), 200

    @api.response(200, "Busca realizada com sucesso")
    @api.param('nome','Nome da Squad')
    @api.param('id_projeto','Id do Projeto Ligado a Squad')
    def put(self, id:int):
        return SquadDb.alterar(int(id), request.json), 201

    def delete(self, id:int):
        return SquadDb.remover(int(id)), 200
