# main.py

from fastapi import FastAPI, Query
from scraper import fetch_news
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Brave News Scraper API",
    description="Scrapes Brave News results based on query and returns structured JSON",
    version="1.0.0"
)

# Optional CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Health"])
def read_root():
    return {"status": "running"}
 


@app.get("/news", tags=["Scraper"])
def get_news(query: str = Query(..., description="Search term to fetch Brave News")):
    data = fetch_news(query)
    return {"query": query, "count": len(data), "results": data}
