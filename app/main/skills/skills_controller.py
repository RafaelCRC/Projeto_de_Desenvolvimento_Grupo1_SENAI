from flask_restplus import Resource, Namespace, fields
from flask import request
from app.main.skills.skills_db import SkillsDb

api = Namespace('Skills', description="Gerenciamento de Skills")
modelo = api.model('SkillModel', {
    'id': fields.String,
    'descricao': fields.String
})

@api.route('/')
class SkillsController(Resource):
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
            return SkillsDb.obter(None, descricao, qtdItens, pagina), 200


    @api.expect(modelo)
    def post(self):
        return SkillsDb.adicionar(request.json),201

@api.route('/query/<query>')
class SkillsController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, query:str):
        return SkillsDb.querySearch(str(query)), 200

@api.route('/<id>')
class SkillsIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id:str):
        return SkillsDb.obter(str(id)), 200

@api.route('/colaborador/<id>')
class ColaboradorSkillsIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id):
        return SkillsDb.colaboradorSkill(id), 200

@api.route('/<id>')
class SkillsIdController(Resource):
    @api.param('id', 'Código da Skill')
    @api.param('descricao', 'Descrição da Skill')
    def put(self, id:str):
        return SkillsDb.adicionar(str(id),request.json), 201

@api.route('/<id>')
class SkillsIdController(Resource):
    def delete(self, id: str):
        return SkillsDb.remover(str(id)), 200