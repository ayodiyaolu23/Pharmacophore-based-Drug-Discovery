import os
import pandas as pd

def convert_feather_to_txt(feather_file, txt_file):
    """
    Convert a Feather file containing chemical SMILES to a tab-delimited text file.
    
    Args:
    feather_file (str): Path to the input .feather file.
    txt_file (str): Path to the output .txt file.
    
    Returns:
    None
    """
    try:
        
        if not os.path.exists(feather_file):
            raise FileNotFoundError(f"File {feather_file} not found.")
        
        df = pd.read_feather(feather_file)
        print("Column names in the Feather file:", df.columns.tolist())
        
        if df.empty:
            raise ValueError(f"The file {feather_file} is empty.")
        
        smiles_column = 'smiles' 
        
        if smiles_column not in df.columns:
            raise KeyError(f"The file {feather_file} does not contain a '{smiles_column}' column.")
        
        if not txt_file.endswith('.txt'):
            raise ValueError("The output file must have a '.txt' extension.")
        
        # Save DataFrame to a tab-separated .txt file
        df.to_csv(txt_file, sep='\t', index=False)
        print(f"Successfully converted {feather_file} to {txt_file}")
    
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    feather_file = 'DB.smiles.feather'  # Path to your input Feather file
    txt_file = 'db-output.txt'          # Path to your desired output .txt file
    convert_feather_to_txt(feather_file, txt_file)

