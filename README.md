# policy-data-insight

# Energy Insecurity in U.S. Households (RECS 2020)

## 🔹 Project Summary

This project analyzes household energy insecurity in the United States using data from the U.S. Energy Information Administration's Residential Energy Consumption Survey (RECS) 2020. "Any Energy Insecurity" as defined by RECS includes one or more of the following experiences: receiving a disconnect notice, reducing or forgoing basic necessities to pay energy bills, or keeping the home at an unsafe temperature. This project investigates "Any Energy Insecurity" across these dimensions, with particular focus on **disconnection notices**.  
By examining variations in energy insecurity across income brackets, racial and ethnic groups, housing construction vintages, and census regions, the study leverages statistical modeling, geospatial mapping, and interactive visualizations to reveal where and among whom the risks are greatest. The insights generated aim to guide more equitable energy assistance policies and interventions that address affordability and access challenges.

## 📊 Project Goals

* Identify patterns of household energy insecurity by demographics and geography.
* Visualize disparities using bar plots and choropleth maps.
* Model disconnection frequency using ordered logistic regression.
* Develop a public-facing Streamlit dashboard for interactive exploration.

## 📂 Repository Contents

| File/Script              | Description                                                             |
| ------------------------ | ----------------------------------------------------------------------- |
| `Dashboard_Streamlit.py` | Streamlit dashboard for visual exploration of insecurity metrics        |
| `CODE.py`                | Python script to generate bar plots and compute metrics                 |
| `Geo-pandas.py`          | Python script to generate regional choropleth maps using GeoPandas      |
| `cleaned_HC11.1.csv`     | Cleaned version of RECS 2020 Table HC11.1 (energy insecurity summary)   |
| `cleaned_data2020.csv`   | Trimmed RECS 2020 microdata (disaggregated household-level data)        |
| `requirements.txt`       | Python dependencies for running the dashboard                           |
| `R_analysis/`            | Contains ordered logit regression script                                |
| `figures/`               | Saved images from Python plots, QGIS maps, and ggplot regression charts |
| `QGISProject.qgz`        | QGIS project file containing styled maps for census division totals     |

**Note:** Figures are saved in the [`/figures/`](./figures) folder within the repository. This includes static bar plots, choropleth maps, and regression visualizations (ggplots). You can also explore interactive versions on the [Streamlit App](https://dashboardapppy-birkbduyuwrxwegphddq4v.streamlit.app/).

## 📅 Data Sources

### 1. **RECS 2020 - Household Energy Insecurity (Table HC11.1)**

* Source: [EIA RECS 2020 Survey Data](https://www.eia.gov/consumption/residential/data/2020/index.php?view=characteristics)
* Notes: The Excel file was cleaned to remove formatting and saved as `cleaned_HC11.1.csv`.

### 2. **RECS 2020 - Microdata**

* Source: [EIA RECS 2020 Microdata](https://www.eia.gov/consumption/residential/data/2020/index.php?view=microdata)
* Notes: The microdata was used as-is but filtered to remove non-relevant variables. Final version saved as `cleaned_data2020.csv`.

### 3. **U.S. Census Divisions Shapefile (2018)**

* Source: [U.S. Census Bureau - Cartographic Boundary Files](https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html)
* Notes: Used in QGIS project to spatially visualize disconnection and insecurity totals. Aligned with `cleaned_HC11.1.csv` division categories and integrated into `QGISProject`.

## 🔧 How to Reproduce

### 🔹 Streamlit and Python Visualizations

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
python Geo-Pandas.py
```

Explore energy insecurity metrics by income, race, housing construction year, and census region:
**🔗 [Streamlit App](https://dashboardapppy-birkbduyuwrxwegphddq4v.streamlit.app/)**

## 🗺️ QGIS Mapping

Two static maps showing total (non-percentage) disconnection and energy insecurity counts by U.S. Census Division were created using QGIS. The shapefile used was the 2018 U.S. Census Division shapefile, and the project is saved as `QGISProject`.

* These maps visualize **raw totals**, in contrast to the percentage-based choropleths created in `Geo-pandas.py`.
* The project uses the `cleaned_HC11.1.csv` regional summary data aligned to division names and overlays them on the 2018 shapefile to generate spatial visualizations.
* Output PNGs from QGIS are stored in the `/figures/` folder.

### 🔹 QGIS Mapping Procedure

1. Open the file `QGISProject` in QGIS (v3.0 or later).
2. Ensure that the 2018 Census shapefile components (`.shp`, `.shx`, `.dbf`) and `cleaned_HC11.1.csv` are present in the same directory.
3. Load the shapefile as the base layer and join the `cleaned_HC11.1.csv` using the `Division` field.
4. Style maps by count fields for Energy Insecurity and Disconnect Notices.
5. Export maps to PNG using `Project → Import/Export → Export Map to Image`.

## 🔄 Modeling Summary

* **Tool**: R / Rcmdr
* **Method**: Ordered logistic regression (`polr`)
* **Outcome**: Disconnection notice frequency (`SCALEE`, ordered 0 to 3)
* **Predictors**: Income bracket (`MONEYPY`), Householder race (`HOUSEHOLDER_RACE`)
* **Output**:

  * `MONEYPY`: Coefficient = −0.15 (p < 0.001) ➔ Higher income reduces disconnection risk
  * `HOUSEHOLDER_RACE`: Coefficient = +0.14 (p < 0.001) ➔ Non-white households face elevated risk
* **Visualization**: ggplot showing predicted probabilities across race & income

## 📊 Results Overview

* **The ordered logit regression confirms the expected trend**: higher income households are less likely to face disconnection, and racial disparities persist even after controlling for income.
* **Income, race, and housing construction year** are strong predictors of energy insecurity.
* **Census divisions** show wide disparities in both energy insecurity and disconnection notice rates.
* A total of **8 bar graphs** (Python), **2 choropleth maps** (Python- Geopandas),  and **2 choropleth maps** (QGIS) provide visual insight.
* **QGIS maps** are based on raw disconnection and energy insecurity counts by region (not percentage-wise).
* **Percentage-wise regional maps** have been created using GeoPandas.

## 📙 Credits & License

All code is publicly available for reproduction and reuse.
Data courtesy of the U.S. Energy Information Administration (RECS 2020) adn US Census Bureau (2018 Division Map).
