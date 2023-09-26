from flask import Blueprint

from decouple import config

main = Blueprint('main_blueprint', __name__)

@main.route('/',methods=['GET', 'POST'])
def index() -> str | None:
  return config('TOKEN')