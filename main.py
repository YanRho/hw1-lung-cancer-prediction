from data_cleaning import load_and_clean_data
import visualization as viz

# Define the file path
file_path = "Lung Cancer Dataset.csv"

# Load and clean data
cleaned_df = load_and_clean_data(file_path)

# Verify the cleaned dataset
print(cleaned_df.info())
print(cleaned_df.head())

# Call visualization functions
viz.plot_age_distribution(cleaned_df)
viz.plot_gender_distribution(cleaned_df)
viz.plot_smoking_vs_disease(cleaned_df)
viz.plot_energy_vs_disease(cleaned_df)