import re
from datetime import date

from src.config import get_langchain_model

# Configuração do modelo
llm = get_langchain_model(temperature=0.3)


# Agente simples
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


# Prompt com instruções claras
prompt = """
Você executa em um ciclo de Pensamento, Ação, PAUSA, Observação.
No final do ciclo você fornece uma Resposta.
Use Pensamento para descrever seus pensamentos sobre a pergunta que foi feita.
Use Ação para executar uma das ações disponíveis - então retorne PAUSA.
Observação será o resultado da execução dessas ações. 
IMPORTANTE: Nunca invente idades ou valores de conversão.
IMPORTANTE: Sempre use as funções fornecidas (ano_atual,calcular_idade, conversor_moeda).
IMPORTANTE: Sempre use exatamente o valor fornecido na Observação como resposta final.
IMPORTANTE: Nunca repita a mesma ação com o resultado da Observação.

Suas ações disponíveis são:

ano_atual:
ex: ano_atual:1900
Retorna o ano atual do dia em que a consulta é feita. use esta função sempre que precisar saber qual o ano vigente.

conversor_moeda:
ex: conversor_moeda: 100
Converte o valor em dólares para reais usando a taxa fixa de 5.0

calcular_idade:
ex: calcular_idade: 1920
Retorna a idade de uma pessoa com base no ano de nascimento fornecido. Use a funçãp calcular_idade(ano_nascimento) que retorna a idade diretamente calculada.
""".strip()


# Funções disponíveis
def ano_atual():
    return date.today().year


def calcular_idade(ano_nascimento):
    ano_atual = date.today().year
    nascimento = int(ano_nascimento)
    idade = ano_atual - nascimento
    return f"Quem nasceu em {nascimento} hoje tem {idade} anos"


def conversor_moeda(montante):
    dolares = float(montante)
    conversao = dolares * 5.0
    return f"A conversão de {dolares} dólares é R$ {conversao:.2f}"


known_actions = {
    "calcular_idade": calcular_idade,
    "conversor_moeda": conversor_moeda,
    "ano_atual": ano_atual,
}

# Regex para capturar ações
action_re = re.compile(r"^Ação: (\w+): (.*)$")


# Loop de interação
def query(question, max_turns=8):
    i = 0
    bot = Agent(llm, system=prompt)
    next_prompt = question
    while i < max_turns:
        i += 1
        result = bot(next_prompt)
        print(result)

        matches = []
        for line in result.split("\n"):
            m = action_re.match(line.strip())
            if m:
                matches.append(m)

        print("Ações detectadas:", matches)

        if matches:
            action, action_input = matches[0].groups()
            if action not in known_actions:
                raise Exception(f"Ação desconhecida: {action}: {action_input}")
            print(f" -- executando {action} {action_input}")
            observation = known_actions[action](action_input)
            print("Observação:", observation)
            next_prompt = f"Observação: {observation}"
        else:
            return


# Exemplo de uso

question = "Quantos anos tem alguém que nasceu em 1976?"

# question = "Quanto é 125 dólares em reais"

query(question)
