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

    container = soup.find(class_="seeds-list")
    if not container:
        print(f"ページ {page} に 'seeds-list' が見つかりませんでした。")
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

        p_tag = item.find("span", class_="seeds_example")
        description = p_tag.get_text(strip=True) if p_tag else ""

        detail_tag = item.find("figcaption")
        detail = detail_tag.get_text(strip=True) if detail_tag else ""

        results.append({"title": title,
                        "link": link, "description": description, "detail": detail})

# 結果を JSON ファイルとして保存
with open("results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("スクレイピング完了。結果は results.json に保存されました。")
