# Generate functions to ingest data from various sources (e.g., CSV, JSON, databases) and store it in a standardized format for further processing.
import pandas as pd


def ingest_csv(file_path: str) -> pd.DataFrame:
    """
    Ingest data from a CSV file and return it as a pandas DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: The ingested data as a DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully ingested data from {file_path}")
        return df
    except Exception as e:
        print(f"Error ingesting data from {file_path}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

