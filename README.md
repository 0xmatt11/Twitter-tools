🤖 Twitter/X Emoji Name Rotator
A simple Python bot that automatically updates your Twitter (X) display name every minute by appending a random, rotating emoji (e.g., YourName 🚀 → YourName 👾).
⚠️ Important Warnings
 * Ban Risk: updating your profile metadata (name/bio) every 60 seconds is aggressive behavior. X/Twitter automated systems may flag this as spam or lock your account. Use at your own risk.
 * API Limits: If you hit a "Rate Limit" (Error 429), the bot is designed to sleep for 15 minutes. Do not try to bypass this, or you will be suspended.
 * Access Tier: You likely need the Basic Tier ($100/mo) of the X Developer API for update_profile endpoints (v1.1) to work reliably, though some legacy Free tier apps may still function.
🚀 Features
 * Updates your profile Display Name automatically.
 * Randomly selects from a curated list of emojis.
 * Handles Rate Limits gracefully (auto-sleeps).
 * Uses .env for secure API key storage.
🛠️ Prerequisites
 * Python 3.7+ installed on your machine.
 * An X Developer Account with a Project & App set up.
 * Read and Write Permissions enabled in your App settings.
📦 Installation
 * Clone or download this repository.
 * Install the required libraries:
   pip install tweepy python-dotenv

🔑 Configuration
 * Create a file named .env in the project root directory.
 * Paste your X API credentials inside (no spaces around the =):
   API_KEY=your_consumer_key_here
API_KEY_SECRET=your_consumer_key_secret_here
ACCESS_TOKEN=your_access_token_here
ACCESS_TOKEN_SECRET=your_access_token_secret_here

 * Edit the script (name_bot.py):
   * Find the line BASE_NAME = "YourName"
   * Change "YourName" to the name you want to keep static (e.g., "Fionna").
🏃‍♂️ Usage
Run the bot using Python:
python name_bot.py

To stop the bot, press CTRL + C in your terminal.
📋 Troubleshooting
| Error | Cause | Solution |
|---|---|---|
| 401 Unauthorized | Keys are wrong or permissions are stale. | Regenerate Keys & Tokens in Developer Portal. Ensure you generated them after setting permissions to "Read & Write". |
| 403 Forbidden | Wrong Access Level. | You likely need the Basic Tier subscription. The Free Tier is mostly Write-Only for tweets, not profile updates. |
| 429 Too Many Requests | You updated it too fast. | The bot will automatically sleep for 15 minutes.
