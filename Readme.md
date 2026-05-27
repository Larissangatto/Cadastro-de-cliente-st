# 📝 Customer Management System / Sistema de Gestão de Clientes

A customer registration and consultation system developed with Python and Streamlit.  
Sistema de cadastro e consulta de clientes desenvolvido com Python e Streamlit.
## Preview

<video controls width="100%">
  <source src="./assets/videos/demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## 🚀 Technologies Used / Tecnologias Utilizadas

- Python
- Streamlit
- Pandas
- Poetry

## 📂 Project Structure / Estrutura do Projeto

The project follows a modular architecture to separate responsibilities.  
O projeto segue uma arquitetura modular para separar responsabilidades.

app/
├── data/       # CSV file storage / Armazenamento do arquivo CSV
├── pages/      # Registration and consultation pages / Páginas de cadastro e consulta
├── services/   # Business logic and validations / Lógica de negócio e validações
├── utils/      # CSV file handling / Manipulação de arquivos CSV
└── Home.py     # Application entry point / Ponto de entrada da aplicação

## 🛠️ How to Run / Como Executar

1. Install dependencies. / Instale as dependências.

```bash
poetry install --no-root
```

2. Activate the virtual environment. / Ative o ambiente virtual.

```bash
poetry shell
```

3. Run the app. / Rode o app.

```bash
streamlit run app/Home.py
```

## 📖 Features / Funcionalidades
- Home page with system overview and navigation guide. / Página inicial com visão geral do sistema e guia de navegação.

- Customer registration form. / Formulário para cadastro de clientes.

- Registered customer consultation table. / Tabela para consulta dos clientes cadastrados.

## ⚠️ Technical Notes / Observações Técnicas

- The system uses CSV files for data storage. / O sistema utiliza arquivos CSV para armazenamento dos dados.

- The project separates interface, business logic, and file handling. / O projeto separa interface, lógica de negócio e manipulação de arquivos.

- latin1 encoding is used for Windows compatibility and special characters. / A codificação latin1 é usada para compatibilidade com Windows e caracteres especiais.