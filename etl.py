import csv

path_arquivo = 'vendas.csv'

def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:
       
    lista = []   
    with open(nome_do_arquivo_csv, mode='r', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for linha in leitor_csv:
            lista.append(linha)
    return lista


def flitrar_produtos_nao_entregues(lista: list[dict]) -> list[dict]:
    lista_com_produtos_filtrados = []
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados


def somar_valores_dos_produtos(lista_com_produtos_filtrados: list[dict]) -> int:
    valor_total = 0    
    for produto in lista_com_produtos_filtrados:
        valor_total += int(produto.get("price"))    
    return valor_total 