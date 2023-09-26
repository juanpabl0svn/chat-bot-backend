from flask import Flask
from .routes import answer_route, main_route, change_password
from flask_cors import CORS



app = Flask(__name__)

cors = CORS(app)


def init_app(config):
  app.config.from_object(config)

  app.register_blueprint(main_route.main, url_prefix='/')
  app.register_blueprint(answer_route.main, url_prefix='/review')
  app.register_blueprint(change_password.main, url_prefix='/')

  return app

