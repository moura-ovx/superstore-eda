# E-Commerce & Sales Analytics Dashboard

Este projeto consiste em uma aplicação interativa de Análise Exploratória de Dados (EDA) e acompanhamento de métricas de negócios, desenvolvida com Python, Pandas e Streamlit. A solução consome dados reais do dataset **Superstore Sales** (Kaggle) para simular um painel de inteligência comercial.

---

## Estrutura do Projeto

```text
superstore-eda/
├── data/
│   └── train.csv
├── src/
│   ├── app.py
│   └── data_loader.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Funcionalidades Principais

* **Métricas de Negócio (KPIs):** Exibição em tempo real de Faturamento Total, Quantidade de Pedidos e Ticket Médio.
* **Filtros Dinâmicos:** Filtragem interativa por Região e Categoria de Produtos na barra lateral.

## Tecnologias Utilizadas

* **Python 3.10+**: Linguagem base do projeto.
* **Pandas**: Manipulação de dados.
* **Streamlit**: Criação da interface gráfica e gerenciamento de estado da aplicação web.

## Instruções de Instalação e Execução

### 1. Clonar o Repositório

```bash
git clone https://github.com/moura-ovx/superstore-eda.git
cd superstore-eda
```
### 2. Configurar o Ambiente Virtual

No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

No PowerShell:

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```
No Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as Dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a Aplicação

```bash
streamlit run src/app.py
```

A aplicação estará disponível no seu navegador no endereço `http://localhost:8501`.