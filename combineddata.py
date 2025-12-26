import pandas as pd
import numpy as np

#read CSV files
df_chu = pd.read_csv('chuichupa.csv')
df_diaz = pd.read_csv('diaz.csv')
df_gua = pd.read_csv('guadaloupe.csv')
df_dublan = pd.read_csv('dublan.csv')
df_gar = pd.read_csv('garcia.csv')
df_juarez = pd.read_csv('juarez.csv')
df_pa = pd.read_csv('pancheco.csv')

#combine dataframes
df_combined = pd.concat([df_chu, df_diaz, df_gua, df_dublan, df_gar, df_juarez, df_pa], ignore_index=True)

#display combined dataframe
print(df_combined)

#order by Colony and sex_indicated
df_combined = df_combined.sort_values(by=['colony', 'sex_indicated'])

#export combined dataframe to CSV
df_combined.to_csv('combined_colonies_data.csv', index=False)
