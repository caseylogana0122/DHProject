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
def find_highest_frequency_last_name():
    csv_files = [
        ('chuichupa.csv', df_chu),
        ('diaz.csv', df_diaz),
        ('dublan.csv', df_dublan),
        ('garcia.csv', df_gar),
        ('guadaloupe.csv', df_gua),
        ('juarez.csv', df_juarez),
        ('pancheco.csv', df_pa)
    ]

    last_name_counts = {}

    for file_name, df in csv_files:
        # Adjusted to assume names are in the second column
        last_names = df.iloc[:, 1]
        for name in last_names:
            if name in last_name_counts:
                last_name_counts[name] += 1
            else:
                last_name_counts[name] = 1

    # Find the last name with the highest frequency
    highest_frequency_name = max(last_name_counts, key=last_name_counts.get)
    highest_frequency_count = last_name_counts[highest_frequency_name]

    print(f"The last name with the highest frequency is '{highest_frequency_name}' with {highest_frequency_count} occurrences.")

# Call the function
find_highest_frequency_last_name()

#generates a list of the highest frequency last names from each CSV file.
df = biggest_family = pd.concat([
    df_chu[df_chu['last_name'].str.lower() == 'johnson'],
    df_pa[df_pa['last_name'].str.lower() == 'johnson'],
    df_diaz[df_diaz['last_name'].str.lower() == 'johnson'],
    df_dublan[df_dublan['last_name'].str.lower() == 'johnson'],
    df_gar[df_gar['last_name'].str.lower() == 'johnson'], 
    df_gua[df_gua['last_name'].str.lower() == 'johnson'], 
    df_juarez[df_juarez['last_name'].str.lower() == 'johnson']
])

print(biggest_family)

df.to_csv('biggest_family.csv', index=False)
# This will create a new CSV file named 'biggest_family.csv' with the combined data.