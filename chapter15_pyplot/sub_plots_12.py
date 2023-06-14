import matplotlib.pyplot as plt

# Generate some data to display
t = range(0, 20)
s = range(30, 10, -1)

# Set up the figure
fig = plt.figure()
gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
(ax1, ax2), (ax3, ax4) = gs.subplots(sharex='col', sharey='row')

fig.suptitle('Shared grid')
ax1.plot(t, s)
ax2.plot(t, s, 'tab:orange')
ax3.plot(t, s, 'tab:green')
ax4.plot(t, s, 'tab:red')

for ax in fig.get_axes():
    ax.label_outer()

# Display the chart
plt.show()
