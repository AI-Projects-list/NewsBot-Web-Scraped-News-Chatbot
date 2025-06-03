import openai
import sqlite3

openai.api_key = "YOUR_OPENAI_API_KEY"

def get_latest_news():
    conn = sqlite3.connect("news.db")
    c = conn.cursor()
    c.execute("SELECT title FROM headlines")
    news = "\n".join([row[0] for row in c.fetchall()])
    conn.close()
    return news

def chat_with_user(prompt):
    context = "Here are the latest BBC news headlines:\n" + get_latest_news()
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"]