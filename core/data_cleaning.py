import pandas as pd
import numpy as np

def clean_data(file_path):
    # Loading the dataset from the source folder
    data = pd.read_csv("./source/player1.csv")

    # Fix the missing values using median for numerical columns and mode for categorical columns
    # Filling the numerical columns with median
    num_cols = ['kills', 'damage', 'placement', 'survival_time', 'headshots']
    for col in num_cols:
        if col in data.columns:
            data[col] = data[col].fillna(data[col].median())

    # Replacing the negative or impossible values with the minimum valid values
    data['kills'] = data['kills'].apply(lambda x: max(x, 0))
    data['damage'] = data['damage'].apply(lambda x: max(x, 0))
    data['placement'] = data['placement'].apply(lambda x: max(x, 1))
    data['survival_time'] = data['survival_time'].apply(lambda x: max(x, 1))
    data['headshots'] = data['headshots'].apply(lambda x: max(x, 0))

    # Removing the extreme outliers (using IQR)
    for col in ['kills', 'damage', 'survival_time', 'headshots']:
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        data[col] = np.where(data[col] > upper, upper, data[col])
        data[col] = np.where(data[col] < lower, lower, data[col])

    # Save cleaned data
    data.to_csv("outputs/cleaned_data.csv", index=False)
    return data