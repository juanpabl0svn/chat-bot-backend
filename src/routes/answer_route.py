from flask import Blueprint
from ..services.wit_service import give_an_answer

main = Blueprint('answer_blueprint', __name__)

@main.route('/<text>',methods=['GET', 'POST'])
def index(text:str) -> str | None:
  res = give_an_answer(text)
  if res == None:
    return {
      "error": "Did not understand what the user said"
    },400
  return {
      "response": res
    },200