def decimal_to_hexadecimal(decimal_number):
    """
    Convert a decimal number to hexadecimal.
    
    :param decimal_number: Non-negative integer
    :return: Hexadecimal representation as a string
    :raises ValueError: If the number is negative
    """
    if decimal_number < 0:
        raise ValueError("The number should be a non-negative integer.")
    return hex(decimal_number)[2:]


if __name__ == "__main__":
    try:
        number = int(input("Enter a decimal number: "))
        hex_value = decimal_to_hexadecimal(number)
        print(f"Hexadecimal: {hex_value.upper()}")
    except ValueError as e:
        print(e)