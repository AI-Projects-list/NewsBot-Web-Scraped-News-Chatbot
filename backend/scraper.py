import requests
from bs4 import BeautifulSoup
import sqlite3

def scrape_bbc():
    url = "https://www.bbc.com/news"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    headlines = [h.text for h in soup.select("h3")[:10]]

    conn = sqlite3.connect("news.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS headlines (title TEXT)")
    c.execute("DELETE FROM headlines")
    for h in headlines:
        c.execute("INSERT INTO headlines (title) VALUES (?)", (h,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    scrape_bbc()