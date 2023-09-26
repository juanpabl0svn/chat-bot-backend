from flask import Flask
from .routes import answer_route, main_route


app = Flask(__name__)


def init_app(config):
  app.config.from_object(config)

  app.register_blueprint(main_route.main, url_prefix='/')
  app.register_blueprint(answer_route.main, url_prefix='/review')

  return app

