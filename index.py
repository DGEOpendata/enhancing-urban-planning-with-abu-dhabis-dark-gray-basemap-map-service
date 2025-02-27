python
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the Abu Dhabi basemap
basemap = gpd.read_file('path_to_Abu_Dhabi_dark_gray_basemap.shp')

# Plot the basemap
fig, ax = plt.subplots(figsize=(10, 10))
basemap.plot(ax=ax, color='black', edgecolor='white')

# Overlay additional data (e.g., transportation routes)
transportation_data = gpd.read_file('path_to_transportation_routes.shp')
transportation_data.plot(ax=ax, color='blue', linewidth=2)

plt.title('Abu Dhabi Urban Planning with Dark Gray Basemap')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
