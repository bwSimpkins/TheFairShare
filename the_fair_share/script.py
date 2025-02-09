import locale

# Adds commas to the values and rounds decimals
def format_currecy_value(value):
    locale.setlocale(locale.LC_ALL, '')
    return locale.currency(value, symbol=False, grouping=True)


# Calculates the percent of each person's income towards the household income
def percent_of_household(incomes):
    percentages = []
    for income in incomes:
        percentages.append((income / sum(incomes)) * 100)
    return percentages


def split_dict(input_dict, keys_to_split):
    """Splits a dictionary into two based on specified keys.

    Args:
        input_dict (dict): The dictionary to split.
        keys_to_split (list): A list of keys to extract into a new dictionary.

    Returns:
        tuple: A tuple containing two dictionaries:
            - The first dictionary contains the key-value pairs where the keys are in keys_to_split.
            - The second dictionary contains the remaining key-value pairs.
    """
    dict1 = {k: input_dict[k] for k in keys_to_split if k in input_dict}
    dict2 = {k: input_dict[k] for k in input_dict if k not in keys_to_split}
    return dict1, dict2


# Format the percent of household incomes into a string
def format_percent_of_household(percentage_income, output_string):
    iterator = 1
    for income in percentage_income:
        output_string.append("Individual " + str(iterator) + " makes " + str(income) + "% of household income")
        iterator += 1

def process_multiple_inputs(inputs):
    try:
        # Split keys into incomes and the rest of the inputs
        keys_to_move = ['income1', 'income2', 'income3', 'income4', 'income5', 'income6', 'income7', 'income8', 'income9', 'income10']
        income_dict, rest_dict = split_dict(inputs, keys_to_move)

        # Calculate sum of the incomes
        incomes = [float(value) for value in income_dict.values()]  # Convert inputs to floats
        household_income = sum(incomes)  # Calculate sum
        output_string = [f"Household Income: ${format_currecy_value(household_income)}"] # Adds to the output list

        # Calculate income percentages
        percentage_income = percent_of_household(incomes) # Get percentage of each income
        format_percent_of_household(percentage_income, output_string)

        # Get rent info
        rent = [float(value) for value in rest_dict.values()]  # Convert inputs to floats
        rent = sum(rent)
        output_string.append("Rent: $" + format_currecy_value(rent))

        return "\n".join(output_string)
    except ValueError:
        return "Please enter valid numbers."
