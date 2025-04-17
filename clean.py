import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file, setting header to row 4 (index 4, since indexing starts at 0)
data = pd.read_csv('hc11.1.csv', header=4)

# Rename the first column to 'Category' (pandas may name it 'Unnamed: 0' due to empty first cell in header row)
data.rename(columns={data.columns[0]: 'Category'}, inplace=True)

# Strip whitespace from 'Category' column to ensure consistent filtering
data['Category'] = data['Category'].str.strip()

# Define column names for clarity and consistency with the CSV
any_insecurity_col = 'Any household energy insecurity3'
disconnect_col = 'Receiving disconnect or delivery stop notice'

# Replace 'Q' (suppressed data) and 'N' (no responses) with NaN
data.replace(['Q', 'N'], pd.NA, inplace=True)

# Convert relevant columns to numeric, coercing errors to NaN
data[any_insecurity_col] = pd.to_numeric(data[any_insecurity_col], errors='coerce')
data[disconnect_col] = pd.to_numeric(data[disconnect_col], errors='coerce')

# Filter data for census regions
regions = ['Northeast', 'Midwest', 'South', 'West']
region_data = data[data['Category'].isin(regions)].dropna(subset=[any_insecurity_col])

# Filter data for income levels
income_categories = [
    'Less than $20,000', '$20,000 to $39,999', '$40,000 to $59,999',
    '$60,000 to $79,999', '$80,000 to $99,999', '$100,000 to $119,999',
    '$120,000 to $139,999', '$140,000 or more'
]
income_data = data[data['Category'].isin(income_categories)].dropna(subset=[disconnect_col])

# Plot 1: Households Reporting Any Energy Insecurity by Region
plt.figure(figsize=(8, 5))
plt.bar(region_data['Category'], region_data[any_insecurity_col], color='skyblue')
plt.title('Households Reporting Any Energy Insecurity by Region (2015)')
plt.xlabel('Census Region')
plt.ylabel('Housing Units (millions)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('energy_insecurity_by_region.png')

# Plot 2: Households Receiving Disconnect Notices by Income Level
plt.figure(figsize=(10, 6))
plt.bar(income_data['Category'], income_data[disconnect_col], color='salmon')
plt.title('Households Receiving Disconnect Notices by Income Level (2015)')
plt.xlabel('Income Level')
plt.ylabel('Housing Units (millions)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('disconnect_notices_by_income.png')