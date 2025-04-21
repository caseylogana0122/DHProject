import pandas as pd
import csv
from collections import Counter

#Read CSV file.
df_pa = pd.read_csv('chuichupa.csv')

#Count how many women are in the colony
female_count = df_pa['sex_indicated'].str.lower().value_counts().get('female', 0)
print(female_count)

#Count how many men are in the colony. 
male_count = df_pa['sex_indicated'].str.lower().value_counts().get('male', 0)
print(male_count)

# Count how many times 'female' appears in 'sex_indicated' AND 'single' appears in 'marriage_status'
female_single_count = df_chu[
    (df_pa['sex_indicated'].str.lower() == 'female') &
    (df_pa['marriage_status'].str.lower() == 'single')
].shape[0]
print(female_single_count)
