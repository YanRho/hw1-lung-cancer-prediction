import matplotlib.pyplot as plt
import seaborn as sns

def plot_age_distribution(df):
    """Plots the distribution of patient ages."""
    plt.figure(figsize=(8, 5))
    sns.histplot(df["AGE"], bins=30, kde=True)
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.title("Age Distribution of Patients")
    plt.show()

def plot_gender_distribution(df):
    """Plots the distribution of gender in the dataset."""
    plt.figure(figsize=(6, 4))
    sns.countplot(x="GENDER", data=df, palette="coolwarm")
    plt.xticks([0, 1], ["Female", "Male"])
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.title("Gender Distribution")
    plt.show()

def plot_smoking_vs_disease(df):
    """Plots the relationship between smoking and pulmonary disease."""
    plt.figure(figsize=(6, 4))
    sns.countplot(x="SMOKING", hue="PULMONARY_DISEASE", data=df, palette="coolwarm")
    plt.xticks([0, 1], ["Non-Smoker", "Smoker"])
    plt.xlabel("Smoking Status")
    plt.ylabel("Count")
    plt.title("Smoking vs. Pulmonary Disease")
    plt.legend(["No Disease", "Has Disease"])
    plt.show()

def plot_energy_vs_disease(df):
    """Plots energy levels against pulmonary disease status."""
    plt.figure(figsize=(8, 5))
    sns.boxplot(x="PULMONARY_DISEASE", y="ENERGY_LEVEL", data=df, palette="coolwarm")
    plt.xticks([0, 1], ["No Disease", "Has Disease"])
    plt.xlabel("Pulmonary Disease")
    plt.ylabel("Energy Level")
    plt.title("Energy Level vs. Pulmonary Disease")
    plt.show()
