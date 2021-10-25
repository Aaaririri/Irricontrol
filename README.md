# REST API To Do List
![image](https://user-images.githubusercontent.com/64850642/138717317-1ea48785-d968-4436-8625-f634d47c694a.png)


Parte do Teste Técnico da Irricontrol, trata-se de uma REST API para uma lista de afazeres implementada em Python, usando Django e Django REST framework.

## Especificações

* Possui, id, descrição, um atributo chamado done para verificar se a tarefa foi realizada ou não, data de criação e data de atualização;

## Endpoints

* [POST]-`/http://localhost:8000/todos/`
* [PUT]-`/http://localhost:8000/todos/{todo_id}/`
* [DELETE]-`/http://localhost:8000/todos/{todo_id}/`
* [GET]-`/http://localhost:8000/todos/`
* [GET]-`/http://localhost:8000/todos/?done=True/`
* [GET]-`/http://localhost:8000/todos/?done=False/`

## Realizar Download do Projeto:
É possível fazer o download do projeto clicando em Code e realizando o download do arquivo .zip, em sequida o arquivo deve ser descompactado para que seja utilizado.

![image](https://user-images.githubusercontent.com/64850642/138732772-5ce6b349-4550-4ade-a526-f57ee61449f0.png)

Ou é possível realizar a clonagem do repositório:
    
    $ git clone https://github.com/Aaaririri/Irricontrol.git
    
## Como Executar o Projeto:
Com os arquivos baixados, é possível executar projeto como demonstrado abaixo, por recomendação é criada uma venv para isso:

    > cd Irricontrol-main
    > python -m venv venv
    > venv\Scripts\activate.bat
    > pip install -Ur requirements.txt
    > python manage.py runserver
 
