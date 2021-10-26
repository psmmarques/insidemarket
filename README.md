InsideMarket

Telegram Bot escrito em python com Django para busca de dados
do mercado financeiro.

(https://t.me/testeMarketBot)

![Principal](https://github.com/psmarques/MegasenaExplorer/blob/master/JarvisB3_Bot/print.png?raw=true)


## Rodar a aplicação

Lembre-se de alterar o token na core/constant.py assim não haverá problema com o robo
prod

Para rodar/debugar esta aplicação é necessario instalar o python 3.8 ou superior
instalar as bibliotecas contidas no requirements.txt

#Arquivo .env
Crie o arquivo .env dentro da pasta insidemarketb3/.env
DATABASE_URL=xxxx


#instalação das libs
pip install -f requirements.txt

#rodar o projeto
python manage.py runserver

ou se quiser publicar no docker
docker-compose up -d

#remover
docker-compose down --rmi all
