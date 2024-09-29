import matplotlib.pyplot as plt

# Data
categories = [
    'People targeted (HNRP/HRP)', 
    'People targeted (FSL)', 
    'PIN (FSL)', 
    'PIN (All sectors)'
]
values = [
    15.5, 
    10.4, 
    15.8, 
    21.4
]

# Define colors for each segment
colors = ['#ff6347', '#ffa500', '#008FDB', '#ffcc99']

# Create pie chart
plt.figure(figsize=(10, 8))
explode = (0.1, 0, 0, 0)  # Explode the first slice for emphasis
patches, texts, autotexts = plt.pie(
    values, 
    labels=categories, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    explode=explode, 
    shadow=True, 
    wedgeprops={'edgecolor': 'black'}
)

# Adjust the percentage labels for better readability
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(12)
    autotext.set_weight('bold')

# Add title
plt.title('Ethiopia Key Figures: PIN & Target in Millions - HNRP/HRP 2024-25', fontsize=16, fontweight='bold', pad=20)

# Show plot
plt.tight_layout()
plt.show()
