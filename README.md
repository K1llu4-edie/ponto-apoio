# Ponto de Apoio



![image](https://github.com/user-attachments/assets/535a33f9-37b2-467f-ad84-2f6071766b83)


**Ponto de Apoio** é uma plataforma online dedicada à **doação, recebimento e recolhimento de itens** para pessoas em situação de necessidade. Através deste site, pessoas podem fazer doações de itens que não utilizam mais e também requisitar itens essenciais, contribuindo para a construção de uma comunidade mais solidária e colaborativa.

Este projeto foi desenvolvido utilizando **Django** no backend, e **HTML**, **CSS** e **JavaScript** para o frontend.

## Tecnologias Utilizadas

- **Backend:**
  - **Django**: Framework web Python utilizado para o desenvolvimento do sistema.
  
- **Frontend:**
  - **HTML**: Para estruturar as páginas da aplicação.
  - **CSS**: Para estilizar a interface do usuário.
  - **JavaScript**: Para funcionalidades interativas no frontend (ex: formulários dinâmicos, validações).

- **Banco de Dados:**
  - **SQLite**: Banco de dados utilizado durante o desenvolvimento (pode ser configurado para outros SGBDs como PostgreSQL ou MySQL em produções mais avançadas).

## Funcionalidades

A plataforma **Ponto de Apoio** oferece as seguintes funcionalidades:

- **Cadastro de usuários**: Permite que pessoas se cadastrem como doadores ou receptores de itens.
- **Cadastro de doações**: Usuários podem cadastrar os itens que desejam doar juntamentes com seus dados.
- **Recolhimento de doações**: Usuários que precisam de determinados itens podem visualizar as doações disponíveis e entrar em contato para o recolhimento.
- **Listagem de doações e pedidos**: Usuários podem visualizar uma lista de itens disponíveis para doação e também os itens requisitados por outras pessoas.

## Pré-requisitos

Antes de rodar o projeto, certifique-se de ter os seguintes itens instalados na sua máquina:

- **Python 3.x** ou superior: [Link para instalação do Python](https://www.python.org/downloads/)
- **Pip** (gerenciador de pacotes Python) - geralmente vem com o Python.
- **Django** - O framework utilizado para o backend.

## Como Rodar o Projeto

Siga os passos abaixo para rodar o projeto localmente em sua máquina:

### 1. Clone o repositório

Se você ainda não fez o clone do repositório, use o seguinte comando no terminal:

```bash
git clone https://github.com/lucascris203/Ponto-de-Apoio.git
```


### 2. Instruções para Configuração e Execução do Projeto

```bash
cd Ponto-de-Apoio
python -m env  # Para criar o ambiente virtual

cd env\Scripts\activate #Ativar o ambiente virtual

cd .. # para voltar e entrar na  manage.py migrate

cd \env\ponto_de_apoio # aonde o manage.py está localizado

python manage.py migrate # migrações do banco de dados

python manage.py runserver # Para Rodar o servidor de desenvolvimento
```
# Recursos do Projeto


1. **Documentação**: [Link](https://drive.google.com/file/d/1JWsRIDBPNR8dbzVaWkRHT6OhJNopFBaB/view?usp=sharing)
2. **Slides do Projeto**: [Link](https://drive.google.com/file/d/1tgDyiTzS-jTGlP0UOFSLFvrUSzAmgiOM/view?usp=sharing)
