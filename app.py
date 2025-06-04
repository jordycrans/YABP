from flask import Flask, redirect
from datetime import date
import random, json, os

app = Flask(__name__)

URLS_FILE = 'urls.txt'
CACHE_FILE = 'redirect_cache.json'

def load_urls():
    with open(URLS_FILE, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def get_today_url():
    today_str = date.today().isoformat()

    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            cache = json.load(f)
    else:
        cache = {}

    if today_str in cache:
        return cache[today_str]

    urls = load_urls()
    chosen_url = random.choice(urls)
    cache[today_str] = chosen_url

    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f)

    return chosen_url

@app.route('/')
def redirect_to_influencer():
    return redirect(get_today_url(), code=302)

if __name__ == '__main__':
    app.run(debug=True)
