from flask_restplus import Resource, Namespace, fields
from flask import request
from app.main.projeto.projeto_db import ProjetoDb

api = Namespace('Projeto',description='Manutenção de Projetos')
modelo = api.model('ProjetoModel', {
    'id': fields.Integer,
    'nome': fields.String,
    'descricao': fields.String,
    'ContatoCliente': fields.String,
    'lozalizadorGira': fields.String,
    'lozalizadorSgt': fields.String,
    'lozalizadorFgt': fields.String,
    'inicioPlanejado': fields.String,
    'fimPlanejado': fields.String,
    'InicioReal': fields.String,
    'fimReal': fields.String
})
@api.route('/')
class PessoaController(Resource):
    @api.response(200, "Found with success")
    def get(self):
        return ProjetoDb.obter(), 200
    @api.expect(modelo)
    def post(self):
        return ProjetoDb.adicionar(request.json), 201

@api.route('/<id>')
class PessoaIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id:int):
        return ProjetoDb.obter(int(id)), 200

    @api.response(200, "Busca realizada com sucesso")
    @api.param('nome','Nome do Projeto')
    @api.param('descricao','Descrição do Projeto')
    @api.param('contatoCliente','Contato do Cliente')
    @api.param('lozalizadorGira','Localizador do Gira')
    @api.param('lozalizadorSgt','Localizador do Sgt')
    @api.param('lozalizadorFgt','Localizador do Fgt')
    @api.param('inicioPlanejado','Data de Inicio Planejado do Projeto')
    @api.param('fimPlanejado','Data de Fim Planejado do Projeto')
    @api.param('InicioReal', 'Data de Inicio Real do Projeto')
    @api.param('fimReal', 'Data de Fim Real do Projeto')
    def put(self, id:int):
        return ProjetoDb.alterar(int(id), request.json), 201

    def delete(self, id:int):
        return ProjetoDb.remover(int(id)), 200
