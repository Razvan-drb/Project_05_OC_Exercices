

## Écrivez votre code ici !
def input_number():
    while True:
        user_input = input('Enter a number (integer or float): ')
        try:
            number = float(user_input)
            return number
        except ValueError:
            print("Invalid input. Please enter a valid integer or float.")

def square(num):
    """
    Cette fonction prend un nombre en entrée et renvoie son carré.
    Args:
        num (int or float): Un nombre
    Returns:
        int or float: Le carré du nombre
    """
    if num is not None:
        return num ** 2
    else:
        return None

num_to_square = input_number()

print(f"The square of {num_to_square} is: {square(num_to_square)}")
