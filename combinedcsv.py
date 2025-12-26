import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read CSV files
df_combined = pd.read_csv('combined_colonies_data.csv')

#display combined dataframe
print(df_combined)

#create pie chart of sex_indicated distribution
sex_counts = df_combined['sex_indicated'].value_counts()
plt.pie(sex_counts, labels=sex_counts.index, autopct='%1.1f%%')
plt.title('Sex Indicated Distribution')
plt.show()
