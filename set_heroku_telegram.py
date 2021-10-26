import requests
from core.constant import TOKEN

urlComp = 'https://api.telegram.org/bot{0}/setWebhook?url=https://insidemarketb3.herokuapp.com/event/'.format(TOKEN)
print("Setando a url no telegram: {0}".format(urlComp))

hookResult = requests.get(urlComp)
print("Conteudo da resposta: {0}".format(hookResult.content))


