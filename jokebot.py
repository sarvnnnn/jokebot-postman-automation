import requests
import json

# =============================================
#   JokeBot — Fetch a joke and send to Slack
# =============================================

# 🔧 CONFIG — Paste your Slack webhook URL here
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"

# -----------------------------------------------
# STEP 1: Fetch a random joke
# -----------------------------------------------
def fetch_joke():
    print("Fetching joke...")
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)

    if response.status_code == 200:
        joke = response.json()
        full_joke = f"{joke['setup']} ... {joke['punchline']}"
        print(f"Joke fetched: {full_joke}")
        return full_joke
    else:
        print(f"Failed to fetch joke. Status: {response.status_code}")
        return None

# -----------------------------------------------
# STEP 2: Send joke to Slack
# -----------------------------------------------
def send_to_slack(joke_text):
    print("Sending to Slack...")
    payload = {
        "text": f"😂 *Joke of the Day!*\n{joke_text}"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(SLACK_WEBHOOK_URL, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        print("✅ Joke sent to Slack successfully!")
    else:
        print(f"❌ Failed to send. Status: {response.status_code}, Response: {response.text}")

# -----------------------------------------------
# STEP 3: Run the bot
# -----------------------------------------------
def run_jokebot():
    print("=== JokeBot Starting ===")
    joke = fetch_joke()
    if joke:
        send_to_slack(joke)
    print("=== JokeBot Done ===")

if __name__ == "__main__":
    run_jokebot()
