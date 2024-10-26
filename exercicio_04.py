from typing import List

# Converter Celsius para Fahrenheit em uma lista
def celsius_para_fahrenheit(valores: List[float]) -> List[float]:
    """
    Converte uma lista de valores de Celsius para Fahrenheit.

    Args:
        valores (List[float]): Uma lista de valores em Celsius.

    Returns:
        List[float]: Uma lista de valores convertidos para Fahrenheit.
    """
    return [valor * 9/5 + 32 for valor in valores]

print(celsius_para_fahrenheit([0, 10, 20, 30, 40, 50])) # [32.0, 50.0, 68.0, 86.0, 104.0, 122.0]

