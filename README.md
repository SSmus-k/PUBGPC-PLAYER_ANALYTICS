PUBG Player Performance Analysis
Project Overview

This project analyzes player performance data from PUBG: Battlegrounds using Python and common data science libraries. It focuses on exploring trends in kills, damage, placement, survival time, and headshots to provide insights into player performance.

Features

Data cleaning and preprocessing (handling missing values, correcting negatives, detecting outliers)

Statistical analysis (average kills, damage, win rate, correlations)

Visualizations:

Kill distribution histogram

Damage vs placement scatter plot

Performance trends over matches

Survival time vs placement

Headshots vs kills

Boxplots for kills and damage

Modular Python scripts (data_cleaning.py, analysis.py, visualization.py)

Notebook (exploration.ipynb) for step-by-step experimentation

Folder Structure
PUBGPC_PLAYER_ANALYTICS/
│
├── core/
│   ├── data_cleaning.py
│   ├── analysis.py
│   └── visualization.py
│
├── source/
│   └── player1.csv          # Raw dataset
│
├── outputs/
│   ├── cleaned_data.csv
│   ├── kill_distribution.png
│   ├── damage_vs_placement.png
│   └── performance_trend.png
│
├── notebooks/
│   └── exploration.ipynb
│
├── main.py
├── requirements.txt
└── README.md
Installation

Clone the repository:

git clone https://github.com/SSmus-k/PUBGPC-PLAYER_ANALYTICS

Navigate to the project folder:

cd PUBGPC_PLAYER_ANALYTICS

Install dependencies:

pip install -r requirements.txt
Usage

Run the main script to clean the data, analyze it, and generate visualizations:

python main.py

Cleaned data will be saved to outputs/cleaned_data.csv

Plots will be saved in the outputs/ folder

For step-by-step experimentation and exploration, open the Jupyter Notebook:

jupyter notebook notebooks/exploration.ipynb
Libraries Used

Python 3.x

Pandas

NumPy

Matplotlib

SciPy (optional for statistical analysis)

Observations (Sample)

Average kills per match: X

Average damage per match: Y

Kill and damage trends over time

Correlation between damage and placement

Win probability analysis

(Replace X and Y with actual computed values from your dataset.)

Future Work

Extend analysis to multiple players or teams

Add machine learning models to predict placement or win probability

Include advanced visualizations like heatmaps or 3D plots

License

This project is for educational purposes only.
