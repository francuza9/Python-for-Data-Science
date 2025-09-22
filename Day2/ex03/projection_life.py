import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def display_life_vs_income_projection() -> None:
    """
    Display a scatter plot of life expectancy
    vs income per person for the year 1900.

    Raises:
        ValueError: If datasets are invalid or required data is missing.
    """
    life_expectancy_dataset = load("life_expectancy_years.csv")
    income_dataset = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    )

    if (life_expectancy_dataset is None
       or not isinstance(life_expectancy_dataset, pd.DataFrame)
       or life_expectancy_dataset.empty):
        raise ValueError("Invalid life expectancy dataset")
    if (income_dataset is None
       or not isinstance(income_dataset, pd.DataFrame)
       or income_dataset.empty):
        raise ValueError("Invalid income dataset")

    if "1900" not in life_expectancy_dataset.columns:
        raise ValueError("Year 1900 not found in life expectancy dataset")
    if "1900" not in income_dataset.columns:
        raise ValueError("Year 1900 not found in income dataset")

    life_1900 = life_expectancy_dataset[["country", "1900"]].copy()
    income_1900 = income_dataset[["country", "1900"]].copy()

    life_1900.columns = ["country", "life_expectancy"]
    income_1900.columns = ["country", "gpd_per_capita"]

    merged_data = life_1900.merge(income_1900, on="country", how="inner")

    if merged_data.empty:
        raise ValueError("No matching countries found in both datasets")

    merged_data = merged_data.dropna()

    if merged_data.empty:
        raise ValueError("No valid data after dropping NaN values")

    gdp_values = merged_data["gpd_per_capita"].values
    life_values = merged_data["life_expectancy"].values

    plt.figure(figsize=(12, 8))
    plt.scatter(gdp_values, life_values, alpha=0.6, s=50, color='blue')
    plt.title('1900', fontsize=16, fontweight='bold')
    plt.xlabel('Gross domestic product', fontsize=12)
    plt.ylabel('Life Expectancy', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def main() -> None:
    """
    Main function to display life expectancy vs income projection.

    Handles exceptions and prints error messages.
    """
    try:
        display_life_vs_income_projection()
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
