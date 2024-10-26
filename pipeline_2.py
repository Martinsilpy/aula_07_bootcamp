from etl import ler_csv, flitrar_produtos_nao_entregues, somar_valores_dos_produtos

path_arquivo = 'vendas.csv'

lista_de_produtos = ler_csv(path_arquivo)
produtos_entregues = flitrar_produtos_nao_entregues(lista_de_produtos)

print(produtos_entregues)