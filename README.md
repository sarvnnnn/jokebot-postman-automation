# 😂 JokeBot — Postman Automation Project

A beginner-friendly API automation project that fetches a random joke and posts it to a Slack channel automatically using Postman.

---

## 🛠️ Tools Used
- **Postman** — API testing and automation
- **Official Joke API** — Free public API for random jokes
- **Slack Incoming Webhooks** — To post messages into a Slack channel

---

## ⚙️ How It Works
1. Postman sends a **GET request** to the Joke API
2. The API returns a joke in JSON format (setup + punchline)
3. A **Postman script** reads the joke and saves it as `jokeText` variable
4. Postman sends a **POST request** to Slack with the joke
5. The joke appears in the Slack channel automatically

---

## 📁 Project Structure
JokeBot Collection
├── fetch joke (GET) → Fetches random joke from API
└── slackWebhook (POST) → Sends joke to Slack channel

---

## 🚀 Setup Instructions
1. Import `jokebot.postman_collection.json` into Postman
2. Create a Slack App at https://api.slack.com/apps
3. Enable Incoming Webhooks and copy the webhook URL
4. Create a Postman environment with:
   - `slackWebhook` = your Slack webhook URL
   - `jokeText` = (leave empty)
5. Run the collection using Collection Runner

---

## 📸 Output
The joke appears in your Slack channel like this:

😂 Joke of the Day!
What did Romans use to cut pizza before the rolling cutter was invented? ... Lil Caesars

---

## 💡 Concepts Learned
- What is a REST API
- GET vs POST requests
- JSON data format
- Postman environment variables
- Writing test scripts in Postman
- What is a Webhook
- API request chaining using Collection Runner

---

## 🌍 Real World Use Cases
- Send daily reports to a team Slack channel
- Alert team when a server goes down
- Post weather updates every morning
- Notify when a new order arrives on a website

---

## 👨‍💻 Author
**Sarvnn**  
Beginner API Automation Project — Built with Postman + Slack
