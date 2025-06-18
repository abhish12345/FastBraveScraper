# BraveNewsAPI 🚀

A FastAPI-based web service to fetch and serve news articles from Brave Search News using web scraping.  
It uses `requests` + `BeautifulSoup` for fast scraping and supports querying up to 100 articles (or as many Brave provides).

---

## Features 🌟
✅ Fetch news articles by query term  
✅ Get structured data: title, description, URL, source, date, image URL  
✅ Lightweight and fast (no Selenium)  
✅ Easily extensible  

---

## How it works 🔍

- Sends a request to Brave Search News for the given query
- Parses the returned HTML for news snippets
- Normalizes relative dates (e.g. `2 hours ago` → `2025-06-18`)
- Returns JSON data

---

## Installation ⚙️

1️⃣ Clone this repository  
```bash
https://github.com/abhish12345/FastBraveScraper
cd bravenewsapi
pip install -r requirements.txt
python run_server.py

