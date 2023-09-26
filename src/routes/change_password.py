from flask import Blueprint,request
import json

main = Blueprint('change_password_blueprint', __name__)

@main.route('/change/password',methods=['POST'])
def index() -> str | None:
  data = json.loads(request.data)
  password = data['password']
  return password