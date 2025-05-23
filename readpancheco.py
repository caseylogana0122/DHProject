import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read CSV file.
df_pa = pd.read_csv('pancheco.csv')

# Clean the 'sex_indicated' and 'marriage_status' columns to ensure consistent formatting
df_pa['sex_indicated'] = df_pa['sex_indicated'].str.strip().str.lower().fillna('unknown')
df_pa['marriage_status'] = df_pa['marriage_status'].str.strip().str.lower().fillna('unknown')

#Count how many women are in the colony
female_count = df_pa['sex_indicated'].str.lower().value_counts().get('female', 0)
print("Total labeled females in Colony Pancheco:", female_count)

#Count how many men are in the colony. 
male_count = df_pa['sex_indicated'].str.lower().value_counts().get('male', 0)
print("Total labeled males in Colony Pancheco:",male_count)

#Count how mnay times 'female' appears in 'sex_indicated' AND 'married' appears in 'marriage_status'
female_married_count = df_pa[
    (df_pa['sex_indicated'].str.lower() == 'female') &
    (df_pa['marriage_status'].str.lower() == 'married')
].shape[0]
print("Total labeled married females in Colony Pancheco:", female_married_count)

# Count how many times 'female' appears in 'sex_indicated' AND 'single' appears in 'marriage_status'
female_single_count = df_pa[
    (df_pa['sex_indicated'].str.lower() == 'female') &
    (df_pa['marriage_status'].str.lower() == 'single')
].shape[0]
print("Total labeled single females in Colony Pancheco:", female_single_count)

# Count how many times 'male' appears in 'sex_indicated' AND 'single' appears in 'marriage_status'
male_single_count = df_pa[
    (df_pa['sex_indicated'].str.lower() == 'male') &
    (df_pa['marriage_status'].str.lower() == 'single')
].shape[0]
print("Total labeled singled males in Colony Pancheco:", male_single_count)

# Count how many times 'male' appears in 'sex_indicated' AND 'married' appears in 'marriage_status'
male_married_count = df_pa[
    (df_pa['sex_indicated'].str.lower() == 'male') &
    (df_pa['marriage_status'].str.lower() == 'married')
].shape[0]
print("Total labeled married males in Colony Pancheco:", male_married_count)

#Creating Pie Chart with Total Sex Distrubution in Juarez Colony
y = np.array([female_count, male_count,])
mylabels = ['Females', 'Males',]
colors = ['pink', 'blue']

total = sum(y)
def autopct_format(pct):
    absolute = round(pct/100.*total)
    return "{:.1f}%\n({:d})".format(pct, absolute)

plt.title("Total Sex Distribution in Colony Pancheco")
plt.pie(y, labels=mylabels, colors=colors, autopct=autopct_format)
plt.show()

#Creating Pie Chart with Married to Single Sex Distrubution in Juarez Colony
y = np.array([female_married_count, male_married_count,male_single_count,female_single_count])
mylabels = ['Married Females', 'Married Males' , 'Single Males', 'Single Females']
myexplode = (0,0,0.1,0.1)  # explode the 3rd and 4th slice
colors = ['pink', 'blue', 'green', 'orange']

total = sum(y)
def autopct_format(pct):
    absolute = round(pct/100.*total)
    return "{:.1f}%\n({:d})".format(pct, absolute)

plt.title("Married-to-Single Distribution in Colony Pancheco")
plt.pie(y, labels=mylabels, explode=myexplode, colors=colors, autopct=autopct_format)
plt.show()

