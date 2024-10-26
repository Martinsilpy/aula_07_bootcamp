from typing import List

# Encontrar Valores Ausentes em um Sequência
def valores_ausentes(valores: List[int]) -> List[int]:
    """
    Encontra valores ausentes em uma sequência de inteiros.

    Args:
        valores (List[int]): Uma lista de inteiros.

    Returns:
        List[int]: Uma lista de valores ausentes.
    """
    return [valor for valor in range(min(valores), max(valores) + 1) if valor not in valores]

print(valores_ausentes([1, 2, 3, 4, 6, 7, 8, 10])) # [5, 9]
