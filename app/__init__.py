from flask import Flask, Blueprint
from flask_restplus import Api
from werkzeug.middleware.proxy_fix import ProxyFix

from app.main.projeto.projeto_controller import api as projeto_ns
from app.main.squad.squad_controller import api as squad_ns
from app.main.custos.custos_controller import api as custos_ns

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
api.add_namespace(custos_ns, path='/costs')