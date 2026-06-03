Este trabalho pretende resolver um problema real de gestão de projetos: a otimização de fluxos de trabalho e a identificação do caminho crítico em entregas.

A aplicação utiliza todo o fluxo de produção de uma campanha (desde o briefing inicial, passando por design, copy, revisão, aprovação, até o tráfego pago e a análise final de performance) utilizando uma estrutura de Grafo Direcionado. Cada etapa do processo é tratada como um nó, onde o usuário define dinamicamente os prazos entre as tarefas e o nível de impacto de cada entrega.

Para navegar por esse fluxo e encontrar a melhor rota de execução, o sistema implementa três algoritmos de busca:

Busca em Largura (BFS) e Busca em Profundidade (DFS);

Algoritmo A*.
