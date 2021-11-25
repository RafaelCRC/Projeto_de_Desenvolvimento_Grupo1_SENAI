from flask import Flask, Blueprint
from flask_restplus import Api
from werkzeug.middleware.proxy_fix import ProxyFix

from app.main.projeto.projeto_controller import api as projeto_ns
from app.main.squad.squad_controller import api as squad_ns
from app.main.custos.custos_controller import api as custos_ns
from app.main.cargos.cargos_controller import api as cargos_ns
from app.main.pacotedeservicos.pacotedeservicos_controller import api as pacote_ns
from app.main.vagas.vagas_controller import api as vagas_ns
from app.main.contadeacesso.contadeacesso_controller import api as conta_ns

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
blueprint = Blueprint('api', __name__)
app.register_blueprint(blueprint)

authorizations = {
    'bearer': {
        'name': "Authorization",
        'in': "header",
        'type': "apiKey",
        'description': "Insert your JWT Token here!"
    }
}
api = Api(app, title='Projects and Teams', version='1.0', description='Projects and Teams API',prefix='/api', authorizations=authorizations)


api.add_namespace(projeto_ns, path='/projeto')
api.add_namespace(squad_ns, path='/squad')
api.add_namespace(pacote_ns, path='/pacote')
api.add_namespace(vagas_ns, path='/vagas')
api.add_namespace(custos_ns, path='/costs')
api.add_namespace(cargos_ns, path='/cargos')
api.add_namespace(conta_ns, path='/conta')
