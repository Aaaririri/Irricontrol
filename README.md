# REST-API-To-Do-List
![image](https://user-images.githubusercontent.com/64850642/138717317-1ea48785-d968-4436-8625-f634d47c694a.png)


Parte do Teste Técnico da Irricontrol, trata-se de uma REST API para uma lista de afazeres implementada em Python, usando Django e Django REST framework.

## Especificações

* Possui, id, descrição, um atributo chamado done para verificar se a tarefa foi realizada ou não, data de criação e data de atualização;

## Endpoints

* [POST]-`/http://localhost:8000/todos/`
* [PUT]-`/http://localhost:8000/todos/{todo_id}/`
* [DELETE]-`/http://localhost:8000/todos/{todo_id}/`
* [GET]-`/http://localhost:8000/todos/`
* [GET]-`/http://localhost:8000/todos/{todo_id}/`
* [GET]-`/http://localhost:8000/todos/?done=True/`
* [GET]-`/http://localhost:8000/todos/?done=False/`

