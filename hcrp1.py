import matplotlib.pyplot as plt

# Data to plot
labels = ['IPC 4 Emergency (Ethiopia, Somalia & South Sudan)', 
          'IPC 3 Crisis (Kenya, Mozambique, Madagascar, Malawi & Zimbabwe)']
sizes = [421477, 305860]
colors = ['#ff914d','#008FDB']
explode = (0.1, 0)  # explode 1st slice

# Plot
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%',
                                  shadow=True, startangle=140)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')

# Title
plt.title('HCRP Target Population and IPC Outlook 2024-25')

# Legend with wrapped text
wrapped_labels = ['\n'.join([label[i:i+30] for i in range(0, len(label), 30)]) for label in labels]
ax.legend(wedges, wrapped_labels, title="IPC Levels", loc="lower right", bbox_to_anchor=(1.25, 0))

# Show the plot
plt.show()
