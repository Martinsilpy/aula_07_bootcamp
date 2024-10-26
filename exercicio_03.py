from typing import List

# Contar valores único em uma lista
def contar_unicos(valores: List[float]) -> int:
    """
    Conta a quantidade de valores únicos em uma lista.

    Args:
        valores (List[float]): Uma lista de valores numéricos.

    Returns:
        int: A quantidade de valores únicos na lista fornecida.
    """
    return len(set(valores))

print(contar_unicos([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])) # 5