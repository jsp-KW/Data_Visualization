import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


plt.rcParams['font.family'] = 'NanumGothic' # 한글 폰트 나눔고딕체 설정
 
# csv 파일 읽어오기.
df = pd.read_csv ('나스닥.csv')

# 문자열 값을 숫자로 변환

df["시가"] = df["시가"].str.replace(',','').astype(float)
df["종가"] = df["종가"].str.replace(',','').astype(float)
df["거래량"] = df["거래량"].str.replace('M','e6').str.replace('B','e9').astype(float)

#날짜를 datetime 형식으로 변환하여 x축에 쓰기위함
df["날짜"] = pd.to_datetime(df["날짜"])

#print(df)

# 사이즈 조절
fig,ax1= plt.subplots(figsize=(10, 6))

# 시가와 종가를 그래프로 표시
ax1.plot(df["날짜"],df["시가"], color ="blue", label ="시가")
ax1.plot(df["날짜"], df["종가"], color ="red", label= "종가")
ax1.set_ylabel ("Price")
ax1.set_ylim([df["시가"].min(), df["종가"].max()])

# x축 y축을 공유하기 위하여 쌍둥이 축 생성
ax2 = ax1.twinx()
ax2.bar(df["날짜"], df["거래량"], color= "orange", label= "거래량")
ax2.set_ylabel("volume")
ax2.set_ylim([0,df["거래량"].max()*1.2])


plt.xlabel("월 단위")
plt.ylabel("거래량")
plt.title("나스닥 (2019-2023 Month)")

# 설명을 쓰기위한 legend 함수
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc="upper right")
           
plt.show()
