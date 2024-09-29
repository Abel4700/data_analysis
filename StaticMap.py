import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Create a DataFrame with locations and their coordinates
data = {
    'Location': ['Harar', 'Adama', 'Debre Birhan', 'Mekelle', 'Addis Ababa', 'Dire Dawa', 
                 'Shanghai', 'Kuwait', 'Bahrain', 'Dubai'],
    'Latitude': [9.3133, 8.5470, 9.6803, 13.4967, 9.0306, 9.6008, 31.2304, 29.3759, 26.0667, 25.276987],
    'Longitude': [42.1182, 39.2695, 39.5320, 39.4753, 38.7408, 41.8501, 121.4737, 47.9774, 50.5577, 55.296249]
}

df = pd.DataFrame(data)

# Create a figure with a larger size
plt.figure(figsize=(20, 15))

# Create a Basemap instance
m = Basemap(projection='merc', llcrnrlat=-10, urcrnrlat=50, llcrnrlon=30, urcrnrlon=130, resolution='i')

# Draw map details
m.drawcoastlines()
m.drawcountries()
m.drawmapboundary()

# Convert latitude and longitude to map projection coordinates
x, y = m(df['Longitude'].values, df['Latitude'].values)

# Plot the points on the map
m.scatter(x, y, marker='o', color='r', zorder=5)

# Show the plot

plt.show()
