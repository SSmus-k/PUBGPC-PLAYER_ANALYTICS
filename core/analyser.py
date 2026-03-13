import pandas as pd
import numpy as np

def analyze_data(data):
    print("\n--- Basic Statistics ---")
    print(data.describe())

    # Correlation matrix
    corr = data.corr()
    print("\n--- Correlations ---")
    print(corr)

    # Average stats
    avg_kills = data['kills'].mean()
    avg_damage = data['damage'].mean()
    win_rate = data['win'].mean() if 'win' in data.columns else None

    print(f"\nAverage kills per match: {avg_kills:.2f}")
    print(f"Average damage per match: {avg_damage:.2f}")
    if win_rate is not None:
        print(f"Overall win rate: {win_rate*100:.2f}%")

    return {
        'avg_kills': avg_kills,
        'avg_damage': avg_damage,
        'correlations': corr,
        'win_rate': win_rate
    }