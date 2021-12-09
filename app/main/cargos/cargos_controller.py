
from flask_restplus import Resource, Namespace, fields
from flask import request
from app.main.cargos.cargos_db import CargosDb
from app.main.squad.squad_db import SquadDb

api = Namespace('Cargos', description="Gerenciamento de Cargos")
modelo = api.model('CargosModel', {
    'id': fields.String,
    'descricao': fields.String,
    'nome': fields.String,
    'funcao': fields.String
})

@api.route('/')
class CargosController(Resource):
    @api.response(200, "Found with success")
    @api.param("qtdItens", "Quantidade de itens por página")
    @api.param("pagina", "Número da página")
    def get(self):
        qtdItens = None
        pagina = None
        if request.method == 'GET':
            if 'qtdItens' in request.args:
                qtdItens = request.args['qtdItens']
            if 'pagina' in request.args:
                pagina = request.args['pagina']
        return CargosDb.obter(None, qtdItens, pagina, titulo=True), 200

    @api.expect(modelo)
    def post(self):
        return CargosDb.adicionar(request.json), 201


@api.route('/findByName/<nome>')
class CargosNomeController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, nome: str):
        return CargosDb.obter(nome=nome, titulo=False), 200


@api.route('/squad/<id>')
class CargosAndSquadIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id: int):
        return SquadDb.obter(str(id)), 200


@api.route('/<id>')
class CargosRemovalIdController(Resource):
    def delete(self, id):
        return CargosDb.remover(id), 200

    def get(self, id: str):
        return CargosDb.obter(id=id, titulo=False), 200

    @api.response(200, "Busca realizada com sucesso")
    @api.expect(modelo)
    def put(self, id):
        return CargosDb.alterar(id, request.json), 201


"""
@api.route('/skill/<id>')
class PessoaIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id:int):
        return CargosDb.cargoSkill(int(id)), 200
"""

