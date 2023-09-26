from flask import Blueprint
from ..services.wit_service import give_an_answer

main = Blueprint('answer_blueprint', __name__)

@main.route('/<text>',methods=['GET', 'POST'])
def index(text:str) -> str | None:
  if text == '1' or text == ' ':
    return 'Ingresa texto'
  res = give_an_answer(text)
  return 'No entiendo' if res is None else res