import pandas as pd
import csv
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

#Read CSV file.
df_juarez = pd.read_csv('juarez.csv')

#Count how many women are in the colony
female_count = df_juarez['sex_indicated'].str.lower().value_counts().get('female', 0)
print(female_count)

#Count how many men are in the colony. 
male_count = df_juarez['sex_indicated'].str.lower().value_counts().get('male', 0)
print(male_count)

# Count how many times 'female' appears in 'sex_indicated' AND 'single' appears in 'marriage_status'
female_single_count = df_juarez[
    (df_juarez['sex_indicated'].str.lower() == 'female') &
    (df_juarez['marriage_status'].str.lower() == 'single')
].shape[0]
print(female_single_count)

y = np.array([female_count, male_count])
mylabels = ['Females', 'Males']
plt.pie(y, labels=mylabels)
plt.show()




