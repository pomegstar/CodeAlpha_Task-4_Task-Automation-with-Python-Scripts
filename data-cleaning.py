# Handle missing values: Drop rows with missing data
# Remove duplicates: Automatically removes duplicate rows.
# Standardize columns: Makes column names uniform (lowercase, no spaces).

import pandas as pd

# Load the CSV file
def load_data(file_path):
    try:
        # Attempt to read the CSV file using the 'latin1' encoding
        df = pd.read_csv(file_path, encoding='latin1', engine='python')
        print(f"Data loaded successfully! Shape: {df.shape}")
        return df
    except FileNotFoundError:
        print("File not found. Please check the path.")
        return None
    except UnicodeDecodeError:
        print("There was an encoding error. Please check the file encoding.")
        return None


# Handle missing values
def handle_missing_values(df):
    # Option 1: Drop rows with missing values
    df_cleaned = df.dropna()

    # Option 2: Fill missing values with mean, median, or specific value
    # df_cleaned = df.fillna(df.mean())  # Example for numeric columns
    print(f"Handled missing values. Shape: {df_cleaned.shape}")
    return df_cleaned

# Remove duplicates
def remove_duplicates(df):
    df_cleaned = df.drop_duplicates()
    print(f"Removed duplicates. Shape: {df_cleaned.shape}")
    return df_cleaned

# Standardize column names
def standardize_columns(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    print("Standardized column names.")
    return df


# Save the cleaned dataset
def save_cleaned_data(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}.")

# Main function to automate the cleaning process
def automate_data_cleaning(file_path, output_path):
    df = load_data(file_path)
    if df is not None:
        df = handle_missing_values(df)
        df = remove_duplicates(df)
        df = standardize_columns(df)
        save_cleaned_data(df, output_path)

if __name__ == "__main__":
    # Input and output file paths
    input_file = 'data.csv'  # Replace with your actual file path
    output_file = 'cleaned_data.csv'

    # Automate the data cleaning process
    automate_data_cleaning(input_file, output_file)
