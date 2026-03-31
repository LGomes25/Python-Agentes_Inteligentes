from src.config import get_langchain_model

# Configuracao do modelo
llm = get_langchain_model(temperature=0.3)


# Criacao de um agente simples
class Agent:
    def __init__(self, llm, system=""):
        self.llm = llm
        self.system = system
        self.messages = []
        if self.system:
            self.messages.append({"role": "system", "content": system})

    def __call__(self, message):
        self.messages.append({"role": "user", "content": message})
        result = self.execute()
        self.messages.append({"role": "assistant", "content": result})
        return result

    def execute(self):
        completion = self.llm.invoke(self.messages)
        return completion


agent = Agent(llm, system="Você é um assistente útil.")
response = agent("Bom dia, como vai?")
print(response)
