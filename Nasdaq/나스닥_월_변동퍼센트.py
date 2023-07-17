import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumGothic' # 폰트 설정

df = pd.read_csv('나스닥.csv')

df['날짜'] = pd.to_datetime(df['날짜'])
df['변동 %'] = df['변동 %'].str.replace('%', '').astype(float)


# 변동폭은 음수도 있으므로 bar를 이용하여
plt.figure(figsize=(10, 6))
plt.bar(df['날짜'], df['변동 %'], width = 5.0 ,color='Green')
plt.xlabel('달 (2019~2023년)')
plt.ylabel('월 별 변동률 %')
plt.title('나스닥 변동률 % (Month)')
plt.xticks(rotation=45)
plt.show()
