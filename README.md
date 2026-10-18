# IBM Data Science Capstone: SpaceX Falcon 9 First-Stage Landing Prediction

This project predicts whether the Falcon 9 first stage will land successfully, using SpaceX launch data. If we can predict the landing, we can estimate the cost of a launch (about $62M for SpaceX vs. $165M+ for other providers).

## Notebooks and files

| Step | File |
|---|---|
| 1. Data collection (SpaceX REST API) | `jupyter-labs-spacex-data-collection-api.ipynb` |
| 2. Data collection (web scraping Wikipedia) | `jupyter-labs-webscraping.ipynb` |
| 3. Data wrangling | `labs-jupyter-spacex-Data_wrangling.ipynb` |
| 4. EDA with SQL | `jupyter-labs-eda-sql-coursera_sqllite.ipynb` |
| 5. EDA with data visualization | `jupyter-labs-eda-dataviz.ipynb` |
| 6. Interactive map with Folium | `lab-jupyter-launch-site-location.ipynb` |
| 7. Interactive dashboard with Plotly Dash | `spacex_dash_app.py` |
| 8. Machine learning prediction | `SpaceX-Machine-Learning-Prediction-Part-5.ipynb` |
| Final presentation | `Data_Science_Capstone_Project_Report.pdf` |

## Key results
- Overall first-stage landing success rate: 66.7%, rising from 0% (2010–2013) to about 85–90% (2019–2020)
- ES-L1, GEO, HEO and SSO orbits had 100% success; KSC LC-39A had the most successful launches
- Logistic Regression, SVM, Decision Tree and KNN reach about 83% test accuracy
