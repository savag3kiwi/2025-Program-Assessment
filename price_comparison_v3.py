import pandas
import numpy


# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"


def string_check(question, valid_ans_list=('yes', 'no'),
                 num_letters=1):
    """Checks that users enter the full word
    or the first letter of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire world
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


def instructions():
    make_statement("Instructions", "ℹ️")

    print('''
    
For each buyer enter ...
- budget
- name of the cheese

The program will record the purchases and calculate the cost.

Users can buy multiple cheeses or enter the 
exit code ('xxx'), and the program will end

It will finally show an itemised list of all the purchases and will save it
to a writing file

    ''')


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.")


def int_check(question, low, high):
    """Checks users enter an integer between two values"""

    error = f"Oops - please enter an integer between {low} and {high}."

    while True:

        try:
            # Change the response to an integer and check that it's more than zero
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def currency(x):
    """Formats numbers as currency ($#.##)"""
    return "${:.2f}".format(x)


# Main Routine goes here

# Initialise cheese numbers
MAX_SPEND = 600
budget = 0

# lists to hold cheese details
all_cheese = ["Colby", "Mozzarella", "Cheddar", "Gouda", "Brie",
              "Manchego", "Roquefort", "Parmigiano Reggiano",
              "Époisses de Bourgogne", "Pule Cheese"]
all_cheese_costs = [20, 30, 35, 40, 60, 80, 100, 150, 200, 300]

cheese_dict = {
    'Cheese': all_cheese,
    'Cheese Price': all_cheese_costs,
}

# create dataframe / table from dictionary
cheese_frame = pandas.DataFrame(cheese_dict)

# Rearranging index
cheese_frame.index = numpy.arange(1, len(cheese_frame) + 1)

# Program main heading
print(make_statement("The Online Cheese Market", "🧀"))

# Ask user for their name (and check it's not blank)
print()
name = not_blank("Name: ")

# Ask user if they want to see the instructions
# display them if necessary
print()
want_instructions = string_check(f"Hi {name}, do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()

# Ask for the users budget
budget = int_check("What is your budget (Maximum budget of $600)? ", 20, 600)

print(f"Your budget is ${budget}")
print()

# set purchased cheeses to none
purchased_cheese = []
purchased_prices = []

# import list of cheeses
cheese_string = cheese_frame.to_string(index=False)

# Loop to get name, age and payment details
while budget <= MAX_SPEND:

    print()

    # Display menu items
    print("Here is a list of Cheeses you can choose from:")
    print(cheese_frame)
    print()

    # Prompt user to select a row from the index
    try:
        # ask user for their choice
        choice = int_check("Choose your cheese with the number of the row: ", 1, 10)

        selected_row = all_cheese[choice - 1]
        cheese_price = all_cheese_costs[choice - 1]

        if budget >= cheese_price:
            budget -= cheese_price

            purchased_cheese.append(selected_row)
            purchased_prices.append(cheese_price)

            # display user choice
            print(f"You selected {selected_row}, costing ${cheese_price} ")
            print(f"Your new budget is ${budget} ")
            print()

        else:
            print(f"Sorry, the {selected_row} costing {cheese_price} "
                  f"is above your current budget of ${budget}. Please try again.")
            continue

        repurchase = string_check("Would you like to purchase another Cheese? ")

        if repurchase == "no":
            break

        else:
            print("Invalid number. Please enter a number 1-10")

    except ValueError:
        print("Please enter a valid number")

# End of Loop

# Calculate the total payable for each ticket
cheese_frame['Total'] = cheese_frame['Cheese Price']
cheese_frame['Profit'] = cheese_frame['Cheese Price'] - 5

# Work out total paid and total profit...
total_paid = cheese_frame['Total'].sum()
total_profit = cheese_frame['Profit'].sum()

# choose random winner...
# winner = random.choice(all_cheese)

# find index of winner (ie: position in list)
# winner_index = all_cheese.index(winner)

# retrieve Winner Ticket Price and Profit (so we can adjust
# profit numbers so that the winning ticket is excluded)
# ticket_won = cheese_frame.at[winner_index, 'Total']
# profit_won = cheese_frame.at[winner_index, 'Profit']

# Currency Formatting (uses currency function)
add_dollars = ['Cheese Price', 'Total', 'Profit']
for var_item in add_dollars:
    cheese_frame[var_item] = cheese_frame[var_item].apply(currency)

# Output cheese frame without index
# cheese_string = cheese_frame.to_string(index=False)

total_paid_string = f"Total Paid: ${total_paid:.2f}"
total_profit_string = f"Total Profit: ${total_profit:.2f}"

# winner announcement
# lucky_winner_string = (f"The lucky winner is {winner}. "
# f"Their ticket worth ${ticket_won:.2f} is free!")
# final_total_paid_string = f"Total Paid is now ${total_paid - ticket_won:.2f}"
# final_profit_string = f"Total Profit is now ${total_profit - profit_won:.2f}"

# if budget == MAX_SPEND:
# num_sold_string = make_statement(f"You have spent too much "
# f"({MAX_SPEND})", "-")
# else:
# num_sold_string = make_statement(f"Your budget is {budget} / "
# f"{MAX_SPEND}.", "-")

# Additional strings / Headings
# heading_string = make_statement("Online Cheese Store", "=")
# ticket_details_heading = make_statement("Ticket Details", "-")
# raffle_heading = make_statement("--- Raffle Winner ---", "-")
# adjusted_sales_heading = make_statement("Adjusted Sales & Profit",
# "-")
# adjusted_explanation = (f"We have given away a ticket worth ${ticket_won:.2f} which means \nour"
# f"sales have decreased by ${ticket_won:.2f} and our profit \n "
#  f"decreased by ${profit_won:.2f}")

# List of strings to be outputted / written to file
# to_write = [heading_string, "\n",
# ticket_details_heading,
# cheese_string, "\n",
# total_paid_string,
# total_profit_string, "\n",
# raffle_heading,
# lucky_winner_string, "\n",
# adjusted_sales_heading,
# adjusted_explanation, "\n",
# final_total_paid_string,
# final_profit_string, "\n",
# num_sold_string]

# Print Area
# print()
# for item in to_write:
# print(item)

# create file to hold data (add .txt extension)
# file_name = "price_comparison_ticket_details"
# write_to = f"{file_name}.txt"

# text_file = open(write_to, "w+")

# write the item to file
# for item in to_write:
# text_file.write(item)
# text_file.write("\n")
