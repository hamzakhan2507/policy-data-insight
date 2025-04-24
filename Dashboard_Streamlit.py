import pandas as pd
import streamlit as st
import plotly.express as px

# ────── Configuration ──────
CSV_PATH = 'cleaned_HC 11.1.csv'
TOTAL_COL = 'Total U.S.'
ANY_COL = 'Any household energy insecurity'
DISCONNECT_COL = 'Receiving disconnect or delivery stop notice'

CATEGORIES = {
    "Census Division": [
        'New England', 'Middle Atlantic', 'East North Central', 'West North Central',
        'South Atlantic', 'East South Central', 'West South Central', 'Mountain', 'Pacific'
    ],
    "Income Level": [
        'Less than $5,000', '$5,000 to $9,999', '$10,000 to $19,999',
        '$20,000 to $39,999', '$40,000 to $59,999', '$60,000 to $99,999',
        '$100,000 to $149,999', '$150,000 or more'
    ],
    "Race": [
        'White alone', 'Black or African American alone', 'Asian alone',
        'American Indian or Alaska Native alone', 'Native Hawaiian or Other Pacific Islander alone',
        'More than one race'
    ],
    "Construction Year": [
        'Before 1950', '1950 to 1959', '1960 to 1969', '1970 to 1979',
        '1980 to 1989', '1990 to 1999', '2000 to 2009', '2010 to 2015', '2016 to 2020'
    ]
}

# ────── Data Loading & Preparation ──────
@st.cache_data
def load_and_prepare(path):
    df = pd.read_csv(path)
    df.rename(columns={'Variables': 'Category'}, inplace=True)
    df['Category'] = df['Category'].str.strip()
    for col in (TOTAL_COL, ANY_COL, DISCONNECT_COL):
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df['Any Insecurity Percent']    = df[ANY_COL] / df[TOTAL_COL] * 100
    df['Disconnect Notice Percent'] = df[DISCONNECT_COL] / df[TOTAL_COL] * 100
    return df

df = load_and_prepare(CSV_PATH)

# ────── Sidebar Controls ──────
st.sidebar.header("Select View")
category_type = st.sidebar.selectbox("Category type", list(CATEGORIES.keys()))
available     = CATEGORIES[category_type]
selected      = st.sidebar.multiselect(f"Pick {category_type}", available, default=available)
metric        = st.sidebar.selectbox("Metric to plot", ["Any Insecurity Percent", "Disconnect Notice Percent"])
sort_asc      = st.sidebar.checkbox("Sort ascending", value=True)

# ────── Filter & Sort ──────
view_df = df[df['Category'].isin(selected)].copy()
if sort_asc:
    view_df = view_df.sort_values(by=metric)

# ────── Plot ──────
st.title("🏠 Household Energy Insecurity Dashboard")
st.markdown(f"**Category:** {category_type}\n**Metric:** {metric}")

fig = px.bar(
    view_df,
    x='Category',
    y=metric,
    title=f"{metric} by {category_type} (2020)",
    labels={metric: metric.replace(" Percent", " (%)")}
)
fig.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig, use_container_width=True)
