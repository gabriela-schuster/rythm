# Rythm
Um app (ou jogo) simples, aionde você ganha xp ao completar tarefas diárias

## Instalação:
instale as dependencias com
```
$ pip install -r requeriments.txt
```
inicie o projeto django com
```
$ django-admin startproject rythm
```
e copie os arquivos desse repositorio para a pasta do projeto
#### crie um usuario mysql para usar com a aplicação, o default é root, mas pode-se mudar em /rythm/settings.py, pela variavel DATABASES
***
crie um arquivo .env em /rythm/.env com o seguinte conteudo:
```
PASSWORD=<mysql_password>
SECRET_KEY=<secret>
```
#### OBS: a secret_key é única do seu projeto, ela estará visível em /rythm/settings.py em 
```
SECRET_KEY = <secret>
```
#### OBS2: para rodar o server em modo debug, va para /rythm/settings.py, e altere
```
DEBUG = True
```
