#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


FILE = "skostr_hoyde.xlsx"


def least_squares(xs, ys):
    """Create linear function based on the least square method."""
    # Get the average of each sequence
    x_avg = sum(xs) / len(xs)
    y_avg = sum(ys) / len(ys)

    # Compute top part of fraction
    top = 0
    for x, y in zip(xs, ys):
        top += (x - x_avg) * (y - y_avg)

    # Compute bottom part of fraction
    bot = sum([(x - x_avg) * (x - x_avg) for x in xs])

    # Compute constants
    b = top / bot
    a = y_avg - b * x_avg

    # Create and return function based on the new constants
    return lambda x: a + b * x


# Get data from excel file
df = pd.read_excel(FILE)

# Get the columns from dataframa as lists
cat1, cat2 = df.columns
xs = list(df[cat1])
ys = list(df[cat2])

# Use linspace in scatterplot to approximate a continuous line
x = np.linspace(30, 50, 200)
y = least_squares(xs, ys)(x)

df2 = pd.DataFrame({"x": x, "y": y})

# Plot regression line
ax = df2.plot.scatter(
    x="x",
    y="y",
    s=0.1,
    c="black",
)

# Plot scatter data
df.plot.scatter(
    x="skostr",
    y="hoyde",
    marker="x",
    ax=ax,
)

# Save to PDF
# plt.savefig(fname="plot.pdf", format="pdf")

# Display to screen
plt.show()