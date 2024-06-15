import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

# Ensure that the IBM Plex Sans font is available
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['IBM Plex Sans']

# Data
categories = ['IPC 4 Emergency', 'IPC 3 Crisis']
population = [421477, 305860]
colors = ['#ff6347', '#ffa500']  # Red and orange colors

# Create pie chart
fig, ax = plt.subplots(figsize=(4, 2))
explode = (0.1, 0)  # Explode the first slice for emphasis
patches, texts, autotexts = ax.pie(population, labels=categories, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode, wedgeprops=dict(width=0.4))

plt.title('Food Insecurity by IPC Phase', fontsize=16, fontweight='bold', pad=20)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Adjust the percentage labels to rest fully on the slices
for autotext in autotexts:
    autotext.set_color('blue')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

# Create a custom legend with countries on the bottom right
legend_labels = [
    'Ethiopia, Somalia & South Sudan',
    'Kenya, Mozambique, Madagascar, Malawi & Zimbabwe'
]
plt.legend(patches, legend_labels, loc='lower right', fontsize=10, frameon=False, bbox_to_anchor=(1, 0.5), bbox_transform=fig.transFigure)

plt.tight_layout()  # Avoids cropping labels
plt.show()
