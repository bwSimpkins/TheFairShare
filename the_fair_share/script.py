import locale

# Adds commas to the values and rounds decimals
def format_currecy_value(value):
    locale.setlocale(locale.LC_ALL, '')
    return locale.currency(value, symbol=False, grouping=True)

def process_multiple_inputs(inputs):
    try:
        numbers = [float(value) for value in inputs.values()]  # Convert inputs to floats
        total_sum = sum(numbers)  # Calculate sum
        return f"Household Income: ${format_currecy_value(total_sum)}" + "\n hello"
    except ValueError:
        return "Please enter valid numbers."
