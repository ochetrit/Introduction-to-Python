from load_csv import load
import matplotlib.pyplot as plt


def main():
    db = load("life_expectancy_years.csv")
    db.set_index("country", inplace=True)
    series = db.loc["France"]
    # plt.plot(series.index, series.values)
    # plt.title("France Life expectancy Projections")
    # plt.show()
    series.plot(kind="line", title="France Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    try:
        plt.show()
    except KeyboardInterrupt:
        print("\033[1;93m\nProgram has been closed with Ctrl+C.")


if __name__ == "__main__":
    main()
