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


# Format the percent of household incomes into a string
def format_percent_of_household(percentage_income, output_string):
    iterator = 1
    for income in percentage_income:
        output_string.append("Individual " + str(iterator) + " makes " + str(income) + "% of household income")
        iterator += 1

def process_multiple_inputs(inputs):
    try:
        incomes = [float(value) for value in inputs.values()]  # Convert inputs to floats
        household_income = sum(incomes)  # Calculate sum
        output_string = [f"Household Income: ${format_currecy_value(household_income)}"] # Adds to the output list
        percentage_income = percent_of_household(incomes) # Get percentage of each income
        format_percent_of_household(percentage_income, output_string)
        return "\n".join(output_string)
    except ValueError:
        return "Please enter valid numbers."
