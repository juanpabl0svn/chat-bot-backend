from wit import Wit
from decouple import config


# client = Wit(config('TOKEN'))

options = {
  "password": ['cambiar','contraseña','clave','ingresar','problema','quiero'],
  "pqr" : ['problema','pqr','cambiar','no','funciona','error','quiero','queja','insatisfecho'],
  "tournament" : ['torneo','problema','ingresar','persona','participante'],
}

# def give_an_answer(message: str) -> str | None:
#   res = client.message(message)
#   if not res['intents'] or res['intents'][0]['name'] == 'no_sense':
#     return None 
#   return res['intents'][0]['name']

def give_an_answer(message: str) -> str | None:
  answers = message.lower().split(' ')
    

  best_one = ''
  contador = 0
  for clave in options:
    contador_temp=0
    for answer in answers:
      if answer in options[clave]:
        contador_temp+=1
    if contador_temp>contador:
      contador = contador_temp
      best_one = clave
  
  if contador <3:
    if 'contraseña' in answers or 'clave' in answers: return 'password'
    if 'pqr' in answers or 'queja' in answers or 'insatisfecho' in answers or 'insatisfecha' in answers: return 'pqr'
    if 'torneo' in answers: return 'tournament'
    if len(answers) == 1:
      if answers[0] == 'si':
        return 'yes'
      if answers[0] == 'no':
        return 'no'
      return 'no_sense'
    best_one = 'no_sense'
  return best_one





