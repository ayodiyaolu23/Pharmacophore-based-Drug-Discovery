import os
import pandas as pd

def inspect_feather_file(feather_file):
    """
    Inspect the columns of the Feather file to find the correct column for SMILES.
    
    Args:
    feather_file (str): Path to the input .feather file.
    
    Returns:
    None
    """
    try:
        # Check if the input file exists
        if not os.path.exists(feather_file):
            raise FileNotFoundError(f"File {feather_file} not found.")
        
        # Load the .feather file into a DataFrame
        df = pd.read_feather(feather_file)
        
        # Print the column names for inspection
        print("Column names in the Feather file:", df.columns.tolist())
        
        # Print the first few rows of the data for further inspection
        print("First few rows of the Feather file:\n", df.head())
    
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    feather_file = 'DB.smiles.feather'  # Path to your input Feather file
    inspect_feather_file(feather_file)

