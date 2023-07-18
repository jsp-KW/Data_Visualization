import requests
import datetime
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

plt.rcParams['font.family'] = 'NanumGothic' # 한글 폰트 나눔고딕체 설정
 

url = 'https://coinmarketcap.com/ko/'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

# 선택자를 이용하여
dominance_element = soup.select_one('#__next > div.sc-48e202ed-1.hJWPVO > div.main-content > div.sc-48e202ed-0.CXaXP > div > div:nth-child(2) > div > div.sc-23686b16-0.ijKKTW > div > div.cmc-global-stats__content > div > div:nth-child(5) > a')

if dominance_element:
    dominance_text = dominance_element.get_text(strip=False) # 이어붙이려면 False 값을 True로
    print("코인마켓캡 기준 도미넌스 :" ,dominance_text)
else:
    print("텍스트를 추출할 요소를 찾을 수 없습니다.")

compile_time =  datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

alt_coin_dominance=0

split_dominance = dominance_text.replace(' ','').replace('\xa0',''). split(":")
print(split_dominance)

btc_dominance = float(split_dominance[1].replace('%ETH',''))
eth_dominance = float(split_dominance[2].replace('%',''))
alt_coin_dominance = 100.0 - (btc_dominance+eth_dominance)

# print (btc_dominance)
# print(eth_dominance)
# print(alt_coin_dominance)

labels =  ['BTC', 'ETH', 'Alt Coins']
size = [btc_dominance,eth_dominance,alt_coin_dominance]
colors = ['#F0B429', '#3C873A', '#1D4ED8']
explode = (0.05,0,0)

plt.pie(size, explode=explode,labels=labels,colors=colors, autopct='%1.1f%%',startangle=90)

plt.axis('equal')
plt.title (' Dominance Percentage\n ({})'.format(compile_time))

annotation = "도미넌스의 값은 정확히 일치하지 않을 수 있습니다.(CoinMarketCap)"
plt.text(0.4, -1.3, annotation, horizontalalignment='center', verticalalignment='center')

plt.show()
