import pandas as pd

def load(path: str) -> pd.DataFrame | None:
    """
    Load a CSV file into a pandas DataFrame.

    Parameters:
        path (str): The file path to the CSV file.
    Returns:
        pd.DataFrame | None: The loaded DataFrame, or None if loading failed.
    """
    try:
        if (path is None or not isinstance(path, str)
            or path == "" or not path.endswith(".csv")):
            raise ValueError("Invalid file path")
        dataset = pd.read_csv(path)
        if dataset.empty:
            raise ValueError("Loaded dataset is empty")
        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: The CSV file is malformed.")
        return None
    except FileNotFoundError:
        print("Error: The file was not found.")
        return None
    except ValueError as ve:
        print(f"Value Error: {ve}")
        return None
    except PermissionError:
        print("Error: Permission denied when accessing the file.")
        return None
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None

