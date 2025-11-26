import pandas as pd
import numpy as np

d1 = {'임석현':[100, 99, 98, 97], '박종범':[95,94,100,90], '성수경':[90,95, 89, 88], '이준석':[85,86,87,100]}

df1 = pd.DataFrame(d1, index=['국어', '영어', '수학', '한국사'])

df1.iloc[3, 0] = 95
df1.loc["수학", "박종범"] = 80
df1.loc['국어', '임석현'] = np.nan
df1.loc['영어', '박종범'] = np.nan
df1.loc['수학', '성수경'] = np.nan

df1[df1.isna()] = 90

print(df1.sort_values(by='임석현'))