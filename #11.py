import pandas as pd

d1 = {'임석현':[100, 99, 98, 97], '박종범':[95,94,100,90], '성수경':[90,95, 89, 88], '이준석':[85,86,87,100]}

df1 = pd.DataFrame(d1, index=['국어', '영어', '수학', '한국사'])
print(df1)
print(df1.shape)
print(df1.size)