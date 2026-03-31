from src.config import get_langchain_model

# Configuracao do modelo
llm = get_langchain_model(temperature=0.3)

# testes iniciais para chamada ao modelo
messages = [{"role": "user", "content": "Bom dia, como vai?"}]
response = llm.invoke(messages)
print(response.content)
