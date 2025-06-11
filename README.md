Projeto Django - Plataforma de Negócios Locais da Baixada Santista
Descrição
Este projeto é uma aplicação web desenvolvida em Django para conectar pequenos negócios locais da Baixada Santista a consumidores da região. O sistema permite que comerciantes se cadastrem e divulguem seus estabelecimentos, exibindo catálogo de produtos, horários de funcionamento, endereço e formas de pagamento. Os clientes podem navegar, favoritar comércios, adicionar produtos ao carrinho e simular compras.

Funcionalidades principais
Cadastro e login para comerciantes (com CNPJ) e clientes.

Perfil do comércio com informações como nome, tipo, horário, endereço e formas de pagamento.

Catálogo de produtos, com imagens opcionais, estoque e categorias.

Busca e filtros para facilitar a navegação do cliente.

Sistema de carrinho de compras com opções de pagamento (pagar no local ou em casa).

Comentários e feedbacks para comércios baseados em compras realizadas.

Controle de estoque automático após finalização da compra.

Sistema de favoritar comércios para clientes.

Página inicial com destaque para comércios e produtos mais vendidos.

Suporte a imagens para perfil do comércio e produtos.

Tecnologias usadas
Python 3.x

Django 4.x

PostgreSQL (banco de dados)

HTML, CSS (templates do Django)

JavaScript (para interatividade básica)

Estrutura do projeto
/app - Aplicação principal com models, views, templates e forms.

/templates - Arquivos HTML organizados por funcionalidades (perfil, comércio, cliente, catálogo, etc).

/static - Arquivos estáticos como CSS, JS e imagens.

/media - Imagens carregadas pelos usuários (comércios e produtos).

Como rodar o projeto localmente
Clone o repositório:

bash
Copiar
Editar
git clone <url-do-repo>
cd <nome-do-projeto>
Crie e ative um ambiente virtual Python:

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Configure o banco de dados PostgreSQL e atualize settings.py com suas credenciais.

Execute as migrations:

bash
Copiar
Editar
python manage.py migrate
Crie um superusuário (opcional, para administração):

bash
Copiar
Editar
python manage.py createsuperuser
Inicie o servidor de desenvolvimento:

bash
Copiar
Editar
python manage.py runserver
Acesse o site em http://127.0.0.1:8000/

