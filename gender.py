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

#Count how many women are in the colonies (THAT ARE LABELED)
female_count = df_combined['sex_indicated'].str.lower().value_counts().get('female', 0)
print(female_count)

male_count = df_combined['sex_indicated'].str.lower().value_counts().get('male', 0)  
print(male_count)

#Creating Pie Chart with Labeled Sex Distrubution throughout Mormon Colonies
y = np.array([female_count, male_count])
mylabels = ['Females', 'Males',]
colors = ['pink', 'blue']

total = sum(y)
def autopct_format(pct):
    absolute = round(pct/100.*total)
    return "{:.1f}%\n({:d})".format(pct, absolute)

plt.title("Labeled Sex Distribution Throughout Mormon Colonies")
plt.pie(y, labels=mylabels, colors=colors, autopct=autopct_format)
plt.show()