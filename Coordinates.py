import pandas as pd

# Create a DataFrame with locations and their coordinates
data = {
    'Location': ['Harar', 'Adama', 'Debre Birhan', 'Mekelle', 'Addis Ababa', 'Dire Dawa', 
                 'Shanghai', 'Kuwait', 'Bahrain', 'Dubai'],
    'Latitude': [9.3133, 8.5470, 9.6803, 13.4967, 9.0306, 9.6008, 31.2304, 29.3759, 26.0667, 25.276987],
    'Longitude': [42.1182, 39.2695, 39.5320, 39.4753, 38.7408, 41.8501, 121.4737, 47.9774, 50.5577, 55.296249]
}

df = pd.DataFrame(data)
print(df)
