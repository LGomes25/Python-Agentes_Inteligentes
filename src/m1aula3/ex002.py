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
        if hasattr(completion, "content"):
            return completion.content
        return completion


# prompt com instrucoes claras para o agente executar
prompt = """
Você executa em um ciclo de Pensamento, Ação, PAUSA, Observação.
No final do ciclo você fornece uma Resposta
Use Pensamento para descrever seus pensamentos sobre a pergunta que foi feita.
Use Ação para executar uma das ações disponíveis - então retorne PAUSA.
Observação será o resultado da execução dessas ações.

Suas ações disponíveis são:

calcular:
ex: calcular: 4 * 7 / 3
Executa um cálculo e retorna o número - usa Python então certifique-se de usar sintaxe de ponto flutuante se necessário

preco_prato:
ex: preco_prato: Feijoada
retorna o preço do prato quando fornecido o nome

Exemplo de sessão:

Pergunta: Quanto custa uma Moqueca?
Pensamento: Devo verificar o preço da Moqueca usando preco_prato
Ação: preco_prato: Moqueca
PAUSA

Você será chamado novamente com isto:

Observação: Uma Moqueca custa R$ 89,90

Você então fornece:

Resposta: Uma Moqueca custa R$ 89,90
""".strip()


def calculate(formula):
    return eval(formula)


def preco_prato(nome):
    if nome == "Feijoada":
        return "Uma Feijoada custa R$ 75,90"
    elif nome == "Moqueca":
        return "Uma Moqueca custa R$ 89,90"
    elif nome == "Picanha":
        return "Uma Picanha custa R$ 129,90"
    else:
        return "Prato não encontrado no cardápio"


known_actions = {"calculate": calculate, "preco_prato": preco_prato}

campeao = Agent(llm, system=prompt)
result = campeao("Quanto custa uma Moqueca?")
print(result)

obs = preco_prato("Moqueca")
print(obs)

response = campeao(f"Observation: {obs}")
print(response)
