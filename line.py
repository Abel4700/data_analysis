import matplotlib.pyplot as plt

# Data
years = [2017, 2018, 2019, 2020, 2021, 2022, 2023]
individual_case_management = [69, 77, 81, 102, 129, 141, 148]
family_reunification_support = [60, 61, 57, 71, 87, 97, 101]
mental_health_counseling = [6, 8, 8, 8, 12, 13, 17]
psychosocial_support = [67, 71, 76, 95, 119, 125, 131]
alternative_care_arrangement = [50, 56, 58, 74, 92, 104, 109]
educational_support = [31, 29, 30, 32, 44, 39, 40]
community_based_cp = [64, 71, 75, 95, 124, 132, 137]
shelter_provision = [11, 8, 10, 6, 10, 6, 9]
livelihood_support_for_families = [9, 6, 7, 6, 15, 17, 20]
wash = [11, 9, 9, 11, 8, 9, 12]
health_and_nutrition = [13, 10, 10, 10, 19, 17, 16]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(years, individual_case_management, marker='o', label='Individual Case Management')
plt.plot(years, family_reunification_support, marker='o', label='Family Reunification Support')
plt.plot(years, mental_health_counseling, marker='o', label='Mental Health Counseling')
plt.plot(years, psychosocial_support, marker='o', label='Psychosocial Support')
plt.plot(years, alternative_care_arrangement, marker='o', label='Alternative Care Arrangement')
plt.plot(years, educational_support, marker='o', label='Educational Support')
plt.plot(years, community_based_cp, marker='o', label='Community Based CP')
plt.plot(years, shelter_provision, marker='o', label='Shelter Provision')
plt.plot(years, livelihood_support_for_families, marker='o', label='Livelihood Support for Families')
plt.plot(years, wash, marker='o', label='WASH')
plt.plot(years, health_and_nutrition, marker='o', label='Health and Nutrition')

# Labels and title
plt.xlabel('Year')
plt.ylabel('Mean')
plt.title('Mean of Services by Year')
plt.xticks(years)
plt.grid(True)
plt.legend()

# Show plot
plt.tight_layout()
plt.show()
