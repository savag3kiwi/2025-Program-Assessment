# Importing pandas package
import pandas


# lists to hold ticket details
all_cheese = ["Colby", "Mozzarella", "Cheddar", "Gouda", "Brie",
              "Manchego", "Roquefort", "Parmigiano Reggiano",
              "Époisses de Bourgogne", "Pule Cheese"]
all_cheese_costs = [20, 30, 35, 40, 60, 80, 100, 150, 200, 300]
# all_surcharges = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    'Cheese': all_cheese,
    'Cheese Price': all_cheese_costs,
    # 'Surcharge': all_surcharges
}

# create dataframe / table from dictionary
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Calculate the total payable for each ticket
mini_movie_frame['Total'] = mini_movie_frame['Ticket Price']  # + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# Work out total paid and total profit...
total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

print(mini_movie_frame)
print()
print(f"Total Paid: ${total_paid:.2f}")
print(f"Total Profit: ${total_profit:.2f}")
