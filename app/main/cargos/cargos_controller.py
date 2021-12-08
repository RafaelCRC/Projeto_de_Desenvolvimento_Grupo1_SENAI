
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
        descricao = None
        qtdItens = None
        pagina = None
        if request.method == 'GET':
            if 'descricao' in request.args:
                descricao = request.args['descricao']
            if 'qtdItens' in request.args:
                qtdItens = request.args['qtdItens']
            if 'pagina' in request.args:
                pagina = request.args['pagina']
        return CargosDb.obter(None, descricao, qtdItens, pagina), 200

    @api.expect(modelo)
    def post(self):
        return CargosDb.adicionar(request.json), 201


@api.route('/findByName/<nome>')
class CargosNomeController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, nome: str):
        return CargosDb.obter(nome=nome), 200


@api.route('/squad/<id>')
class CargosAndSquadIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id: int):
        return SquadDb.obter(str(id)), 200


@api.route('/<id>')
class CargosIdController(Resource):
    @api.param('id', 'Códgio identificador')
    @api.param('nome', 'Título do cargo')
    @api.param('funcao', "Trabalho a ser executado pelo cargo")
    def put(self, id: str):
        return CargosDb.adicionar(str(id), request.json), 200

@api.route('/<id>')
class CargosRemovalIdController(Resource):
    def delete(self, id):
        return CargosDb.remover(id), 200

    def get(self, id: str):
        return CargosDb.obter(id=id), 200


"""
@api.route('/skill/<id>')
class PessoaIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id:int):
        return CargosDb.cargoSkill(int(id)), 200
"""
