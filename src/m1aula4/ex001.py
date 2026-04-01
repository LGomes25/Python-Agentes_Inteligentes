import os

from dotenv import load_dotenv

from src.config import get_langchain_model

_ = load_dotenv()
import operator
from typing import Annotated, TypedDict

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import AnyMessage, HumanMessage, SystemMessage, ToolMessage
from langgraph.graph import END, StateGraph

# Configuracao do modelo
llm = get_langchain_model(temperature=0.3, max_completion_tokens=2048)

# ferramenta de busca na internet
tool = TavilySearchResults(
    max_results=2, tavily_api_key=os.getenv("TAVILY_SEARCH_API_KEY")
)


# criação de uma classe de estado
class AgentState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]


class Agent:

    def __init__(self, model, tools, system=""):
        self.system = system
        graph = StateGraph(AgentState)
        graph.add_node("llm", self.call_openai)
        graph.add_node("action", self.take_action)
        graph.add_conditional_edges(
            "llm", self.exists_action, {True: "action", False: END}
        )
        graph.add_edge("action", "llm")
        graph.set_entry_point("llm")
        self.graph = graph.compile()
        self.tools = {t.name: t for t in tools}
        self.model = model.bind_tools(tools)

    def exists_action(self, state: AgentState):
        result = state["messages"][-1]
        tool_calls = getattr(result, "tool_calls", None)
        return bool(tool_calls)

    def call_openai(self, state: AgentState):
        messages = state["messages"]
        if self.system:
            messages = [SystemMessage(content=self.system)] + messages
        message = self.model.invoke(messages)
        return {"messages": [message]}

    def take_action(self, state: AgentState):
        tool_calls = getattr(state["messages"][-1], "tool_calls", []) or []
        results = []
        for t in tool_calls:
            print(f"Chamando: {t}")
            if (
                not t["name"] in self.tools
            ):  # verificar nome de ferramenta incorreto do LLM
                print("\n ....nome de ferramenta incorreto....")
                result = "nome de ferramenta incorreto, tente novamente"  # instruir LLM a tentar novamente
            else:
                result = self.tools[t["name"]].invoke(t["args"])
                result = str(result)[
                    :2000
                ]  # Truncar o tamanho da resposta para diminuir o contexto para o llm
            results.append(
                ToolMessage(tool_call_id=t["id"], name=t["name"], content=str(result))
            )
        print("De volta ao modelo!")
        return {"messages": results}


prompt = """Você é um assistente de pesquisa inteligente. Use o motor de busca para procurar informações. \
Você pode fazer múltiplas chamadas (juntas ou em sequência). \
Só procure informações quando tiver certeza do que quer. \
Se precisar procurar algumas informações antes de fazer uma pergunta de acompanhamento, você pode fazer isso!
"""

### chamada 1 - busca simples

# abot = Agent(llm, [tool], system=prompt)
# result = abot.graph.invoke({"messages": [HumanMessage(content="Qual é o clima no Rio de Janeiro?")]})
# print("Resultado completo:")
# print(result)
# print("\nResposta final:")
# print(result["messages"][-1].content)

### chamada 2 - busca com multiplas chamadas

query = "Quem ganhou a Copa do Mundo de 2014? Informe o PIB desse país? Responda cada pergunta."
abot = Agent(llm, [tool], system=prompt)
result = abot.graph.invoke({"messages": [HumanMessage(content=query)]})
print(result["messages"][-1].content)
