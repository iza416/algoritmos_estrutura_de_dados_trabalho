class Tarefa: 
    def __init__(self, nome, impacto):
        self.nome = nome
        self.impacto = impacto
        
        self.heuristica = 1 / impacto if impacto > 0 else 99
        self.vizinhos = []
        
    def adicionar_aresta(self, vertice, peso):
        self.vizinhos.append((vertice, peso)) 