import matplotlib.pyplot as plt

# Generate some data to display
t = range(0, 20)
s = range(30, 10, -1)

# Set up the grid of subplots to be 2 by 2
fig, axs = plt.subplots(2, 2)
fig.suptitle('Subplots')

# Add first subplot
axs[0, 0].plot(t, s)
axs[0, 0].set_title('Subplot [0, 0]')

# Add second subplot
axs[0, 1].plot(t, s, 'g-')
axs[0, 1].set_title('Subplot [0, 1]')

# Add third subplot
axs[1, 0].plot(t, s, 'r-')
axs[1, 0].set_title('Subplot [1, 0]')

# Add fourth subplot
axs[1, 1].plot(t, s, 'y-')
axs[1, 1].set_title('Subplot [1, 1]')

for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='y-label')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

# Display the chart
plt.show()
