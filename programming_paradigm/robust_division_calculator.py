def safe_divide(numerator, denominator):
    # Convert inputs to floats (catch invalid numeric input)
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    # Perform the division (catch division by zero)
    try:
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

