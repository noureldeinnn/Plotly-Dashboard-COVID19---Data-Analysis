# COVID-19 Data Analysis and Visualization Dashboard

## Overview

This project focuses on analyzing and visualizing COVID-19 data using Google Colab and Plotly Dash. The goal is to explore the data, perform in-depth analysis, and present findings through an interactive dashboard.

## Features

- **Data Sources**: The project utilizes five CSV files, including:
  - Country-wise data
  - Day-wise data
  - Worldwide meter data
  - Full-group USA data
  - COVID-19 clean and complete data

- **Exploratory Data Analysis (EDA)**:
  - Initial analysis conducted in **Google Colab**.
  - Used the *country-wise* and *day-wise* datasets for detailed analysis.
  - Handled extreme values (outliers) to clean the data.
  - Visualized data using Seaborn and Matplotlib to uncover patterns and trends.

- **Interactive Visualizations**:
  - Created dynamic graphs using **Plotly** for a more hands-on experience.
  - Graph types include:
    - **Sunburst Chart**
    - **Line Graphs**
    - **Area Graphs**
    - **Pie Charts**

- **Dynamic Dashboard**:
  - Built with Plotly Dash to combine visualizations into an interactive interface.
  - Allows users to explore data insights in real time.

## Tools and Technologies

- **Programming Language**: Python
- **Libraries**:
  - Pandas: For data manipulation
  - Seaborn & Matplotlib: For initial EDA visualizations
  - Plotly: For interactive and dynamic visualizations
  - Dash: To build the web-based dashboard

## Workflow

1. **Google Colab**:
   - Uploaded the five CSV files and analyzed the data using Pandas.
   - Conducted EDA, cleaned outliers, and visualized data using Seaborn and Matplotlib.

2. **Python Script**:
   - Exported the Colab notebook as a `.py` file (`COVID.py`).
   - This script contains all data analysis and visualization steps performed earlier.

3. **Dashboard Creation**:
   - Used the `app.py` file to:
     - Call visualizations from `COVID.py`.
     - Create an interactive dashboard using Plotly Dash.
   - The dashboard integrates all visualizations for a seamless user experience.



