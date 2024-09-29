import matplotlib.pyplot as plt

# Data
countries = [
    'Ethiopia', 'Somalia', 'South Sudan', 'Kenya', 
    'Mozambique', 'Madagascar', 'Malawi', 'Zimbabwe'
]
categories = [
    'Livelihood & Market', 'Food Security & Nutrition', 'DRR & CIM', 
    'Safeguarding & Protection', 'Crisis Modifier'
]
data = [
    [74526, 21600, 8660, 11370, 17372],
    [3150, 19470, 2235, 43025, 29766.6],
    [67980, 48978, 21216, 36888, 15240],
    [46475, 81928, 36405, 31966, 16150],
    [10000, 5000, 660, 6500, 2000],
    [2810, 0, 10200, 1000, 0],
    [750, 1500, 5400, 5400, 2500],
    [9577, 6643, 15782, 5110, 2104]
]

colors = ['#ff6347', '#ffa500', '#008FDB', '#ffcc99', '#c2c2f0']

# Plotting individual 2D pie charts
fig, axes = plt.subplots(2, 4, figsize=(20, 10))
axes = axes.flatten()

for i, country in enumerate(countries):
    ax = axes[i]
    ax.pie(data[i], startangle=140, colors=colors, wedgeprops=dict(width=0.3, edgecolor='w'))
    ax.set_title(country, fontsize=14, fontweight='bold')

# Create a legend
fig.legend(categories, loc='lower center', ncol=5, fontsize=12)

fig.suptitle('HCRP 2024-25 Targeted Population by Country and Program', fontsize=16, fontweight='bold')
plt.tight_layout(rect=[0, 0.1, 1, 0.95])
plt.show()
