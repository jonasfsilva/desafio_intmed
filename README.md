# desafio_intmed
Gerencia de Loja com boards no trello

## Url do projeto:
http://ferreirajonasss.pythonanywhere.com/

## Url do Trello:
https://trello.com/b/UJtpW2QR/loja-intmed

## Usuario default para login:
email: admin@gmail.com
password: admin

## URL's da api:

    /api/produtos/ -> CRUD de produtos
    /api/pedidos/  -> Criar Pedidos
    /api/clientes/ -> CRUD de clientes
    /api/webhooks_received/ -> Lista os webhooks recebidos apos mover os cartoes no trello

## Regras de negocio:

    É possivel criar produtos e criar pedidos utilizando os mesmos
    É necessario escolher um produto de cada categoria
    É possivel criar cliente e logar com o mesmo
    É o cliente logado pode criar pedidos e listar apenas os seus pedidos
    O administrador pode ver todos os pedidos e todos os clientes
    Ao criar um pedido o card é adcionado no trello
    Ao mover o card de coluna no trello é salvo o webhook que retornado da api do trello
    Apos processar o webhook o card tem seu status alterado

## Para tesar localmente:
- Clone o repositorio
- Crie e ative a virtulenv 
- Execute python manage.py migrate na raiz do projeto
- Execute o comando populate_db (Opcional, para popular o banco default)