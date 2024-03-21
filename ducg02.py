import requests
from bs4 import BeautifulSoup

# requestsを使用してWebページを取得
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'ja'  # 日本語を受け入れるように指定
}
response = requests.get('https://html.duckduckgo.com/html?q=織田信長&ia=web',headers=headers)

# responseからHTMLを取得
data = response.text
print(data)

# BeautifulSoupオブジェクトの作成
parsed = BeautifulSoup(data, 'html.parser')

# 各検索結果を取得
results = parsed.find_all('div', class_='result')

# 各結果のURLとスニペットを取得
for result in results:
    url_tag = result.find('a', class_='result__url')
    snippet_tag = result.find('a', class_='result__snippet')

    url = url_tag['href'] if url_tag else "URL not found"
    snippet = snippet_tag.text if snippet_tag else "Snippet not found"

    print("URL:", url)
    print("Snippet:", snippet)
    print("---")