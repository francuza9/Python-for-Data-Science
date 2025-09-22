import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def display_aff_life(dataset: pd.DataFrame, country_name: str) -> None:
	if dataset is None or not isinstance(dataset, pd.DataFrame) or dataset.empty:
		raise ValueError("Invalid dataset")
	if country_name is None or not isinstance(country_name, str) or country_name == "":
		raise ValueError("Invalid country name")
	if country_name not in dataset["country"].values:
		raise ValueError(f"Country '{country_name}' not found in dataset columns")
	country_data = dataset[dataset["country"] == country_name]
	if country_data.empty:
		raise ValueError(f"No data available for country '{country_name}'")
	# Extract years from the dataset columns
	years = [col for col in dataset.columns if col != "country" and col.isdigit()]
	years = [int(year) for year in years]
	years.sort()
	# Extract life expectancy values for the specified country
	life_expectancy_years = []
	for year in years:
		value = country_data[str(year)].iloc[0]
		life_expectancy_years.append(value)
	
	plt.figure(figsize=(12, 6))
	plt.plot(years, life_expectancy_years, linewidth=2, color='blue')
	plt.title(f'{country_name} Life Expectancy Projections', fontsize=16, fontweight='bold')
	plt.xlabel('Year', fontsize=12)
	plt.ylabel('Life Expectancy (years)', fontsize=12)
	plt.grid(True, alpha=0.3)
	plt.tight_layout()
	plt.show()



def main() -> None:
	dataset = load("life_expectancy_years.csv")
	country_name = "France"
	display_aff_life(dataset, country_name)
	

if __name__ == "__main__":
	main()
