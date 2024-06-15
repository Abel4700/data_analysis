import pandas as pd

# Create a DataFrame from your data
data = {
    'Year': [2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Individual Case Management': [69, 77, 81, 102, 129, 141, 148],
    'Family Reunification Support': [60, 61, 57, 71, 87, 97, 101],
    'Mental Health Counseling': [6, 8, 8, 8, 12, 13, 17],
    'Psychosocial Support': [67, 71, 76, 95, 119, 125, 131],
    'Alternative Care Arrangement': [50, 56, 58, 74, 92, 104, 109],
    'Educational Support': [31, 29, 30, 32, 44, 39, 40],
    'Community Based CP': [64, 71, 75, 95, 124, 132, 137],
    'Shelter Provision': [11, 8, 10, 6, 10, 6, 9],
    'Livelihood Support for Families': [9, 6, 7, 6, 15, 17, 20],
    'WASH': [11, 9, 9, 11, 8, 9, 12],
    'Health and Nutrition': [13, 10, 10, 10, 19, 17, 16]
    # Add other columns with corresponding data
}
df = pd.DataFrame(data)

# Iterate over the columns of the DataFrame
for variable in df.columns[1:]:  # Exclude the 'Year' column
    # Perform operations on each column
    print(f"Variable: {variable}")
    print(df[variable])  # Example: Print the values of the column
