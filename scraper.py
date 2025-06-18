import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re

def normalize_relative_date(date_str):
    now = datetime.now()
    date_str = date_str.lower()
    match = re.search(r'\d+', date_str)
    value = int(match.group()) if match else 0

    if "minute" in date_str:
        return (now - timedelta(minutes=value)).strftime('%Y-%m-%d')
    elif "hour" in date_str:
        return (now - timedelta(hours=value)).strftime('%Y-%m-%d')
    elif "day" in date_str:
        return (now - timedelta(days=value)).strftime('%Y-%m-%d')
    elif "week" in date_str:
        return (now - timedelta(weeks=value)).strftime('%Y-%m-%d')
    elif "month" in date_str:
        return (now - timedelta(days=30 * value)).strftime('%Y-%m-%d')
    elif "year" in date_str:
        return (now - timedelta(days=365 * value)).strftime('%Y-%m-%d')
    return date_str

def fetch_news(query, max_articles=100):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    url = f"https://search.brave.com/news?q={query.replace(' ', '+')}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    news_cards = soup.select("div.snippet")
    structured_data = []

    for card in news_cards:
        title = card.select_one('.snippet-title')
        description = card.select_one('.desc')
        link = card.select_one('a.result-header')
        source = card.select_one('.netloc')
        image = card.select_one('img.svelte-12iz79g')

        date_tags = card.select('.attr')
        date = None
        for tag in date_tags:
            txt = tag.get_text(strip=True)
            if txt != '•':
                date = normalize_relative_date(txt)
                break

        entry = {
            "title": title.get_text(strip=True) if title else None,
            "description": description.get_text(strip=True) if description else None,
            "url": link['href'] if link and link.has_attr('href') else None,
            "source": source.get_text(strip=True) if source else None,
            "date": date,
            "image_url": image['src'] if image and image.has_attr('src') else None
        }

        if any(entry.values()):
            structured_data.append(entry)

        if len(structured_data) >= max_articles:
            break

    return structured_data


