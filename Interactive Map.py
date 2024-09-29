import pandas as pd
import folium

# Create a DataFrame with locations and their coordinates
data = {
    'Location': ['Harar', 'Adama', 'Debre Birhan', 'Mekelle', 'Addis Ababa', 'Dire Dawa', 
                 'Shanghai', 'Kuwait', 'Bahrain', 'Dubai'],
    'Latitude': [9.3133, 8.5470, 9.6803, 13.4967, 9.0306, 9.6008, 31.2304, 29.3759, 26.0667, 25.276987],
    'Longitude': [42.1182, 39.2695, 39.5320, 39.4753, 38.7408, 41.8501, 121.4737, 47.9774, 50.5577, 55.296249]
}

df = pd.DataFrame(data)

# Create a map centered around Ethiopia
map_center = [9.145, 40.489673]
m = folium.Map(location=map_center, zoom_start=3, width='100%', height='100%')

# Add markers to the map without popups
for index, row in df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']]
    ).add_to(m)

# Save the map to an HTML file
m.save('about_us_map_large.html')
