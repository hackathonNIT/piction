import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dat = np.random.rand(20,4)
df = pd.DataFrame(dat, columns=['baseball','soccer','basketball','golf',])
# df_1 = df.set_index('baseball')
df.index.name = 'Time'

fig = plt.figure(figsize=(12,5))

ax1 = plt.subplot(121)
plt.plot(df.index, df.baseball, label='baseball')
plt.scatter(df.index, df.golf, color='red', label='golf')
ax1.set_title('test')
ax1.set_xlim(0,22)
ax1.set_xlabel('time', fontsize=20)
ax1.set_ylabel('arb units', fontsize=24)
plt.tick_params(labelsize=18)

ax2 =plt.subplot(122)
plt.scatter(df.index, df.basketball, color='red')
ax2.set_title('test_2')
ax2.set_xlim(0,22)
ax2.set_xlabel('time', fontsize=20)
ax2.set_ylabel('basketball', fontsize=24)
plt.tick_params(labelsize=18)

plt.tight_layout()

st.pyplot(fig)