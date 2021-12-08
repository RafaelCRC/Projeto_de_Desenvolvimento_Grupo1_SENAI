from flask_restplus import Resource, Namespace, fields
from flask import request
from app.main.contadeacesso.contadeacesso_db import ContaDB

api = Namespace('Conta de Acesso',description='Controle de Contas de Acesso')
modelo = api.model('ContaModel', {
    'id': fields.String,
    'nome': fields.String,
    'email': fields.String,
    'senha': fields.String,
    'idColaborador': fields.String,
})

@api.route('/')
class ContaController(Resource):
    @api.response(200, "Found with success")
    def get(self):
        pagina = None
        quantidade = None
        if request.method == 'GET':
            if 'pagina' in request.args:
                pagina = request.args['pagina']
            if 'quantidade' in request.args:
                quantidade = request.args['quantidade']
        return ContaDB.obter(pagina, quantidade), 200

    @api.expect(modelo)
    def post(self):
        return ContaDB.adicionar(request.json), 201


@api.route('/<id>')
class ContaIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id:str):
        return ContaDB.obter(str(id)), 200

    def delete(self, id:str):
        return ContaDB.remover(str(id)), 200

@api.route('/FindByConta/<nome>')
class ContaNomeController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, nome:str):
        return ContaDB.obterContaPorNome(str(nome)), 200

@api.route('/FindByEmail/<email>')
class ContaEmailController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, email:str):
        return ContaDB.obterContaPorEmail(str(email)), 200