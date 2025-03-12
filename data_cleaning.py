import pandas as pd

def load_and_clean_data(file_path):
    """
    Loads and cleans the Lung Cancer dataset.
    
    Args:
    file_path (str): Path to the dataset CSV file.
    
    Returns:
    pd.DataFrame: Cleaned dataset.
    """
    # Load dataset
    df = pd.read_csv(file_path)

    # Convert target variable to binary
    df["PULMONARY_DISEASE"] = df["PULMONARY_DISEASE"].map({"YES": 1, "NO": 0})

    # Ensure binary categorical columns contain only 0 and 1
    binary_columns = [
        "GENDER", "SMOKING", "FINGER_DISCOLORATION", "MENTAL_STRESS",
        "EXPOSURE_TO_POLLUTION", "LONG_TERM_ILLNESS", "IMMUNE_WEAKNESS",
        "BREATHING_ISSUE", "ALCOHOL_CONSUMPTION", "THROAT_DISCOMFORT",
        "CHEST_TIGHTNESS", "FAMILY_HISTORY", "SMOKING_FAMILY_HISTORY", "STRESS_IMMUNE"
    ]
    df[binary_columns] = df[binary_columns].applymap(lambda x: 1 if x > 0 else 0)

    # Handle numerical outliers using percentile capping
    def cap_outliers(series, lower_percentile=0.01, upper_percentile=0.99):
        lower_bound, upper_bound = series.quantile([lower_percentile, upper_percentile])
        return series.clip(lower_bound, upper_bound)

    df["ENERGY_LEVEL"] = cap_outliers(df["ENERGY_LEVEL"])
    df["OXYGEN_SATURATION"] = cap_outliers(df["OXYGEN_SATURATION"])

    return df
