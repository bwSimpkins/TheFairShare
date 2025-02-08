def process_multiple_inputs(inputs):
    try:
        numbers = [float(value) for value in inputs.values()]  # Convert inputs to floats
        total_sum = sum(numbers)  # Calculate sum
        return f"Sum of inputs: {total_sum}"
    except ValueError:
        return "Please enter valid numbers."
