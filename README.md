# 🏙️ BXD Santista – Plataforma de Apoio aos Negócios Locais

Este é um sistema web desenvolvido com Django e PostgreSQL, com o objetivo de promover pequenos comércios da região da Baixada Santista, permitindo o cadastro de estabelecimentos e oferecendo um catálogo interativo aos consumidores locais.

## 🚀 Funcionalidades principais

- Cadastro e login para **comerciantes** e **clientes**
- Catálogo de produtos por comércio
- Sistema de **favoritos** e **comentários**
- Carrinho de compras com simulação de pedido
- Página de perfil para clientes e comércios
- Sistema de controle de estoque
- Visualização de produtos em destaque, em falta e mais vendidos
- Suporte a imagem de perfil do comércio e de produtos

---

## ⚙️ Tecnologias utilizadas

- 💻 **Linguagem:** Python 3
- 🌐 **Framework web:** Django
- 🐘 **Banco de dados:** PostgreSQL
- 🎨 **Frontend:** HTML, CSS (estilizado com Bootstrap)
- ☁️ **Hospedagem local:** Django dev server

---

## 🧾 Requisitos

- Python 3.8+
- PostgreSQL instalado
- Git (opcional, para clonar o repositório)

---

## 📦 Instalação e execução

1. **Clone o repositório**

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Crie um ambiente virtual

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # no Linux/macOS
venv\Scripts\activate     # no Windows
Instale as dependências

bash
Copiar
Editar
pip install -r requirements.txt
Configure o banco de dados PostgreSQL

Crie um banco chamado bxd_santista e configure seu settings.py com as credenciais corretas:

python
Copiar
Editar
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bxd_santista',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Execute as migrações

bash
Copiar
Editar
python manage.py makemigrations
python manage.py migrate
Crie um superusuário (opcional)

bash
Copiar
Editar
python manage.py createsuperuser
Inicie o servidor

bash
Copiar
Editar
python manage.py runserver
📁 Organização do projeto
cpp
Copiar
Editar
bxd_santista/
├── comercio/         # app dos comerciantes
├── cliente/          # app dos clientes
├── produtos/         # app de gerenciamento de produtos
├── templates/        # arquivos HTML
├── static/           # arquivos CSS, JS e imagens
└── manage.py         # script principal do Django
📝 Observações
O projeto está em desenvolvimento contínuo.

Sugestões e melhorias são bem-vindas!

👨‍💻 Desenvolvido por
Lu Fernandes de Mello, Vinicius Gomes – Projeto de conclusão de semestre
