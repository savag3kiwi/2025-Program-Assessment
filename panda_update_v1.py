# Importing pandas package
import pandas

# Importing numpy package
import numpy


# lists to hold ticket details
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

print(cheese_frame)

print()
