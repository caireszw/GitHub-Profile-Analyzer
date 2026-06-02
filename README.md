# GitHub Profile Analyzer

Projeto desenvolvido em Python para consulta e análise de perfis do GitHub utilizando a API pública do GitHub.

## Funcionalidades

- Consultar informações de usuários do GitHub
- Visualizar:
  - Nome de usuário
  - Biografia
  - Quantidade de repositórios
  - Seguidores
  - Seguindo
  - Data de criação da conta
- Listar repositórios públicos de um usuário
- Salvar consultas em arquivo JSON
- Visualizar histórico de consultas
- Comparar usuários cadastrados
- Limpar histórico de consultas
- Interface de terminal utilizando Rich

## Tecnologias Utilizadas

- Python 3
- Requests
- JSON
- Rich

## Estrutura do Projeto

```plaintext
GitHub-Profile-Analyzer/
│
├── main.py
├── consultas.py
├── interface.py
├── users.json
├── README.md
└── requirements.txt
```

## Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/GitHub-Profile-Analyzer.git
```

Acesse a pasta:

```bash
cd GitHub-Profile-Analyzer
```

Instale as dependências:

```bash
pip install requests rich
```

## Como Executar

```bash
python main.py
```

## Exemplo de Uso

### Consulta de Usuário

```plaintext
NOME: gvanrossum
BIO: Creator of Python
REPOSITORIOS: 28
SEGUIDORES: 26296
SEGUINDO: 5
DATA DE CRIAÇÃO: 2012-11-26
```

### Comparação de Usuários

```plaintext
gvanrossum possui 26296 seguidores e 28 repositórios
X
caireszw possui 0 seguidores e 14 repositórios
```

## Objetivos de Aprendizado

Este projeto foi desenvolvido com o objetivo de praticar:

- Consumo de APIs REST
- Requisições HTTP com Requests
- Manipulação de JSON
- Estruturas de dados em Python
- Modularização de código
- Persistência de dados
- Interface de terminal

## Melhorias Futuras

- Evitar usuários duplicados no histórico
- Exportar consultas para CSV
- Exibir ranking dos usuários mais consultados
- Comparação avançada entre usuários
- Interface gráfica
- Integração com outras APIs do GitHub

## Autor

Matheus Caires