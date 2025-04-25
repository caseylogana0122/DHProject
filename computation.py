import pandas as pd
import csv
from collections import Counter
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

#Count how many women are in the colonies (THAT ARE LABELED)
female_count = (df_pa['sex_indicated'].str.lower().value_counts().get('female', 0) + df_chu['sex_indicated'].str.lower().value_counts().get('female', 0) + df_diaz['sex_indicated'].str.lower().value_counts().get('female', 0) + df_dublan['sex_indicated'].str.lower().value_counts().get('female', 0) + df_gar['sex_indicated'].str.lower().value_counts().get('female', 0) + df_gua['sex_indicated'].str.lower().value_counts().get('female', 0) + df_juarez['sex_indicated'].str.lower().value_counts().get('female', 0))
print(female_count)

#Count how many men are in the colonies (THAT ARE LABELED)
male_count = (df_pa['sex_indicated'].str.lower().value_counts().get('male', 0) + df_chu['sex_indicated'].str.lower().value_counts().get('male', 0) + df_diaz['sex_indicated'].str.lower().value_counts().get('male', 0) + df_dublan['sex_indicated'].str.lower().value_counts().get('male', 0) + df_gar['sex_indicated'].str.lower().value_counts().get('male', 0) + df_gua['sex_indicated'].str.lower().value_counts().get('male', 0) + df_juarez['sex_indicated'].str.lower().value_counts().get('male', 0))
print(male_count)

#Creating Pie Chart with Labeled Gender Distrubution throughout Mormon Colonies
y = np.array([female_count, male_count,])
mylabels = ['Females', 'Males',]
colors = ['pink', 'blue']

total = sum(y)
def autopct_format(pct):
    absolute = int(pct/100.*total)
    return "{:.1f}%\n({:d})".format(pct, absolute)

plt.title("Labeled Gender Distribution Throughout Mormon Colonies")
plt.pie(y, labels=mylabels, colors=colors, autopct=autopct_format)
plt.show()

#Count how many times 'female' appears in 'sex_indicated' AND 'married' appears in 'marriage_status'
female_married_count = (
    (df_chu[
        (df_chu['sex_indicated'].str.lower() == 'female') &
        (df_chu['marriage_status'].str.lower() == 'married')
    ].shape[0]) +
    (df_pa[
        (df_pa['sex_indicated'].str.lower() == 'female') &
        (df_pa['marriage_status'].str.lower() == 'married')
    ].shape[0]) +
    (df_diaz[
        (df_diaz['sex_indicated'].str.lower() == 'female') &
        (df_diaz['marriage_status'].str.lower() == 'married')
    ].shape[0]) +
    (df_dublan[
        (df_dublan['sex_indicated'].str.lower() == 'female') &
        (df_dublan['marriage_status'].str.lower() == 'married')
    ].shape[0]) +
    (df_gar[
        (df_gar['sex_indicated'].str.lower() == 'female') &
        (df_gar['marriage_status'].str.lower() == 'married')
    ].shape[0]) +
    (df_gua[
        (df_gua['sex_indicated'].str.lower() == 'female') &
        (df_gua['marriage_status'].str.lower() == 'married')
    ].shape[0]) +
    (df_juarez[
        (df_juarez['sex_indicated'].str.lower() == 'female') &
        (df_juarez['marriage_status'].str.lower() == 'married')
    ].shape[0])
)
print(female_married_count)

#Count how many times 'female' appears in 'sex_indicated' AND 'single' appears in 'marriage_status'
female_single_count = (
    (df_chu[
        (df_chu['sex_indicated'].str.lower() == 'female') &
        (df_chu['marriage_status'].str.lower() == 'single')
    ].shape[0]) +
    (df_pa[
        (df_pa['sex_indicated'].str.lower() == 'female') &
        (df_pa['marriage_status'].str.lower() == 'single')
    ].shape[0]) +
    (df_diaz[
        (df_diaz['sex_indicated'].str.lower() == 'female') &
        (df_diaz['marriage_status'].str.lower() == 'single')
    ].shape[0]) +
    (df_dublan[
        (df_dublan['sex_indicated'].str.lower() == 'female') &
        (df_dublan['marriage_status'].str.lower() == 'single')
    ].shape[0]) +
    (df_gar[
        (df_gar['sex_indicated'].str.lower() == 'female') &
        (df_gar['marriage_status'].str.lower() == 'single')
    ].shape[0]) +
    (df_gua[
        (df_gua['sex_indicated'].str.lower() == 'female') &
        (df_gua['marriage_status'].str.lower() == 'single')
    ].shape[0]) +
    (df_juarez[
        (df_juarez['sex_indicated'].str.lower() == 'female') &
        (df_juarez['marriage_status'].str.lower() == 'single')
    ].shape[0])
)
print(female_single_count)

#Creating Pie Chart with Labeled Gender Distrubution in Chuichupa Colony
y = np.array([female_married_count, female_single_count])
mylabels = ['Married Females', 'Single Females',]
colors = ['pink', 'green']

total = sum(y)
def autopct_format(pct):
    absolute = int(pct/100.*total)
    return "{:.1f}%\n({:d})".format(pct, absolute)

plt.title("Married-to-Single Females Throughout Mormon Colonies")
plt.pie(y, labels=mylabels, colors=colors, autopct=autopct_format)
plt.show()

