import matplotlib.pyplot as plt
import numpy as np  # Import numpy

# Data to plot
labels = ['Ethiopia', 'Somalia', 'South Sudan', 'Kenya', 'Mozambique', 'Madagascar', 'Malawi', 'Zimbabwe']
sizes = [133528, 97646.6, 190302, 212924, 24160, 14010, 15550, 39216]
colors = ['#ff914d','#008FDB', '#ffd700', '#90ee90', '#ff69b4', '#87ceeb', '#dda0dd', '#ff6347']
explode = (0.1, 0, 0, 0, 0, 0, 0, 0)  # explode 1st slice for Ethiopia

# Plot
fig, ax = plt.subplots()
wedges, texts = ax.pie(sizes, explode=explode, colors=colors, shadow=True, startangle=140)

# Draw lines connecting slices to the labels
for i, a in enumerate(wedges):
    ang = (a.theta2 - a.theta1)/2. + a.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))

    horizontalalignment = {-1: 'right', 1: 'left'}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    ax.annotate(f'{labels[i]}: {sizes[i]:,}', xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, arrowprops=dict(arrowstyle="-", connectionstyle=connectionstyle))

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')

# Title


# Legend with wrapped text
wrapped_labels = ['\n'.join([label[i:i+30] for i in range(0, len(label), 30)]) for label in labels]
ax.legend(wedges, wrapped_labels, title="Countries", loc="center left", bbox_to_anchor=(1, 0.5))

# Show the plot
plt.show()
