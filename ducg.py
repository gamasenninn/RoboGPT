import requests
import urllib

def search_duckduckgo(query):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept-Language': 'ja'  # 日本語を受け入れるように指定
    }

    encoded_query = urllib.parse.quote(query)
    url = f'https://api.duckduckgo.com/?q={encoded_query}&format=json&pretty=1&no_html=1&skip_disambig=1'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(url)
        print(data)
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

# 使用例
search_duckduckgo("織田信長")
