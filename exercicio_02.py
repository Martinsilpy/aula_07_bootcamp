# Filtrar Dados Acima de um Limite
from typing import List

def filtrar_acima_de(valores: List[float], limite: float) -> List[float]:
    """
    Filtra os valores de uma lista que são maiores que um limite especificado.

    Args:
        valores (List[float]): Uma lista de valores numéricos.
        limite (float): O valor limite para filtrar os valores da lista.

    Returns:
        List[float]: Uma lista contendo os valores que são maiores que o limite especificado.
    """
    resultado = []
    for valor in valores:
        if valor > limite:
            resultado.append(valor)
    return resultado

print(filtrar_acima_de([1, 2, 3, 4, 5], 2)) # [3, 4, 5]

