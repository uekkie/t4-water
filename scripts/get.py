import requests
from lxml import html
from lxml import etree
from bs4 import BeautifulSoup

urls = [
  'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=1',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=2',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=3',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=4',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=5',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=6',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=7',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=8',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=9',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=10',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=11',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=12',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=13',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=14',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=15',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=16',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=17',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=18',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=19',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=20',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=21',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=22',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=23',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=24',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=25',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=26',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=27',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=28',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=29',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=30',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=31',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=32',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=33',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=34',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=35',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=36',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=37',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=38',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=39',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=40',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=41',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=42',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=43',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=44',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=45',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=46',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=47',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=48',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=49',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=50',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=51',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=52',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=53',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=54',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=55',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=56',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=57',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=58',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=59',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=60',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=61',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=62',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=63',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=64',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=65',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=66',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=67',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=68',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=69',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=70',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=71',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=72',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=73',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=74',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=75',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=76',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=77',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=78',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=79',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=80',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=81',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=82',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=83',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=84',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=85',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=86',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=87',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=88',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=89',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=90',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=91',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=92',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=93',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=94',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=95',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=96',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=97',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=98',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=99',
'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=100',
]
# スクレイピング対象の URL にリクエストを送り HTML を取得する
url = 'https://water-pub.env.go.jp/water-pub/mizu-site/meisui/data/index.asp?info=100'

res = requests.get(url)
res.encoding = 'shift_jis'  # 文字コード

# レスポンスの HTML から BeautifulSoup オブジェクトを作る
# _soup = BeautifulSoup(res.text, 'html.parser')
soup = html.fromstring(res.text)


content_table = '//body/table[2]/tbody/tr/td'
content = soup.xpath('//body/table')[2]
target = content.xpath('//td')[0]

print(e for e in target)
# result = ''.join(etree.tostring(e) for e in target)
# print(result)

# title_q = '//font[@class="fxl"]'
# title_text = target.xpath(title_q)[0].text
# print(title_text)

# # /html/body/table[2]/tbody/tr/td/table[2]/tbody/tr
# category_place = target.xpath('//tr/td')[0]
# print(category_place.text)

# # place_q = '/html/body/table[2]/tbody/tr/td/table[2]/tbody/tr/td[2]'
# # place_text = soup.xpath(place_q)
# # print(place_text)

# # /html/body/table[2]/tbody/tr/td/table[3]/tbody/tr/td/a
# url_text = target.xpath('//img/@src')[2]
# print(url_text)

# # desc_q  ='/html/body/table[2]/tbody/tr/td/table[3]/tbody/tr/td/span/div'
# # desc_text = soup.xpath(desc_q)
# # print(desc_text)
