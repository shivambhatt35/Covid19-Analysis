# COVID-19 Data Analysis and World Happiness Report 2020

This repository presents a rigorous analysis of the global COVID-19 pandemic in relation to socio-economic indicators. Leveraging datasets from **Johns Hopkins University** and the **World Happiness Report 2020**, the project investigates the association between COVID-19 case trends and variables such as GDP per capita, social support, and healthy life expectancy. The objective is to provide evidence-based insights into the socio-economic determinants that may influence pandemic outcomes across countries.

---

## Project Overview

| Objective                                                                 |
|---------------------------------------------------------------------------|
| To examine how key socio-economic factors—including GDP per capita, healthy life expectancy, and social support—correlate with the cumulative number of confirmed COVID-19 cases globally. |

---

## Datasets Utilized

| Dataset                            | Description                                                                                      |
|-----------------------------------|--------------------------------------------------------------------------------------------------|
| **COVID-19 Dataset**               | Daily confirmed case counts by country sourced from Johns Hopkins University.                   |
| **World Happiness Report 2020**    | Contains country-level data on GDP per capita, social support, and healthy life expectancy.     |

---

## Methodology

1. **Data Collection and Cleaning**  
   - Acquired global COVID-19 case counts and World Happiness indicators.  
   - Standardized country names and removed missing or inconsistent entries to ensure reliable merging.

2. **Data Integration**  
   - Combined COVID-19 cumulative case data with socio-economic metrics to form a unified dataset suitable for comparative analysis.

3. **Exploratory Data Analysis (EDA)**  
   - Conducted descriptive statistics to understand distributions and detect outliers.  
   - Created scatterplots, line graphs, and heatmaps to visualize relationships between socio-economic factors and COVID-19 case trajectories.

4. **Correlation and Statistical Analysis**  
   - Computed Pearson and Spearman correlation coefficients to quantify associations.  
   - Assessed significance and potential causative trends to evaluate the influence of GDP, social support, and healthy life expectancy on COVID-19 spread.

5. **Visualization and Interpretation**  
   - Developed clear and interpretable visualizations to communicate findings effectively.  
   - Focused on identifying trends that suggest socio-economic resilience may mitigate pandemic severity.

---

## Key Features

- **Comprehensive Data Integration**: Creates a multi-dimensional dataset linking epidemiological and socio-economic information.  
- **Correlation Analysis**: Evaluates the relationships between COVID-19 spread and socio-economic indicators.  
- **Data Visualization**: Generates high-quality figures—including scatterplots, line graphs, and heatmaps—to reveal insights.  

---

## Technologies and Tools

| Tool/Library      | Purpose                                               |
|------------------|-------------------------------------------------------|
| **Python**        | Primary language for data processing and analysis    |
| **Pandas**        | Data manipulation, cleaning, and merging             |
| **NumPy**         | Numerical operations and statistical computations    |
| **Matplotlib**    | Custom visualizations and trend plotting             |
| **Seaborn**       | Enhanced statistical data visualization and styling  |

---

## Visualizations Produced

- Scatterplots comparing GDP per capita against COVID-19 confirmed cases  
- Heatmaps displaying correlation coefficients between variables  
- Line plots of COVID-19 case trajectories overlaid with happiness index metrics  

---

## Key Insights

Analysis indicates potential negative correlations between social support and COVID-19 case growth, suggesting that countries with robust social infrastructures may have experienced slower increases in cases. While GDP per capita exhibited weaker trends, higher healthy life expectancy appeared to be associated with lower cumulative case counts. These findings highlight the potential role of socio-economic resilience in mitigating pandemic impacts.

---

## Future Work

- Expand analysis to include additional socio-economic and demographic indicators, such as population density, healthcare capacity, and government response metrics.  
- Conduct temporal analysis to evaluate how correlations evolve over different pandemic phases.  
- Apply machine learning models to predict case trajectories based on socio-economic and environmental factors.  
- Integrate regional-level datasets to identify intra-country disparities and localized determinants of COVID-19 spread.

---
