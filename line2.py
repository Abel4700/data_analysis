import matplotlib.pyplot as plt

# Historical data
variables = ['Individual Case Management', 'Family Reunification Support', 'Mental Health Counseling',
             'Psychosocial Support', 'Alternative Care Arrangement', 'Educational Support',
             'Community-Based Child Protection', 'Shelter Provision', 'Livelihood Support for Families',
             'WASH', 'Health and Nutrition']
historical_data = {
    'Individual Case Management': [69, 77, 81, 102, 129, 141, 148],
    'Family Reunification Support': [60, 61, 57, 71, 87, 97, 101],
    'Mental Health Counseling': [6, 8, 8, 8, 12, 13, 17],
    'Psychosocial Support': [67, 71, 76, 95, 119, 125, 131],
    'Alternative Care Arrangement': [50, 56, 58, 74, 92, 104, 109],
    'Educational Support': [31, 29, 30, 32, 44, 39, 40],
    'Community-Based Child Protection': [64, 71, 75, 95, 124, 132, 137],
    'Shelter Provision': [11, 8, 10, 6, 10, 6, 9],
    'Livelihood Support for Families': [9, 6, 7, 6, 15, 17, 20],
    'WASH': [11, 9, 9, 11, 8, 9, 12],
    'Health and Nutrition': [13, 10, 10, 10, 19, 17, 16]
}

# Plot historical data
plt.figure(figsize=(12, 8))
for var in variables:
    plt.plot(historical_data[var], label=var)

# Labels and title
plt.xlabel('Year')
plt.ylabel('Mean')
plt.title('Historical Data')
plt.xticks(range(len(historical_data['Individual Case Management'])), range(2017, 2024))
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
