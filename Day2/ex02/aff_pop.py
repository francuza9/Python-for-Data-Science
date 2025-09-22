import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def parse_population_value(value) -> float:
    if pd.isna(value):
        raise ValueError("Population value is NaN")
    str_value = str(value).strip()
    try:
        return float(str_value)
    except ValueError:
        pass
    multiplier = 1
    if str_value.endswith('K'):
        multiplier = 1_000
        str_value = str_value[:-1]
    elif str_value.endswith('M'):
        multiplier = 1_000_000
        str_value = str_value[:-1]
    elif str_value.endswith('B'):
        multiplier = 1_000_000_000
        str_value = str_value[:-1]
    elif str_value.endswith('T'):
        multiplier = 1_000_000_000_000
        str_value = str_value[:-1]
    try:
        numeric_part = float(str_value)
        return numeric_part * multiplier
    except ValueError:
        raise ValueError(f"Cannot parse population value: {value}")

def display_population_comparison(
    dataset: pd.DataFrame,
    my_country_name: str,
    other_country_name: str
) -> None:
    """
    Display the population projections for two given countries.

    Parameters:
        dataset (pd.DataFrame): The dataset containing population data.
        my_country_name (str): The name of
            the first country to display data for.
        other_country_name (str): The name of
            the second country to display data for.
    Raises:
        ValueError: If the dataset is invalid or either country is not found.
    """
    if (dataset is None or not isinstance(dataset, pd.DataFrame)
            or dataset.empty):
        raise ValueError("Invalid dataset")
    if (my_country_name is None or not isinstance(my_country_name, str)
            or my_country_name == ""):
        raise ValueError("Invalid country name")
    if (other_country_name is None or not isinstance(other_country_name, str)
            or other_country_name == ""):
        raise ValueError("Invalid country name")
    if 'country' not in dataset.columns:
        raise ValueError("Dataset must contain 'country' column")
    if my_country_name not in dataset["country"].values:
        raise ValueError(f"Country '{my_country_name}' not found in data")
    if other_country_name not in dataset["country"].values:
        raise ValueError(f"Country '{other_country_name}' not found in data")
    my_country_data = dataset[dataset["country"] == my_country_name]
    other_country_data = dataset[dataset["country"] == other_country_name]

    available_years = [col for col in dataset.columns
                       if col != "country" and col.isdigit()]
    available_years = [int(year) for year in available_years]
    years = [year for year in available_years if 1800 <= year <= 2050]
    if not years:
        raise ValueError("No valid years available in the dataset")
    years.sort()

    my_country_population = []
    other_country_population = []

    for year in years:
        my_population_raw = my_country_data[str(year)].iloc[0]
        other_population_raw = other_country_data[str(year)].iloc[0]
        try:
            my_population = parse_population_value(my_population_raw)
        except ValueError as e:
            raise ValueError(f"Invalid population data for {my_country_name} in year {year}: {e}")
        try:
            other_population = parse_population_value(other_population_raw)
        except ValueError as e:
            raise ValueError(f"Invalid population data for {other_country_name} in year {year}: {e}")
        my_country_population.append(my_population)
        other_country_population.append(other_population)

    plt.figure(figsize=(12, 8))
    plt.plot(years, my_country_population, linewidth=2,
             color='green', label=my_country_name)
    plt.plot(years, other_country_population, linewidth=2,
             color='blue', label=other_country_name)
    plt.title("Population Projections",
              fontsize=16, fontweight='bold')
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Population', fontsize=12)
    plt.legend(fontsize=12, loc='lower right')
    plt.grid(True, alpha=0.3)
    plt.ticklabel_format(style='scientific', axis='y', scilimits=(0, 0))
    plt.tight_layout()
    plt.show()


def main() -> None:
    """
    Main function to load dataset and display
    population comparison for two countries.

    Handles exceptions and prints error messages.
    """
    my_country_name = "France"
    other_country_name = "Belgium"
    try:
        dataset = load("population_total.csv")
        display_population_comparison(dataset, my_country_name,
                                      other_country_name)
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
