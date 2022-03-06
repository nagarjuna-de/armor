import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import os
import re

### Changing Excel file to csv file
df = pd.DataFrame(pd.read_excel(r'C:\Users\rnr31\Documents\GitHub\armor\Measurements automation\spikes.xlsx'))
#df.header = None
#print(df)

if st.button('Show data'):
    st.dataframe(df)

if st.button('Show graph'):
    st.line_chart(df['Force [N]'])


type = ['None','triangle', 'Spikes','other']
page = st.radio('Select one', type)

if page == 'triangle':
    st.write(df['Force [N]'].max())


