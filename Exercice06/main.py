# Fonction calculate_average

def calculate_average(numbers):
    """
    Cette fonction calcule la moyenne d'une liste de nombres.
    Args:
        numbers (List[int]): Liste de nombres
    Returns:
        float: La moyenne des nombres
    """

    if not numbers:
        return 0

    total = sum(numbers)
    return total / len(numbers)


# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("La moyenne est :", average)
