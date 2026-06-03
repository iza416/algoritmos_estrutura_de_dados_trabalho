
from grafo import Tarefa
import buscas

def criar_fluxo_agencia():
    print("\n--- CONFIGURAÇÃO DOS IMPACTOS (1 a 5) ---")
    briefing = Tarefa("Briefing", int(input("Impacto do Briefing: ")))
    design = Tarefa("Design do Layout", int(input("Impacto do Design: ")))
    copy = Tarefa("Redação da Copy", int(input("Impacto da Redação: ")))
    revisao = Tarefa("Revisão Interna", int(input("Impacto da Revisão Interna: ")))
    cliente = Tarefa("Aprovação do Cliente", int(input("Impacto da Aprovação do Cliente: ")))
    programacao = Tarefa("Programação e Montagem", int(input("Impacto da Programação: ")))
    trafego = Tarefa("Configuração de Tráfego", int(input("Impacto do Tráfego: ")))
    ar = Tarefa("Disparar Campanha", int(input("Impacto de Disparar campanha: ")))
    performance = Tarefa("Análise de Performance", int(input("Impacto da Performance: ")))

    print("\n--- CONFIGURAÇÃO DOS PRAZOS (DIAS) ---")
    
    briefing.adicionar_aresta(copy, int(input("Prazo do Briefing para Redação: ")))
    briefing.adicionar_aresta(design, int(input("Prazo do Briefing para Design: ")))
    
    
    copy.adicionar_aresta(revisao, int(input("Prazo da Redação para Revisão: ")))
    design.adicionar_aresta(revisao, int(input("Prazo do Design para Revisão: ")))
    
    
    revisao.adicionar_aresta(cliente, int(input("Prazo da Revisão para o Cliente: ")))
    
    
    cliente.adicionar_aresta(programacao, int(input("Prazo do Cliente para Programação de Posts: ")))
    cliente.adicionar_aresta(trafego, int(input("Prazo do Cliente para Configurar Tráfego: ")))
    
    
    programacao.adicionar_aresta(ar, int(input("Prazo da Programação para o ar: ")))
    trafego.adicionar_aresta(ar, int(input("Prazo do Tráfego para o ar: ")))
    
    
    ar.adicionar_aresta(performance, int(input("Prazo do veiculação para Análise de Performance: ")))

    return briefing, performance


def main():
    print("=== GERENCIADOR DE DEMANDAS ===")
    inicio, fim = criar_fluxo_agencia()
    
    while True:
        print("\n================ Escolha uma opção ================")
        print("1. Executar Busca em Largura (BFS - Cega)")
        print("2. Executar Busca em Profundidade (DFS - Cega)")
        print("3. Executar Busca A*")
        print("4. Reconfigurar Prazos e Impactos")
        print("5. Sair")
        
        opcao = input("Escolha o algoritmo para rodar o grafo: ")
        
        if opcao == "1":
            resultado = buscas.bfs(inicio, fim)
            if resultado:
                print("\n-> Ordem de Visita BFS:\n", " ➔ ".join(resultado))
            else:
                print("\n[ERRO] Nenhum caminho encontrado.")
        elif opcao == "2":
            resultado = buscas.dfs(inicio, fim)
            if resultado:
                print("\n-> Ordem de Visita DFS:\n", " ➔ ".join(resultado))
            else:
                print("\n[ERRO] Nenhum caminho encontrado.")
        elif opcao == "3":
            caminho, custo_total = buscas.a_estrela(inicio, fim)
            if caminho:
                print("\n-> Melhor Caminho Otimizado pelo A*:\n", " ➔ ".join(caminho))
                print(f"-> Custo Total de Prazo do Caminho Crítico: {custo_total} dias.")
            else:
                print("\n[ERRO] Nenhum caminho encontrado.")
        elif opcao == "4":
            inicio, fim = criar_fluxo_agencia()
        elif opcao == "5":
            print("Fechando o sistema.")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()