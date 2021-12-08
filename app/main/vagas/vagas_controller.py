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
        pagina = None
        quantidade = None
        if request.method == 'GET':
            if 'pagina' in request.args:
                pagina = request.args['pagina']
            if 'quantidade' in request.args:
                quantidade = request.args['quantidade']

        return VagasDB.obter(pagina, quantidade), 200


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

    @api.response(200, "Elemento atualizado com sucesso")
    @api.expect(modelo)
    def put(self, id: str):
        return VagasDB.alterar(str(id), request.json), 200

@api.route('/<idColaborador>')
class VagasColaboradorIdController(Resource):
    @api.response(200, "Elemento atualizado com sucesso")
    @api.expect(modelo)
    def put(self, idColaborador: str):
        return VagasDB.alterarPorColaborador(str(idColaborador), request.json), 200

@api.route('/FindByStatus/<status>')
class ProjetoNomeController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, status:str):
        pagina = None
        quantidade = None
        if request.method == 'GET':
            if 'pagina' in request.args:
                pagina = request.args['pagina']
            if 'quantidade' in request.args:
                quantidade = request.args['quantidade']

        return VagasDB.obterProjetoPorStatus(str(status), pagina, quantidade), 200
