import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load your division shapefile (all 3 files must be in this directory)
shapefile_path = "cb_2018_us_division_500k"
gdf = gpd.read_file(shapefile_path)

# Explode multipolygons into singleparts (important!)
gdf = gdf.explode(index_parts=False).reset_index(drop=True)

# Your custom data
data = pd.DataFrame({
    "Division": [
        "New England", "Middle Atlantic", "East North Central", "West North Central",
        "South Atlantic", "East South Central", "West South Central", "Mountain", "Pacific"
    ],
    "Any_Insecurity": [23.13, 26, 25.77, 21.18, 26.49, 32.25, 34.4, 24.51, 28.09],
    "Disconnect_Notice": [7.14, 8.92, 10.84, 9.29, 10.79, 13.28, 13.89, 8.13, 6.86]
})

# Merge with shapefile on division name
merged = gdf.merge(data, left_on="NAME", right_on="Division")

# Plot 1: Energy Insecurity
fig1, ax1 = plt.subplots(figsize=(14, 12))
merged.plot(
    column="Any_Insecurity", cmap="YlGnBu", linewidth=0.8, ax=ax1,
    edgecolor="0.8", legend=True, legend_kwds={'shrink': 0.5, 'label': 'Any Energy Insecurity (%)'}
)
ax1.set_title("Any Household Energy Insecurity by Census Division", fontsize=18)
ax1.axis("off")
plt.tight_layout()
plt.savefig("Map_Any_Energy_Insecurity.png", dpi=300)

# Plot 2: Disconnect Notice
fig2, ax2 = plt.subplots(figsize=(14, 12))
merged.plot(
    column="Disconnect_Notice", cmap="OrRd", linewidth=0.8, ax=ax2,
    edgecolor="0.8", legend=True, legend_kwds={'shrink': 0.5, 'label': 'Disconnect Notice (%)'}
)
ax2.set_title("Receiving Disconnect Notice by Census Division", fontsize=18)
ax2.axis("off")
plt.tight_layout()
plt.savefig("Map_Disconnect_Notice.png", dpi=300)
