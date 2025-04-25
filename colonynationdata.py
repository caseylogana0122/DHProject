import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read CSV files
df_chu = pd.read_csv('chuichupa.csv')
df_diaz = pd.read_csv('diaz.csv')
df_dublan = pd.read_csv('dublan.csv')
df_gar = pd.read_csv('garcia.csv')
df_gua = pd.read_csv('guadaloupe.csv')
df_juarez = pd.read_csv('juarez.csv')
df_pa = pd.read_csv('pancheco.csv')

# Function to determine the last name with the highest frequency across CSV files
def find_highest_frequency_nation():
    csv_files = [
        ('chuichupa.csv', df_chu),
        ('diaz.csv', df_diaz),
        ('dublan.csv', df_dublan),
        ('garcia.csv', df_gar),
        ('guadaloupe.csv', df_gua),
        ('juarez.csv', df_juarez),
        ('pancheco.csv', df_pa)
    ]

    nation_counts = {}

    for file_name, df in csv_files:
        # Adjusted to assume names are in the fourth column
        nation = df.iloc[:, 4]
        for name in nation:
            if name in nation_counts:
                nation_counts[name] += 1
            else:
                nation_counts[name] = 1

    # Find the last name with the highest frequency
    highest_frequency_name = max(nation_counts, key=nation_counts.get)
    highest_frequency_count = nation_counts[highest_frequency_name]

    print(f"The nation of origion with the highest frequency is '{highest_frequency_name}' with {highest_frequency_count} occurrences.")

# Call the function
find_highest_frequency_nation()
