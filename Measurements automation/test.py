import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import re

### Changing Excel file to csv file
df = pd.DataFrame(pd.read_excel(r'C:\Users\rnr31\Documents\GitHub\armor\Measurements automation\spikes.xlsx'))

print(df.head())
print(len(df['Force [N]']))
# print(df['Force [N]'].iloc[2])
# plt.plot(df['Force [N]'])
# plt.show()
i=0
a =0
k=0
emp_list = []
spike_list = []
while i < (len(df['Force [N]'])):
    a= df['Force [N]'].iloc[i]
    emp_list.append(a)
    if a>=2 and a<=emp_list[k]:
        spike_list.append(emp_list[k-1])
        i = i+1
        k = k+1
    else:
        i = i+1
        k= k+1
    

print(spike_list)


