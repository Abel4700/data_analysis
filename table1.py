import matplotlib.pyplot as plt
import numpy as np

# Data to plot
labels = ['Education', 'Health including mental health', 'Family reunification', 
          'Overall child protection', 'Psychosocial support', 'Livelihood', 'Other']
sizes = [21, 1, 26, 150, 47, 5, 3]
colors = ['#ff914d', '#008FDB', '#FFD700', '#7FFF00', '#FF69B4', '#FFA500', '#A9A9A9']
explode = (0.1, 0, 0, 0.1, 0, 0, 0)  # explode slices if necessary

# Plot
fig, ax = plt.subplots()
wedges, _ = ax.pie(sizes, explode=explode, labels=None, colors=colors,
                   shadow=True, startangle=140)

# Draw lines connecting slices to the percentage labels
for i, a in enumerate(wedges):
    ang = (a.theta2 - a.theta1)/2. + a.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))

    # Percentage value
    percentage = sizes[i] / sum(sizes) * 100

    # Adjusting the position of the label based on the angle
    horizontalalignment = {-1: 'right', 1: 'left'}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    ax.annotate(f'{percentage:.1f}%', xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, arrowprops=dict(arrowstyle="-", connectionstyle=connectionstyle))

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')

# Create legend
ax.legend(wedges, labels, title="Service Types", loc="center left", bbox_to_anchor=(1, 0.5))

# Title
plt.title('Types of Service Frequencies')

# Show the plot
plt.show()
