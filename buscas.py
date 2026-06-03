from collections import deque


def bfs(inicio, fim):
    fila = deque([inicio])
    visitados = [] 
    
    while fila:
        no = fila.popleft()
        
        if no not in visitados:
            visitados.append(no)
            
            
            for vizinho, _ in no.vizinhos:
                if vizinho not in visitados and vizinho not in fila:
                    fila.append(vizinho)
                    
    return [n.nome for n in visitados]


def dfs(inicio, fim, visitados=None):
    if visitados is None:
        visitados = []
        
    if inicio not in visitados:
        visitados.append(inicio)
        
        
        for vizinho, _ in inicio.vizinhos:
            dfs(vizinho, fim, visitados)
            
    return [n.nome for n in visitados]

def a_estrela(inicio, fim):
    fila_prioridade = [(inicio.heuristica, 0, id(inicio), [inicio])]
    
    prazos_acumulados = {inicio:0}
    
    while fila_prioridade:
        fila_prioridade.sort(key=lambda x: x[0])
        
        peso, prazo_dias, _, caminho = fila_prioridade.pop(0)
        no_atual = caminho[-1]
        
        if no_atual == fim:
            return [no.nome for no in caminho], prazo_dias
        
        for vizinho, prazo_aresta in no_atual.vizinhos:
            novo_prazo_dias = prazo_dias + prazo_aresta
            
            if vizinho not in prazos_acumulados or novo_prazo_dias < prazos_acumulados[vizinho]:
                prazos_acumulados[vizinho] = novo_prazo_dias
                
                novo_peso = novo_prazo_dias + vizinho.heuristica
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                
                fila_prioridade.append((novo_peso, novo_prazo_dias, id(vizinho), novo_caminho))
                
    return None, 0           
        

