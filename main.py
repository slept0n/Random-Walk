import matplotlib.pyplot as plt

plt.style.use('seaborn')


input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()

ax.scatter(2, 4, c='orange', s=200)

ax.plot(input_values, squares, linewidth=3)

# set chart title and label axes
ax.set_title("Square Numbers", fontsize=14)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.savefig('squares_plot.png', bbox_inches='tight')


plt.show()