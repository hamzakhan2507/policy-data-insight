# policy-data-insight

# Energy Insecurity in U.S. Households (RECS 2020)

## 🔹 Project Summary

This project analyzes household energy insecurity in the United States using data from the U.S. Energy Information Administration's Residential Energy Consumption Survey (RECS) 2020. It explores disparities in energy insecurity and disconnection notices across income groups, racial categories, housing construction years, and census regions through statistical modeling, geospatial mapping, and interactive visualization. The analysis is designed to highlight inequities and inform policy decisions.

## 📊 Project Goals

* Identify patterns of household energy insecurity by demographics and geography.
* Visualize disparities using bar plots and choropleth maps.
* Model disconnection frequency using ordered logistic regression.
* Develop a public-facing Streamlit dashboard for interactive exploration.

## 📂 Repository Contents

| File/Script              | Description                                                            |
| ------------------------ | ---------------------------------------------------------------------- |
| `Dashboard_Streamlit.py` | Streamlit dashboard for visual exploration of insecurity metrics       |
| `CODE.py`                | Python script to generate bar plots and compute metrics                |
| `Geo-pandas.py`          | Python script to generate regional choropleth maps using GeoPandas     |
| `cleaned_HC11.1.csv`     | Cleaned version of RECS 2020 Table HC11.1 (energy insecurity summary)  |
| `cleaned_data2020.csv`   | Trimmed RECS 2020 microdata (disaggregated household-level data)       |
| `requirements.txt`       | Python dependencies for running the dashboard                          |
| `r_analysis/`            | Contains ordered logit regression script, ggplot visuals, model output |

**Note:** Figures are saved in the [`/figures/`](./figures) folder within the repository. This includes static bar plots, choropleth maps, and regression visualizations. You can also explore interactive versions on the [Streamlit App](https://dashboardapppy-birkbduyuwrxwegphddq4v.streamlit.app/).

## 📅 Data Sources

### 1. **RECS 2020 - Household Energy Insecurity (Table HC11.1)**

* Source: [EIA RECS 2020 Survey Data](https://www.eia.gov/consumption/residential/data/2020/index.php?view=characteristics)
* Notes: The Excel file was cleaned to remove formatting and saved as `cleaned_HC11.1.csv`.

### 2. **RECS 2020 - Microdata**

* Source: [EIA RECS 2020 Microdata](https://www.eia.gov/consumption/residential/data/2020/index.php?view=microdata)
* Notes: The microdata was used as-is but filtered to remove non-relevant variables. Final version saved as `cleaned_data2020.csv`.

## 🔧 How to Reproduce

```bash
# Clone the repository
https://github.com/yourusername/energy-insecurity-project.git
cd energy-insecurity-project

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run Dashboard_Streamlit.py

# Run bar plot analysis
python CODE.py

# Run regional map analysis
python Geo-pandas.py
```

## 🌍 Interactive Dashboard

Explore energy insecurity metrics by income, race, housing construction year, and census region:
**🔗 [Streamlit App](https://dashboardapppy-birkbduyuwrxwegphddq4v.streamlit.app/)**

## 📊 Results Overview

* **Income, race, and housing construction year** are strong predictors of energy insecurity.
* **Census divisions** show wide disparities in both energy insecurity and disconnection notice rates.
* **Disconnection notice** is one of the defining indicators of "Any Energy Insecurity" as per RECS definitions.
* A total of **8 bar graphs** (Python) and **2 choropleth maps** (QGIS) provide visual insight.
* **QGIS maps** are based on raw disconnection and energy insecurity counts by region (not percentage-wise).
* **Percentage-wise regional maps** have been created using `Geo-pandas.py`.

## 🔄 Modeling Summary

* **Tool**: R / Rcmdr
* **Method**: Ordered logistic regression (`polr`)
* **Outcome**: Disconnection notice frequency (`SCALEE`, ordered 0 to 3)
* **Predictors**: Income bracket (`MONEYPY`), Householder race (`HOUSEHOLDER_RACE`)
* **Output**:

  * `MONEYPY`: Coefficient = −0.15 (p < 0.001) ➔ Higher income reduces disconnection risk
  * `HOUSEHOLDER_RACE`: Coefficient = +0.14 (p < 0.001) ➔ Non-white households face elevated risk
* **Visualization**: ggplot showing predicted probabilities across race & income

## 📙 Credits & License

All code is publicly available for reproduction and reuse.
Data courtesy of the U.S. Energy Information Administration (RECS 2020).
