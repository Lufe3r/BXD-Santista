# 🏪 BXD Santista

**BXD Santista** é uma plataforma web desenvolvida em Django que conecta pequenos comércios da Baixada Santista a consumidores locais. O sistema permite que comerciantes cadastrem seus estabelecimentos e gerenciem seus produtos, enquanto clientes podem visualizar catálogos, fazer compras e interagir com os comércios.

## 🚀 Funcionalidades

### 👥 Acesso de Usuários
- Cadastro e login para clientes e comerciantes.
- Sistema de sessão independente para cada tipo de usuário.
- Mudança de senha para ambos os perfis.

### 🛒 Cliente
- Catálogo de produtos por comércio.
- Adição de produtos ao carrinho.
- Simulação de compra com opção de pagamento "no local" ou "em casa".
- Favoritar comércios.
- Comentar apenas nos comércios em que já comprou.
- Visualização de códigos de compra.

### 🏪 Comércio
- Cadastro do estabelecimento (nome, tipo, horário de funcionamento, formas de pagamento, localização, imagem).
- Adição de produtos com opção de imagem.
- Destaques para produtos mais vendidos e com estoque em falta.
- Feedback de comentários recebidos.
- Alerta quando ≥10 produtos estiverem com estoque baixo.
- Visualização dos códigos de compra dos clientes.

## 🧰 Tecnologias

- Python 3.11+
- Django 4.x
- PostgreSQL
- HTML + CSS
- JavaScript (básico)
- Bootstrap (opcional)

## ⚙️ Instalação e Execução Local

### 1. Clone o repositório
```bash

git clone https://github.com/seu-usuario/bxd-santista.git
cd bxd-santista
2. Crie e ative o ambiente virtual
bash
Copiar
Editar
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows
3. Instale as dependências
bash
Copiar
Editar
pip install -r requirements.txt
4. Configure o banco de dados
Edite o arquivo settings.py com os dados do seu PostgreSQL:

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
5. Execute as migrações
bash
Copiar
Editar
python manage.py makemigrations
python manage.py migrate
6. Inicie o servidor
bash
Copiar
Editar
python manage.py runserver
7. Acesse o sistema
Abra o navegador e acesse: http://127.0.0.1:8000

🗂️ Estrutura de Pastas (resumo)
csharp
Copiar
Editar
bxd_santista/
├── app/                    # Aplicações Django (clientes, comércios, produtos, etc.)
├── static/                 # Arquivos estáticos (CSS, imagens)
├── templates/              # Templates HTML
├── media/                  # Imagens de perfil e produtos
├── manage.py
├── requirements.txt
└── README.md
📷 Imagem de Perfil Padrão
Se nenhum arquivo for enviado, o sistema usa automaticamente uma imagem de perfil padrão.

📃 Licença
Este projeto é de uso acadêmico e não possui fins comerciais.

Feito com 💙 para a Baixada Santista.

yaml
Copiar
Editar

---

Se quiser que eu crie o `requirements.txt` automaticamente também, posso gerar para você. Deseja isso?







