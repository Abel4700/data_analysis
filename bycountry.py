import matplotlib.pyplot as plt

# Data
countries = ['Ethiopia', 'Somalia', 'South Sudan', 'Kenya', 'Mozambique', 'Madagascar', 'Malawi', 'Zimbabwe']
population = [133528, 97646.6, 190302, 212924, 24160, 14010, 15550, 39216]

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(countries, population, color='#008FDB')  # Use a consistent color for all bars

plt.title('Target Population by Country', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Population', fontsize=12)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right', fontsize=10)

# Add data labels above each bar
for i, val in enumerate(population):
    plt.text(i, val, str(val), ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()
