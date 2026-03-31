## Construindo seu primeiro agente ReAct

Nesta atividade, será implementado um agente simples utilizando o padrão ReAct (Reasoning + Acting).

### Siga as instruções

Replique o código apresentado na aula, criando a classe Agent:

- Crie duas funções de ação novas — por exemplo, calcular_idade() e converter_moeda().
- Atualize o dicionário known_actions para incluir essas novas funções.
- Faça perguntas ao agente que o obriguem a pensar, agir e observar — por exemplo:

```
 “Quantos anos tem alguém que nasceu em 1995?”
 “Quanto é 10 dólares em reais, considerando que 1 USD = 5,00 BRL?”
```

- Teste o comportamento e observe se o fluxo ReAct está funcionando corretamente.

## Descricao do arquivo

**teste_inicial** -> chamada simples e direta ao modelo de llm

**ex001** -> Aqui definimos uma classe simples que armazena o estado da conversa e injeta a instrução de sistema apenas uma vez. Ao chamar a instância com novas mensagens, o agente delega à API da OpenAI, atualiza o histórico e devolve a última resposta — exatamente o padrão ReAct reduzido.

**ex002** -> Neste exemplo, utilizou-se a base anterior, só que com um prompt elaborado, baseado no ReAct. Criamos a instância `campeao` com o prompt, garantindo que toda nova conversa já comece com as regras de pensamento/ação disponíveis. Rodamos `campeao` com uma pergunta simples para observar como o modelo gera **Pensamento/Ação/PAUSA**. Depois, imitamos o retorno de uma ferramenta manual(preço da Moqueca) e mostramos ao agente via `Observation`, forçando-o a concluir com a `Resposta` final do ciclo. A lista de `known_actions` funciona como o inventário de ferramentas que o agente pode acionar durante o ciclo ReAct. Cada item associa um nome textual a uma função Python concreta, permitindo que o modelo “planeje” ações em linguagem natural e o ambiente execute-as de fato.

**ex003** -> Neste exemplo, partimos da base construída em ex002 e acrescentamos um loop automático de interação. A ideia foi transformar o agente em algo mais autônomo, capaz de seguir o ciclo completo Pensamento → Ação → PAUSA → Observação → Resposta sem depender de chamadas manuais para cada etapa.
A função query recebe uma pergunta inicial e roda em ciclos, limitados por max_turns para evitar loops infinitos. Em cada ciclo, o agente é chamado com o próximo prompt, a resposta é analisada linha a linha para detectar ações e, caso existam, o código procura a função correspondente em known_actions. Essa função é executada em Python e o resultado é devolvido ao agente como uma nova entrada de Observação, permitindo que ele continue o raciocínio com base nesse retorno.
Se não houver mais ações, o loop encerra e o agente fornece a resposta final. Dessa forma, o ex003 representa a evolução natural do ex002: em vez de apenas simular manualmente uma observação, o agente agora consegue detectar ações, executar ferramentas e incorporar observações automaticamente. Isso aproxima ainda mais o comportamento do padrão ReAct, permitindo que o modelo planeje em linguagem natural e o ambiente execute de fato, em ciclos sucessivos até chegar à resposta correta.

**atividade_pratica** -> Esse código é uma implementação enxuta do padrão ReAct, voltada apenas para duas funções: calcular idade e converter valores em dólares para reais. Ele define um agente simples que mantém o histórico da conversa e injeta um prompt de sistema com instruções claras sobre como seguir o ciclo Pensamento → Ação → PAUSA → Observação → Resposta. As ações disponíveis são mapeadas em known_actions, associando nomes textuais às funções Python concretas. O loop query automatiza a interação: recebe uma pergunta inicial, chama o modelo, identifica se há alguma ação a executar, roda a função correspondente e devolve o resultado como observação para o modelo continuar. Se não houver mais ações, ou se o modelo já produzir uma linha de resposta final, o ciclo é encerrado. Dessa forma, o código permite que o modelo planeje em linguagem natural e o ambiente execute cálculos reais de idade ou conversão de moeda até chegar à resposta correta.

## Para Rodar

```
python -m src.m1aula3.teste_inicial
python -m src.m1aula3.ex001
python -m src.m1aula3.ex002
python -m src.m1aula3.ex003
python -m src.m1aula3.atividade_pratica

```
