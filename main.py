from core.data_cleaning import clean_data
from core.analyser import analyze_data
from core.visualization import create_plots

def main():
    data = clean_data("source/player1.csv")
    analyze_data(data)
    create_plots(data)

if __name__ == "__main__":
    main()