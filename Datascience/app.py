import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

x2 = st.slider('Select a value2')
st.write(x2, 'squared is2', x2 * x2)

# Histogram import seaborn as sns

st.subheader('Seaborn distplot of Median Family Income')
plt.figure()
plt.title('County Level Income Distribution')
sns.set(style="ticks")
df = sns.load_dataset("iris")
sns.pairplot(df, hue="species")
#for median family income
# sns.set_style('darkgrid')
# sns.distplot(df['Median Family Income'])
st.pyplot()
