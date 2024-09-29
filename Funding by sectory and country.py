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
    [1250686, 1001881, 319155, 298852, 462459],   # Ethiopia
    [461325, 965860, 155093, 1357183, 400000],    # Somalia
    [988092, 1883239, 576642, 464900, 388251],    # South Sudan
    [314639, 2478372, 450235, 178588, 281036],    # Kenya
    [630589, 791800, 93382, 43900, 14806],        # Mozambique
    [574946, 0, 581701, 50000, 0],                # Madagascar
    [60000, 149843, 250000, 65000, 140000],       # Malawi
    [388053, 371928, 40185, 461217, 135000]       # Zimbabwe
]

colors = ['#ff6347', '#ffa500', '#008FDB', '#ffcc99', '#c2c2f0']

# Plotting individual 2D pie charts
fig, axes = plt.subplots(2, 4, figsize=(20, 10))
axes = axes.flatten()

for i, country in enumerate(countries):
    ax = axes[i]
    wedges, texts, autotexts = ax.pie(
        data[i], startangle=140, colors=colors, wedgeprops=dict(width=0.3, edgecolor='w'),
        autopct=None
    )
    ax.set_title(country, fontsize=14, fontweight='bold')
    
    # Add the percentage labels outside the pie chart
    for j, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1) / 2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        ax.annotate(f'{data[i][j] / sum(data[i]) * 100:.1f}%', xy=(x, y), xytext=(1.35 * np.sign(x), 1.4 * y),
                    horizontalalignment=horizontalalignment, clip_on=False,
                    arrowprops=dict(arrowstyle="-", color='black', connectionstyle=connectionstyle))

# Create a legend
fig.legend(categories, loc='lower center', ncol=5, fontsize=12)

fig.suptitle('HCRP Funding Requirement by Country and Category', fontsize=16, fontweight='bold')
plt.tight_layout(rect=[0, 0.1, 1, 0.95])
plt.show()
