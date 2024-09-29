import matplotlib.pyplot as plt

# Data
objectives = [
    'Livelihood & Market', 
    'Food Security & Nutrition', 
    'DRR & CIM', 
    'Safeguarding & Protection', 
    'Crisis Modifier'
]
funding_requirements = [
    4668331, 
    7642924, 
    2466393, 
    2919641, 
    1821552
]

# Define colors for each segment
colors = ['#ff6347', '#ffa500', '#008FDB', '#ffcc99', '#c2c2f0']

# Create pie chart
plt.figure(figsize=(10, 8))
explode = (0.1, 0.1, 0.1, 0.1, 0.1)  # Explode all slices for emphasis
patches, texts, autotexts = plt.pie(
    funding_requirements, 
    labels=objectives, 
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
plt.title('Funding Requirements by Objective', fontsize=16, fontweight='bold', pad=20)

# Show plot
plt.tight_layout()
plt.show()
