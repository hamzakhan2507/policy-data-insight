import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv('cleaned_HC 11.1.csv')

# Rename the first column to 'Category' for clarity
data.rename(columns={'Variables': 'Category'}, inplace=True)

# Strip whitespace from 'Category' column to ensure consistent filtering
data['Category'] = data['Category'].str.strip()

# Define column names for clarity
total_col = 'Total U.S.'
any_insecurity_col = 'Any household energy insecurity'
disconnect_col = 'Receiving disconnect or delivery stop notice'

# Convert columns to numeric, coercing errors to NaN
data[total_col] = pd.to_numeric(data[total_col], errors='coerce')
data[any_insecurity_col] = pd.to_numeric(data[any_insecurity_col], errors='coerce')
data[disconnect_col] = pd.to_numeric(data[disconnect_col], errors='coerce')

# Calculate percentages
data['Any Insecurity Percent'] = (data[any_insecurity_col] / data[total_col]) * 100
data['Disconnect Notice Percent'] = (data[disconnect_col] / data[total_col]) * 100

# Define categories
# 1. Census Divisions
census_divisions = [
    'New England', 'Middle Atlantic', 'East North Central', 'West North Central',
    'South Atlantic', 'East South Central', 'West South Central', 'Mountain', 'Pacific'
]

# 2. Income Levels
income_levels = [
    'Less than $5,000', '$5,000 to $9,999', '$10,000 to $19,999',
    '$20,000 to $39,999', '$40,000 to $59,999', '$60,000 to $99,999',
    '$100,000 to $149,999', '$150,000 or more'
]

# 3. Race
race_categories = [
    'White alone', 'Black or African American alone', 'Asian alone',
    'American Indian or Alaska Native alone', 'Native Hawaiian or Other Pacific Islander alone',
    'More than one race'
]

# 4. Construction Year
construction_years = [
    'Before 1950', '1950 to 1959', '1960 to 1969', '1970 to 1979',
    '1980 to 1989', '1990 to 1999', '2000 to 2009', '2010 to 2015', '2016 to 2020'
]

# Filter data for each category
division_data = data[data['Category'].isin(census_divisions)]
income_data = data[data['Category'].isin(income_levels)]
race_data = data[data['Category'].isin(race_categories)]
construction_data = data[data['Category'].isin(construction_years)]

# Sort Census Division and Race data by percentage (ascending)
# Census Division
division_data_any = division_data.sort_values('Any Insecurity Percent')
division_data_disconnect = division_data.sort_values('Disconnect Notice Percent')

# Race
race_data_any = race_data.sort_values('Any Insecurity Percent')
race_data_disconnect = race_data.sort_values('Disconnect Notice Percent')

# Plot 1: Any Energy Insecurity by Census Division (Sorted)
plt.figure(figsize=(12, 6))
plt.bar(division_data_any['Category'], division_data_any['Any Insecurity Percent'], color='skyblue')
plt.title('Percentage with Any Energy Insecurity by Census Division (2015)')
plt.xlabel('Census Division')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('any_insecurity_by_division_sorted.png')

# Plot 2: Disconnect Notices by Census Division (Sorted)
plt.figure(figsize=(12, 6))
plt.bar(division_data_disconnect['Category'], division_data_disconnect['Disconnect Notice Percent'], color='salmon')
plt.title('Percentage Receiving Disconnect Notices by Census Division (2015)')
plt.xlabel('Census Division')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('disconnect_notices_by_division_sorted.png')

# Plot 3: Any Energy Insecurity by Income Level (Unsorted)
plt.figure(figsize=(10, 6))
plt.bar(income_data['Category'], income_data['Any Insecurity Percent'], color='skyblue')
plt.title('Percentage with Any Energy Insecurity by Income Level (2015)')
plt.xlabel('Income Level')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('any_insecurity_by_income.png')

# Plot 4: Disconnect Notices by Income Level (Unsorted)
plt.figure(figsize=(10, 6))
plt.bar(income_data['Category'], income_data['Disconnect Notice Percent'], color='salmon')
plt.title('Percentage Receiving Disconnect Notices by Income Level (2015)')
plt.xlabel('Income Level')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('disconnect_notices_by_income.png')

# Plot 5: Any Energy Insecurity by Race (Sorted)
plt.figure(figsize=(10, 6))
plt.bar(race_data_any['Category'], race_data_any['Any Insecurity Percent'], color='skyblue')
plt.title('Percentage with Any Energy Insecurity by Race (2015)')
plt.xlabel('Race')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('any_insecurity_by_race_sorted.png')

# Plot 6: Disconnect Notices by Race (Sorted)
plt.figure(figsize=(10, 6))
plt.bar(race_data_disconnect['Category'], race_data_disconnect['Disconnect Notice Percent'], color='salmon')
plt.title('Percentage Receiving Disconnect Notices by Race (2015)')
plt.xlabel('Race')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('disconnect_notices_by_race_sorted.png')

# Plot 7: Any Energy Insecurity by Construction Year (Unsorted)
plt.figure(figsize=(10, 6))
plt.bar(construction_data['Category'], construction_data['Any Insecurity Percent'], color='skyblue')
plt.title('Percentage with Any Energy Insecurity by Construction Year (2015)')
plt.xlabel('Construction Year')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('any_insecurity_by_construction_year.png')

# Plot 8: Disconnect Notices by Construction Year (Unsorted)
plt.figure(figsize=(10, 6))
plt.bar(construction_data['Category'], construction_data['Disconnect Notice Percent'], color='salmon')
plt.title('Percentage Receiving Disconnect Notices by Construction Year (2015)')
plt.xlabel('Construction Year')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('disconnect_notices_by_construction_year.png')