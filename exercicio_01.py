# Calcular a média de valores de uma lista
from typing import List

def calcular_media(valores: List[float]) -> float:
    """
    Calcula a média de uma lista de valores.

    Args:
        valores (List[float]): Uma lista de números de ponto flutuante.

    Returns:
        float: A média dos valores fornecidos.

    Raises:
        ZeroDivisionError: Se a lista de valores estiver vazia.
    """
    return sum(valores) / len(valores)

print(calcular_media([1, 2, 3, 4, 5])) # 3.0