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

## 3. Resultados

### RQ 01: Qual a relação entre a popularidade dos repositórios e suas características de qualidade?


### RQ 02: Qual a relação entre a maturidade dos repositórios e suas características de qualidade?


### RQ 03: Qual a relação entre a atividade dos repositórios e suas características de qualidade?


### RQ 04: Qual a relação entre o tamanho dos repositórios e suas características de qualidade?


## 4. Discussão

### Hipóteses


### Valores Obtidos



## 5. Conclusão
