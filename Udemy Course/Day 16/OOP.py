# import another_module

# print(another_module.my_var)

# from turtle import Turtle, Screen

# timmy = Turtle()

# print(timmy)
# timmy.shape("turtle")
# timmy.color("black")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

import pretty_tables

headers = ['ID', 'Name', 'Occupation', 'Employed']
rows = [
    [1, 'Justin', 'Software Engineer', True],
    [2, 'Misty', 'Receptionist', False],
    [3, 'John', None, False],
]

# Add optional custom colors to each column
colors = [
    pretty_tables.Colors.red,
    pretty_tables.Colors.green,
    pretty_tables.Colors.blue,
    pretty_tables.Colors.purple,
]

# Generate the pretty table output
table = pretty_tables.create(
    headers=headers,
    rows=rows,
    empty_cell_placeholder='No data',  # Optional: override the default `None` with a custom string
    colors=colors,  # Optional: mutually exclusive with `truthy`
    # truthy=3,  # Optional: integer of the column you want to check for truthy values on, mutually exclusive with `colors`
)

print(table)