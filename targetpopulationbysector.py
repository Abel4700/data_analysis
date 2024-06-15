import matplotlib.pyplot as plt

# Data for the pie chart
labels = ['LIVELIHOOD & MARKET', 'FOOD SECURITY & NUTRITION', 'DRR AND CCIM', 'SAFEGUARDING & PROTECTION', 'CRISES MODIFIERS (10%)']
sizes = [215268, 185119, 100558, 141259, 85133]
colors = ['#ff6347', '#ff8c00', '#ff4500', '#ff7f50', '#008FDB']  # Predominantly red and orange, with blue

explode = (0.1, 0.1, 0.1, 0.1, 0.1)  # explode all slices slightly for emphasis

# Plotting the pie chart
fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140, textprops={'fontsize': 12})
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Adding a title with bold font and spacing
plt.title('HCRP TARGET POPULATION BY SECTOR', fontsize=14, fontweight='bold', pad=20)

# Show the plot
plt.show()
