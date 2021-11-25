from flask_restplus import Resource, Namespace, fields
from flask import request
from app.main.squad.squad_db import SquadDb

api = Namespace('Squads',description='Manutenção de Squads')
modelo = api.model('SquadModel', {
    'id': fields.String,
    'nome': fields.String,
    'id_projeto': fields.String,
    'idVagas': fields.List(fields.String)
})

@api.route('/')
class SquadController(Resource):
    @api.response(200, "Found with success")
    def get(self):
        return SquadDb.obter(), 200
    @api.expect(modelo)
    def post(self):
        return SquadDb.adicionar(request.json), 201


@api.route('/<id>')
class SquadIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id:str):
        return SquadDb.obter(str(id)), 200

    def delete(self, id:str):
        return SquadDb.remover(str(id)), 200
