## Fluxo com LangGraph e ferramentas externas

Nesta atividade, é realizado a adaptacao do fluxo do agente de viagens para que ele seja capaz de fazer mais coisas — como contas de orçamento, verificar a temperatura local, sugerir restaurantes e até estimar o preço de passagens aéreas.

### Siga as instruções

1. Analise o grafo criado na aula e identifique onde as novas funções podem ser inseridas.
2. Crie novas tools (funções Python) para cada tipo de tarefa adicional. Exemplos:
   - calcular_orcamento(destino, dias, diaria)
   - ver_temperatura(destino)
   - sugerir_restaurantes(destino)
   - preco_passagens(destino)
3. Atualize o dicionário de ferramentas do agente para incluir as novas ações.
4. Teste consultas que envolvam múltiplas etapas, como:
   - Monte um roteiro para Paris, incluindo orçamento total e sugestões de restaurantes.
5. Observe o comportamento do agente e como ele usa as ferramentas criadas.

## Descricao do arquivo

**ex001** -> Neste exemplo, construímos um planejador de viagens interativo utilizando LangGraph e LangChain, integrado ao modelo da OpenAI e à ferramenta de busca Tavily. O agente é estruturado como um grafo de estados (StateGraph), onde cada nó representa uma etapa do ciclo de planejamento: geração de queries, busca de informações, elaboração do plano inicial, coleta de feedback do usuário e revisões sucessivas.
A classe AgentState define o estado compartilhado do grafo, armazenando os interesses do usuário, as queries geradas, os resultados coletados, o plano atual e o feedback recebido. O nó query_node invoca o modelo de linguagem com saída estruturada em Pydantic para produzir queries específicas de busca. O nó search_node utiliza o TavilyClient para consultar informações relevantes e acumular os resultados. Em seguida, o nó generate_result_node combina os dados coletados com um prompt detalhado para gerar um plano de viagem completo e personalizado.
O ciclo é enriquecido pelo nó user_feedback_node, que imprime o plano no terminal e solicita ao usuário sugestões de alteração ou aprovação. Caso haja feedback, o nó revision_node revisa o planejamento com base nas observações, mantendo a estrutura organizada e iterando até três vezes. A função should_continue controla a transição condicional entre feedback, revisão e término do fluxo.
O grafo é compilado com checkpoint em memória e pode opcionalmente gerar uma visualização em PNG. O agente é testado com um exemplo de viagem ao Japão, incluindo interesses como surf, esportes radicais e cerveja artesanal, demonstrando a capacidade de gerar queries, buscar informações externas, elaborar um plano inicial e refiná-lo iterativamente com participação humana.
👉 Em resumo, este agente mostra como combinar LangChain + LangGraph + Tavily + OpenAI para criar um fluxo de planejamento de viagens interativo, onde o usuário participa ativamente do processo de refinamento até chegar a um plano final satisfatório.

## Para Rodar

```
python -m src.m1aula7.ex001
```
