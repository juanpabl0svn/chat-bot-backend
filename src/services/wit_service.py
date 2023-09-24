from wit import Wit

from token_wit import TOKEN

client = Wit(TOKEN)

res = client.message('quiero cambiar mi contraseña')

print(res)