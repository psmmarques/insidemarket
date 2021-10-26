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
DATABASE_URL=postgres://jzeaeczpzhhbho:172821100e137f85686909b308b0b13313dfcba4237278dfff0d30a19920cb23@ec2-34-194-14-176.compute-1.amazonaws.com:5432/d26bl1b5bbi5ha


#instalação das libs
pip install -f requirements.txt

#rodar o projeto
python manage.py runserver

ou se quiser publicar no docker
docker-compose up -d

#remover
docker-compose down --rmi all
