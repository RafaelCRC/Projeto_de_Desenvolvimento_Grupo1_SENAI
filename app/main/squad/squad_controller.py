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
        pagina = None
        quantidade = None
        if request.method == 'GET':
            if 'pagina' in request.args:
                pagina = request.args['pagina']
            if 'quantidade' in request.args:
                quantidade = request.args['quantidade']

        return SquadDb.obter(pagina, quantidade), 200

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

    @api.response(200, "Atualizado com sucesso")
    @api.expect(modelo)
    def put(self, id):
        return SquadDb.alterar(id, request.json), 201

@api.route('/Projeto/<id_projeto>')
class SquadProjetoIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id_projeto:str):
        return SquadDb.obterPorIdProjeto(str(id_projeto)), 200


@api.route('/FindByName/<nome>')
class ProjetoNomeController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, nome:str):
        return SquadDb.obterProjetoPorNome(str(nome)), 200


@api.route('/Vaga/<idVaga>')
class SquadVagaIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, idVaga:str):
        return SquadDb.obterProjetoPorIdVaga(str(idVaga)), 200



