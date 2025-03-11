import requests
from bs4 import BeautifulSoup
import json

results = []

# ページ1～24までループ
for page in range(1, 25):
    url = f"https://wakasapo.nedo.go.jp/seeds/?sf_paged={page}"
    print(f"Scraping {url}...")
    response = requests.get(url)
    if response.status_code != 200:
        print(
            f"Error: {url} の取得に失敗しました。ステータスコード {response.status_code}"
        )
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    # "search-filter-results" コンテナを取得
    container = soup.find(class_="search-filter-results")
    if not container:
        print(f"ページ {page} に 'search-filter-results' が見つかりませんでした。")
        continue

    items = container.find_all("li")
    if not items:
        items = container.find_all(recursive=False)

    for item in items:
        # タイトルは <span class="seeds_ttl"> 内にある
        title_tag = item.find("span", class_="seeds_ttl")
        title = title_tag.get_text(strip=True) if title_tag else ""

        # リンク（例として最初の <a> タグから抽出）
        a_tag = item.find("a")
        link = a_tag["href"] if a_tag and "href" in a_tag.attrs else ""

        # 説明文（例として最初の <p> タグから抽出）
        p_tag = item.find("p")
        description = p_tag.get_text(strip=True) if p_tag else ""

        results.append({"title": title, "link": link, "description": description})

# 結果を JSON ファイルとして保存
with open("results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("スクレイピング完了。結果は results.json に保存されました。")
