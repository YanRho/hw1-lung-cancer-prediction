from data_cleaning import load_and_clean_data

# Define the file path
file_path = "Lung Cancer Dataset.csv"

# Load and clean data
cleaned_df = load_and_clean_data(file_path)

# Verify the cleaned dataset
print(cleaned_df.info())
print(cleaned_df.head())

# Proceed with visualization or further analysis
