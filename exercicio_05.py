from typing import List

# Calcular o desvio padrão de uma lista
def desvio_padrao(valores: List[float]) -> float:
    """
    Calcula o desvio padrão de uma lista de valores.

    Args:
        valores (List[float]): Uma lista de valores numéricos.

    Returns:
        float: O desvio padrão dos valores fornecidos.
    """
    n = len(valores)
    media = sum(valores) / n
    return (sum((valor - media) ** 2 for valor in valores) / n) ** 0.5

print(desvio_padrao([1, 2, 3, 4, 5])) # 1.4142135623730951