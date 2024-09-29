import matplotlib.pyplot as plt
import pandas as pd

# Data to plot
data = {
    'Region': ['Ethiopia', 'Afar Region', '', ''],
    'Area': ['IPC 3 and worse', 'Chifera District', 'Ewa District', ''],
    'Status': ['', 'IPC 3', 'IPC 4', '']
}

# Create a dataframe
df = pd.DataFrame(data)

# Plot the table
fig, ax = plt.subplots(figsize=(10, 3))  # Adjust the size as needed
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

# Create table
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center', cellColours=[['#f0f0f0', '#f0f0f0', '#f0f0f0']] * len(df))

# Style the table
table.auto_set_font_size(False)
table.set_fontsize(12)
table.auto_set_column_width(col=list(range(len(df.columns))))

# Set the color for the header
for (i, j), cell in table.get_celld().items():
    if i == 0:
        cell.set_text_props(weight='bold', color='white')
        cell.set_facecolor('#4f81bd')
    elif j == 0:
        cell.set_facecolor('#d9e1f2')
    elif j == 1 or j == 2:
        cell.set_facecolor('#f0f0f0')

# Adjust layout
plt.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.2)

# Set title
plt.title('IPC Status by Region and Area', fontsize=16)

# Show the plot
plt.show()