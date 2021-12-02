from flask_restplus import Resource, Namespace, fields
from flask import request
from app.main.custos.custos_db import CustosDb

api = Namespace('Custos',description='Gerenciamento de Custos')
modelo = api.model('CustosModel', {
    'id': fields.String,
    'valor': fields.Float,
    'dataInicio': fields.String,
    'dataFim': fields.String,
    'periodo': fields.Float,
    'descricao': fields.String,
    'deletedBy': fields.String,
    'deletedDate': fields.String
})
@api.route('/')
class CustosController(Resource):
    @api.response(200, "Found with success")
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
        '''if descricao is not None and descricao != '':'''
        return CustosDb.obter(None, descricao, qtdItens, pagina), 200

    @api.expect(modelo)
    def post(self):
        return CustosDb.adicionar(request.json), 201

@api.route('/projeto/<id>')
class CustosIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id: int):
        return CustosDb.projectCost(int(id)), 200

@api.route('/cargo/<id>')
class CustosIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id: int):
        return CustosDb.cargoCost(int(id)), 200

@api.route('/<id>')
class CustosIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id:int):
        return CustosDb.obter(int(id)), 200

    @api.response(200, "Busca realizada com sucesso")
    @api.param('valor', 'Valor do Custo')
    @api.param('dataInicio', 'Data de início do custo')
    @api.param('dataFim', 'Data de término do custo')
    @api.param('periodo', 'periodo do custo')
    @api.param('descricao', 'Descrição do custo')
    @api.param('deletedBy', 'Quem deletou o custo')
    @api.param('deletedDate', 'Data de deleção do custo')
    def put(self, id: int):
        return CustosDb.alterar(int(id), request.json), 201

    def delete(self, id: int):
        return CustosDb.remover(int(id)), 200

@api.route('/<dataInicio>/<dataFim>')
class CustosDataController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, dataInicio:str, dataFim:str):
        return CustosDb.buscarData(str(dataInicio), str(dataFim)), 200


