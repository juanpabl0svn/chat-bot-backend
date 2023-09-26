from wit import Wit
from decouple import config


client = Wit(config('TOKEN'))

def give_an_answer(message: str) -> str | None:
  res = client.message(message)
  if not res['intents'] or res['intents'][0]['name'] == 'no_sense':
    return None 
  return res['intents'][0]['name']
