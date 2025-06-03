# NewsBot – Web-Scraped News Chatbot

## 💡 Description
This project scrapes the latest BBC news headlines and allows users to interact with the data through a chatbot.

## 📦 Tech Stack
- Python (Flask, BeautifulSoup, SQLite)
- React (frontend)
- OpenAI API (GPT-3.5)
- Docker-ready (optional)

## 🔧 Setup Instructions

### Backend
```bash
cd backend
pip install -r requirements.txt
python scraper.py  # Scrape latest news
python app.py      # Run Flask server
```

### Frontend
```bash
cd frontend
npm install
npm start
```

## 🧠 Example Prompt
> "Tell me the latest news"

The chatbot will return summarized info from the latest scraped headlines.