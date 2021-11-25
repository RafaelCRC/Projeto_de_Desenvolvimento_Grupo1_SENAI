from flask_restplus import Resource, Namespace, fields
from flask import request
from app.main.vagas.vagas_db import VagasDB

api = Namespace('Vagas',description='Controle de Vagas')
modelo = api.model('VagasModel', {
    'id': fields.String,
    'status': fields.String,
    'descricao': fields.String,
    'idCusto': fields.String,
    'idColaborador': fields.String,
})

@api.route('/')
class VagasController(Resource):
    @api.response(200, "Found with success")
    def get(self):
        return VagasDB.obter(), 200
    @api.expect(modelo)
    def post(self):
        return VagasDB.adicionar(request.json), 201


@api.route('/<id>')
class VagasIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id:str):
        return VagasDB.obter(str(id)), 200

    def delete(self, id:str):
        return VagasDB.remover(str(id)), 200
