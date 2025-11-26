import pandas as pd

d1 = {'임석현':[100, 99, 98, 97], '박종범':[95,94,100,90], '성수경':[90,95, 89, 88], '이준석':[85,86,87,100]}

df1 = pd.DataFrame(d1, index=['국어', '영어', '수학', '한국사'])

print(df1.info())

# 출력결과
# <class 'pandas.core.frame.DataFrame'> #데이터프레임 객체가 pandas타입임
# Index: 4 entries, 국어 to 한국사 #인덱스는 국어부터 한국사까지 총 4개임
# Data columns (total 4 columns): #컬럼은 모두 4개임
#  #   Column  Non-Null Count  Dtype  
# ---  ------  --------------  -----
#  0   임석현     4 non-null      int64
#  1   박종범     4 non-null      int64
#  2   성수경     4 non-null      int64
#  3   이준석     4 non-null      int64 #각 컬럼의 값이 모두 존재하고 결측치가 없으며 자료형은 모두 64비트 정수형임
# dtypes: int64(4) #총 4개 컬럼 모두 int64
# memory usage: 160.0+ bytes #이 데이터프레임이 사용하는 메모리 용랑은 160바이트임
# None #df.info()는 반환값이 없는 함수이므로 None출력