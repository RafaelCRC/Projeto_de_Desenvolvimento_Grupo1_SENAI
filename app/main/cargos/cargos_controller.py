from flask_restplus import Resource, Namespace, fields
from flask import request
from app.main.cargos.cargos_db import CargosDb

api = Namespace('Cargos', description="Gerenciamento de Cargos")
modelo = api.model('CargosModel', {
    'id': fields.String,
    'descricao': fields.String,
    'nome': fields.String,
    'funcao': fields.String
})


@api.route('/')
class PessoaController(Resource):
    @api.response(200, "Found with success")
    def get(self):
        return CargosDb.obter(), 200

    @api.expect(modelo)
    def post(self):
        return CargosDb.adicionar(request.json), 201


@api.route('/query/<query>')
class PessoaController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, query:str):
        return CargosDb.querySearch(str(query)), 200


@api.route('/<id>')
class PessoaIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id:int):
        return CargosDb.obter(str(id)), 200


@api.route('/<id>')
class PessoaIdController(Resource):
    @api.param('id', 'Códgio identificador')
    @api.param('nome', 'Título do cargo')
    @api.param('funcao', "Trabalho a ser executado pelo cargo")
    def put(self, id: str):
        return CargosDb.adicionar(str(id), request.json), 201

@api.route('/<id>')
class PessoaIdController(Resource):
    def delete(self, id: str):
        return CargosDb.remover(int(id)), 200

"""
@api.route('/skill/<id>')
class PessoaIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id:int):
        return CargosDb.cargoSkill(int(id)), 200
"""
