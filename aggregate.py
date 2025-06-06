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

#Combine all dataframes into one
df_combined = pd.concat([df_chu, df_diaz, df_dublan, df_gar, df_gua, df_juarez, df_pa], ignore_index=True)

# Function to determine the last name with the highest frequency across CSV files
def find_highest_frequency_last_name():
    last_name_counts = df_combined['last_name'].value_counts()
    
    # Find the last name with the highest frequency
    highest_frequency_name = last_name_counts.idxmax()
    highest_frequency_count = last_name_counts.max()

    print(f"The last name with the highest frequency is '{highest_frequency_name}' with {highest_frequency_count} occurrences.")

# Call the function
find_highest_frequency_last_name()











