## Fluxo com LangGraph e ferramentas externas

Nesta atividade, será realizado as atividade de criar, orquestrar e executar agentes usando grafos de execução, tornando o desenvolvimento muito mais simples e visual!

### Siga as instruções

1. Replique o código apresentado na aula que usa LangGraph atrelado à ferramenta externa Tavily
2. Teste outras perguntas como:
   - Qual a capital do Canadá?
   - Quem ganhou a Copa do Mundo de 2014?

## Descricao do arquivo

**ex001** -> Neste exemplo, construímos um agente de pesquisa autônomo utilizando LangGraph e LangChain, integrado a um modelo local via LM Studio e à ferramenta de busca Tavily. O agente é estruturado como um grafo de estados (StateGraph), onde cada nó representa uma etapa do ciclo de raciocínio: o nó llm invoca o modelo de linguagem e o nó action executa as ferramentas disponíveis. A transição entre os nós é controlada pela função exists_action, que verifica se o modelo gerou chamadas de ferramenta (tool_calls) na última mensagem — caso positivo, o fluxo segue para action; caso contrário, encerra no END.
A classe AgentState define o estado compartilhado do grafo, acumulando todas as mensagens trocadas ao longo do ciclo via operator.add. A classe Agent encapsula toda a lógica: inicializa o grafo, vincula as ferramentas ao modelo via bind_tools e expõe o método call_openai para invocar o LLM e take_action para executar as ferramentas e devolver os resultados como ToolMessage. O resultado do Tavily é truncado em 2000 caracteres para evitar sobrecarga de contexto no modelo local.
O agente é testado em duas situações: uma busca simples sobre o clima no Rio de Janeiro e uma consulta encadeada sobre o vencedor da Copa do Mundo e o PIB do país campeão, demonstrando a capacidade do agente de realizar múltiplas chamadas sequenciais à ferramenta antes de formular a resposta final.

## Para Rodar

```
python -m src.m1aula4.ex001
```
