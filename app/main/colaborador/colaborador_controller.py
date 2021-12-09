from flask_restplus import Resource, Namespace, fields
from flask import request
from app.main.colaborador.colaborador_db import ColaboradorDb

api = Namespace('Colaborador', description="Gerenciamento de Colaboradores")
modelo = api.model('ColaboradorModel', {
    'id': fields.String,
    'cpf': fields.String,
    'nome': fields.String,
    'matricula': fields.String,
    'telefone': fields.String,
    'emailPessoal': fields.String,
    'emailInstitucional': fields.String,
    'lattes': fields.String
})


@api.route('/')
class PessoaController(Resource):
    @api.response(200, "Found with success")
    def get(self):
        return ColaboradorDb.obter(), 200

    @api.expect(modelo)
    def post(self):
        return ColaboradorDb.adicionar(request.json), 201

@api.route('/cargo/<id>')
class CargosAndSquadIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id: int):
        return ColaboradorDb.obter(str(id)), 200


@api.route('/<id>')
class PessoaIdController(Resource):
    @api.response(200, "Found with success")
    def get(self, id:int):
        return ColaboradorDb.obter(str(id)), 200




@api.route('/<id>')
class PessoaIdController(Resource):
    def get(self, id: str):
        return ColaboradorDb.obter(id=id, titulo=False), 200

    @api.response(200, "Busca realizada com sucesso")
    @api.expect(modelo)
    def put(self, id):
        return ColaboradorDb.alterar(id, request.json), 201
    def delete(self, id: str):
        return ColaboradorDb.remover(int(id)), 200

