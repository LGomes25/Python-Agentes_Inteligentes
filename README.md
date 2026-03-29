# 📖 Introdução às LLMs
Este repositório reúne os estudos e implementações realizados em uma trilha de introdução a Large Language Models (LLMs).
O projeto está organizado em módulos e aulas, mostrando a evolução desde chamadas simples de modelos até a construção de um chatbot completo com Streamlit, LangChain e LangGraph.

# 🚀 Estrutura do Projeto
A pasta src/ contém os códigos separados por módulos e aulas:

- Módulo 2 – Terminal
- m2aula1: Introdução a LLM com chamada direta e resposta.
- m2aula2: Uso do LangChain com messages e prompts.
- m2aula3: Introdução ao LangGraph e suas estruturas.
- m2aula4: Leitura de PDF e integração com LangChain/LangGraph.
- Módulo 3 – Streamlit
- m3aula1: Primeiros passos com Streamlit.
- m3aula2: Backend com LangChain/LangGraph e frontend com Streamlit.
- m3aula3: Leitura de PDF integrada ao frontend/backend.
- m3aula4: Uso de streaming para mostrar a formação da resposta do LLM.
- Extra: Bot com histórico como contexto, permitindo memória de conversa.

# ⚙️ Configuração do LM Studio
Este projeto utiliza o LM Studio como servidor local de modelos.
No arquivo config.py, estão definidas funções para configurar chamadas tanto via LangChain quanto via cliente OpenAI:

- Base URL: http://127.0.0.1:1234/v1
- API Key: lm-studio
- Modelo: meta-llama-3.1-8b-instruct
  Funções disponíveis:
- get_langchain_model(): retorna o modelo configurado para uso com LangChain.
- get_openai_client(): retorna o cliente OpenAI para chamadas diretas.
  Isso permite alternar facilmente entre chamadas via LangChain e chamadas diretas ao servidor do LM Studio.

# ⚙️ Criando um ambiente
Utilize os comandos no terminal, dentro da raiz do projeto.
```text
- python -m venv .venv
```

# 🖥️ Selecionando o interpretador
- Ctrl + Shift + P
- Digite: Python: Select Interpreter
- Escolha o Python dentro de .venv
  Se não for criada automaticamente a pasta .vscode/settings.json, crie manualmente com:
  ```text
  {
    "python-envs.pythonProjects": [],
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "python.analysis.typeCheckingMode": "basic",
    "python.defaultInterpreterPath": ".venv/Scripts/python.exe"
  }
  ```

# 📂 Estrutura de Pastas
```text
├── src/         # Código principal (módulos e aulas)
├── data/        # PDFs e arquivos de suporte
├── .venv/       # Ambiente virtual
├── .vscode/     # Configurações do VS Code
├── .gitignore
└── README.md    # Documentação
```

# 📦 Instalação das dependências

Atualize o pip e instale as bibliotecas:
```text
- python.exe -m pip install --upgrade pip

- pip list                             // verificar a lista do pip

- pip install -U langchain-core
- pip install -U langchain-community
- pip install -U langchain-openai
- pip install -U langchain-tools       // para decorators tipo @tools
- pip install -U langgraph
- pip install -U pypdf                 // leitor de pdf
- pip install -U pymupdf               // leitor de pdf
- pip install -U streamlit             // visual para o chat
- pip install -U python-dotenv
- pip install -U requests
- pip install -U rich                  // visual para o terminal
```

# ▶️ Ativando e desativando o ambiente
Utilize os comandos no terminal, dentro da pasta do projeto.

### Ativar
```text
.venv\Scripts\activate
```
### Desativar
```text
deactivate
```
# 📝 Observações
- O projeto mostra a evolução do terminal ao frontend web.
- Cada aula traz um passo incremental na construção do chatbot.
- Quando há PDF carregado, o conteúdo é usado como contexto para as respostas.
- A versão final inclui memória de conversa, permitindo continuidade entre interações.
