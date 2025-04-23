# policy-data-insight
# Energy Insecurity in U.S. Households (RECS 2020)

## 🔹 Project Summary
This project analyzes household energy insecurity in the United States using data from the U.S. Energy Information Administration's Residential Energy Consumption Survey (RECS) 2020. It explores disparities in energy insecurity and disconnection notices across income groups, racial categories, and census regions through statistical modeling, geospatial mapping, and interactive visualization.

## 📊 Project Goals
- Identify patterns of household energy insecurity by demographics and geography.
- Visualize disparities using bar plots and choropleth maps.
- Model disconnection frequency using ordered logistic regression.
- Develop a public-facing Streamlit dashboard for interactive exploration.

## 📂 Repository Contents
| File/Folder               | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| `dashboard_app.py`        | Streamlit dashboard for visual exploration of insecurity metrics            |
| `analysis_script.py`      | Python script to generate static plots and compute metrics                  |
| `/figures/`               | Bar plots (total: 8) for income, race, region, construction year            |
| `/qgis_maps/`             | QGIS images showing energy insecurity and disconnect notices by region      |
| `/r_analysis/`            | Ordered logit regression script, ggplot visuals, model output              |
| `cleaned_HC11.1.csv`      | Cleaned version of RECS 2020 Table HC11.1 (energy insecurity summary)       |
| `cleaned_data2020.csv`    | Trimmed RECS 2020 microdata (disaggregated household-level data)            |
| `requirements.txt`        | Python dependencies for running the dashboard                              |

## 📅 Data Sources
### 1. **RECS 2020 - Household Energy Insecurity (Table HC11.1)**
- Source: [EIA RECS 2020 Summary Tables](https://www.eia.gov/consumption/residential/data/2020/index.php?view=characteristics)
- File: Excel format (HC11.1) was cleaned to remove formatting and saved as `cleaned_HC11.1.csv`

### 2. **RECS 2020 - Microdata**
- Source: [EIA RECS 2020 Microdata](https://www.eia.gov/consumption/residential/data/2020/index.php?view=microdata)
- Notes: Used as-is but trimmed to remove variables not relevant to our analysis to reduce file size and speed up processing.
- Saved as `cleaned_data2020.csv`

## 🔧 How to Reproduce
```bash
# Clone the repository
https://github.com/yourusername/energy-insecurity-project.git
cd energy-insecurity-project

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run dashboard_app.py

# Run Python analysis script
python analysis_script.py
```

## 🌍 Interactive Dashboard
Explore metrics by income, race, construction year, and census region:  
**🔗 [Streamlit App](https://dashboardapppy-birkbduyuwrxwegphddq4v.streamlit.app/)**

## 📊 Results Overview
- **Income and race** are strong predictors of energy insecurity.
- **Census divisions** show wide disparities in both energy insecurity and disconnection notice rates.
- **Ordered logistic regression** confirms that lower-income and non-white households face higher risk.
- A total of **8 bar graphs** (Python) and **2 choropleth maps** (QGIS) provide visual insight.

## 🔄 Modeling Summary
- **Tool**: R / Rcmdr
- **Method**: Ordered logistic regression (polr)
- **Outcome**: Disconnection notice frequency (`SCALEE`, 0 to 3)
- **Predictors**: Income bracket (`MONEYPY`), Householder race (`HOUSEHOLDER_RACE`)
- **Visualization**: ggplot showing predicted probabilities across race & income

## 📚 Credits & License
All code is publicly available for reproduction and reuse.

