# Relatório de Análise de Qualidade de Repositórios Java

## 1. Introdução

Neste relatório, analisamos a qualidade de repositórios open-source desenvolvidos na linguagem Java, correlacionando diversas métricas de qualidade com características do processo de desenvolvimento desses repositórios. A hipótese principal é que repositórios mais populares, maduros e com maior atividade tendem a apresentar melhores atributos de qualidade interna, como menor acoplamento e maior coesão, devido à atenção mais frequente dos contribuidores e processos mais maduros de revisão e manutenção.

## 2. Metodologia

A metodologia aplicada seguiu os seguintes passos:

### 2.1. Seleção de Repositórios
Foram selecionados os 1.000 repositórios Java mais populares no GitHub. A seleção foi baseada no número de estrelas, assumindo que esse critério reflete a popularidade e a relevância dos repositórios para a comunidade.

### 2.2. Métricas de Processo
As métricas de processo analisadas incluem:
- **Popularidade**: número de estrelas no GitHub.
- **Tamanho**: linhas de código (LOC) e linhas de comentários.
- **Atividade**: número de releases.
- **Maturidade**: idade (em anos) do repositório.

### 2.3. Métricas de Qualidade
Para avaliar a qualidade interna dos repositórios, utilizamos a ferramenta de análise estática CK, que gera métricas como:
- **CBO (Coupling Between Objects)**: mede o grau de acoplamento entre classes.
- **DIT (Depth Inheritance Tree)**: mede a profundidade da árvore de herança.
- **LCOM (Lack of Cohesion of Methods)**: mede a falta de coesão entre métodos de uma classe.

### 2.4. Coleta de Dados
As métricas de processo foram coletadas utilizando as APIs REST e GraphQL do GitHub, enquanto as métricas de qualidade foram extraídas por meio da análise estática com a ferramenta CK. O CK gera arquivos .csv que foram sumarizados para realizar as correlações com as características de processo.

Aqui está o relatório em markdown atualizado com base nos dados da planilha enviada. A estrutura segue a lógica das seções de resultados, discussão e conclusão.

# Relatório de Análise de Qualidade de Repositórios Java

## 3. Resultados

### RQ 01: Qual a relação entre a popularidade dos repositórios e suas características de qualidade?

Com base nos dados da planilha, observamos que repositórios mais populares, como o **JavaGuide** (146.018 estrelas) e o **GitHub-Chinese-Top-Charts** (98.958 estrelas), apresentam valores nulos ou muito baixos para as métricas de qualidade (CBO, DIT e LCOM). Esses repositórios são grandes em termos de popularidade, mas alguns não possuem linhas de código disponíveis para análise (LOC = 0). Já repositórios como o **mall** (77.370 estrelas) possuem métricas de qualidade mais detalhadas, com um **CBO mediano** de 3.0 e uma **LCOM média** muito alta (1.110,8), o que pode indicar maior acoplamento e falta de coesão entre os métodos, mesmo sendo populares.

### RQ 02: Qual a relação entre a maturidade dos repositórios e suas características de qualidade?

Os repositórios mais antigos, como o **java-design-patterns** (10 anos de idade) e o **mall** (6 anos de idade), apresentam algumas diferenças interessantes. O **java-design-patterns**, apesar de ser mais antigo, tem métricas de qualidade nulas (CBO, DIT e LCOM), o que pode indicar falta de complexidade no código ou falta de dados para análise. O **mall**, por outro lado, apresenta métricas de qualidade significativas, como uma alta variabilidade em **LCOM**, sugerindo que repositórios mais maduros podem enfrentar desafios em manter a coesão do código ao longo do tempo.

### RQ 03: Qual a relação entre a atividade dos repositórios e suas características de qualidade?

Analisando repositórios com maior número de releases, como o **hello-algo** (8 releases), verificamos que, apesar de ter uma alta atividade, ele não apresenta métricas de qualidade significativas (todos os valores para CBO, DIT e LCOM são nulos). Isso sugere que a atividade por si só pode não estar diretamente correlacionada com uma melhoria na qualidade interna do código, ou que a atividade não resultou em mudanças que impactem as métricas de qualidade analisadas.

### RQ 04: Qual a relação entre o tamanho dos repositórios e suas características de qualidade?

Repositórios maiores, como o **mall** (100.903 linhas de código), apresentam um **CBO mediano** de 3.0 e uma **LCOM média** extremamente alta (1.110,8), sugerindo que projetos maiores podem sofrer com acoplamento elevado entre objetos e falta de coesão entre métodos. Em contraste, repositórios com LOC igual a zero, como o **JavaGuide** e **GitHub-Chinese-Top-Charts**, não apresentam dados para análise, o que pode significar que o tamanho dos repositórios é uma métrica essencial para avaliar a qualidade interna do código.

## 4. Discussão

### Hipóteses

A expectativa inicial era de que repositórios mais populares e maduros apresentariam melhores atributos de qualidade interna, como menor acoplamento e maior coesão. Também esperávamos que repositórios com maior atividade (número de releases) tivessem métricas de qualidade mais otimizadas devido à manutenção e refatoração contínua. Quanto ao tamanho, a hipótese era de que projetos maiores enfrentariam desafios em manter a modularidade e coesão.

### Valores Obtidos

Os resultados obtidos a partir da planilha desafiam algumas das hipóteses. Embora alguns repositórios populares apresentem boas métricas de qualidade, muitos não possuem dados suficientes para avaliação, sugerindo que a popularidade por si só pode não ser indicativa de alta qualidade interna. Projetos mais maduros, como o **mall**, confirmam nossa expectativa de que a maturidade pode aumentar o acoplamento e reduzir a coesão, enquanto a atividade, medida pelo número de releases, não mostrou correlação clara com a qualidade.

Repositórios maiores, como esperado, mostraram-se mais desafiadores em termos de modularidade e coesão, mas a ausência de dados de qualidade em alguns repositórios com zero LOC levantou questões sobre como essas métricas são calculadas e sua disponibilidade em projetos grandes.

## 5. Conclusão

Este laboratório demonstrou que a qualidade dos repositórios open-source Java pode variar consideravelmente, mesmo entre projetos populares e maduros. A popularidade e a atividade não são indicadores claros de boa qualidade interna, e projetos maiores tendem a enfrentar desafios relacionados ao acoplamento e à coesão. As métricas de qualidade calculadas pela ferramenta CK fornecem insights valiosos, mas a falta de dados em alguns repositórios sugere a necessidade de maior cuidado na seleção e análise desses projetos.

Em resumo, repositórios populares podem ter baixa complexidade ou dados insuficientes para análise de qualidade interna. Projetos mais antigos e maiores enfrentam desafios de modularidade, e a atividade contínua não necessariamente se traduz em melhorias significativas nas métricas de qualidade.