# 📝 Customer Management System / Sistema de Gestão de Clientes (Streamlit)

This is a customer registration and consultation system developed in Python. /
Este é um sistema de cadastro e consulta de clientes desenvolvido em Python.

## 🚀 Technologies Used / Tecnologias Utilizadas
- Python: Main language. / Linguagem principal.

- Streamlit: Web interface framework. / Framework para a interface web.

- Pandas: Data manipulation and CSV handling. / Manipulação de dados e tratamento de CSV.

- Poetry: Package and environment management. / Gerenciamento de pacotes e ambientes.

 ## 📂 Project Structure / Estrutura do Projeto
 
The project follows a modular architecture to separate concerns:/
O projeto segue uma arquitetura modular para separar as responsabilidades:

- app/data/: CSV file storage. / Armazenamento do arquivo CSV.

- app/pages/: Secondary pages (Registration & Consultation). / Páginas secundárias (Cadastro e Consulta).

- app/services/: Business logic and validations. / Lógica de negócio e validações.

- app/utils/: File handling (CSV read/write). / Manipulação de arquivos (leitura/escrita de CSV).

- Home.py: Application entry point (Home). / Ponto de entrada da aplicação (Home).

## 🛠️ How to Run / Como Executar
1- Install Poetry: Ensure you have Poetry installed. / Certifique-se de ter o Poetry instalado.

2 - Install Dependencies / Instalar Dependências:

Bash
```bash
poetry install
```
3 - Run the App / Rodar o App:

Bash
  ```bash
 poetry shell
 streamlit run Home.py
  ```
## 📖 Features / Funcionalidades
- Home: System overview and navigation guide. / Visão geral do sistema e guia de navegação.

- Registration: Form to register new customers. / Formulário para cadastrar novos clientes.

- Consultation: Table to view registered records. / Tabela para visualizar os registros cadastrados.

⚠️ Technical Notes / Observações Técnicas
- Encoding: The system uses latin1 for Windows compatibility and special characters. / Encoding: O sistema utiliza latin1 para compatibilidade com Windows e caracteres especiais.

- Architecture: Logic is separated from the UI for professional code standards. / Arquitetura: A lógica está separada da interface para seguir padrões profissionais de código.
