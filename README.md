🚀 Plataforma de Negócios Locais da Baixada Santista
📋 Descrição
Aplicação web feita com Django para conectar pequenos negócios locais da Baixada Santista aos consumidores da região. Comerciantes podem cadastrar seus estabelecimentos e divulgar catálogo, horário, endereço e formas de pagamento. Clientes podem navegar, favoritar comércios, adicionar produtos ao carrinho e simular compras.

✨ Funcionalidades principais
🛠️ Cadastro e login para comerciantes (via CNPJ) e clientes.

🏪 Perfil completo do comércio: nome, tipo, horário, endereço e formas de pagamento.

📦 Catálogo de produtos com imagens opcionais, estoque e categorias.

🔍 Busca e filtros para facilitar a navegação do cliente.

🛒 Carrinho de compras com opções de pagamento (pagar no local ou em casa).

💬 Comentários e feedbacks baseados em compras realizadas.

📉 Controle automático do estoque após finalização da compra.

❤️ Sistema de favoritar comércios para clientes.

🏆 Página inicial com comércios e produtos em destaque.

🖼️ Suporte a imagens para perfis e produtos.

🛠️ Tecnologias usadas
Python 3.x 🐍

Django 4.x

PostgreSQL 🐘

HTML, CSS 🎨

JavaScript ⚡

📂 Estrutura do projeto
/app - Models, views, templates e forms principais.

/templates - HTML organizados por funcionalidade.

/static - CSS, JS e imagens estáticas.

/media - Imagens carregadas pelos usuários.

⚙️ Como rodar localmente
Clone o repositório:

bash
Copiar
Editar
git clone <url-do-repo>
cd <nome-do-projeto>
Crie e ative o ambiente virtual:

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
Configure o banco de dados PostgreSQL no settings.py.

Rode as migrations:

bash
Copiar
Editar
python manage.py migrate
Crie um superusuário (opcional):

bash
Copiar
Editar
python manage.py createsuperuser
Inicie o servidor:

bash
Copiar
Editar
python manage.py runserver
Acesse em: http://127.0.0.1:8000/
