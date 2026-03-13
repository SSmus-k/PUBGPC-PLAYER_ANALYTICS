import matplotlib.pyplot as plt

def create_plots(data):
    # Kill Distribution
    plt.figure(figsize=(8,5))
    plt.hist(data['kills'], bins=range(0, int(data['kills'].max())+2), color='skyblue', edgecolor='black')
    plt.title('Kill Distribution')
    plt.xlabel('Kills')
    plt.ylabel('Number of Matches')
    plt.savefig('outputs/kill_distribution.png')
    plt.close()

    # Damage vs Placement
    plt.figure(figsize=(8,5))
    plt.scatter(data['damage'], data['placement'], color='orange')
    plt.title('Damage vs Placement')
    plt.xlabel('Damage')
    plt.ylabel('Placement')
    plt.gca().invert_yaxis()  # lower placement is better
    plt.savefig('outputs/damage_vs_placement.png')
    plt.close()

    # Performance Trend (kills over matches)
    plt.figure(figsize=(10,5))
    plt.plot(range(1, len(data)+1), data['kills'], marker='o', linestyle='-', color='green')
    plt.title('Kills Trend Over Matches')
    plt.xlabel('Match Number')
    plt.ylabel('Kills')
    plt.savefig('outputs/performance_trend.png')
    plt.close()