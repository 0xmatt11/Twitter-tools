import tweepy
import os
import random
import time
from dotenv import load_dotenv

# Load API keys
load_dotenv()

# --- CONFIGURATION ---
BASE_NAME = "YourName"  # Change this to your actual name
# ---------------------

# Authenticate to X (Twitter)
# Note: Profile updates still largely rely on API v1.1, so we use 'tweepy.API'
auth = tweepy.OAuthHandler(os.getenv("API_KEY"), os.getenv("API_KEY_SECRET"))
auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
api = tweepy.API(auth)

# List of emojis
EMOJI_LIST = [
    "🤖", "👾", "🚀", "🌙", "⭐", "🔥", "💿", "💾", "📡", "🔋",
    "🕹️", "🖥️", "⚡", "🕶️", "🦾", "🌌", "🧬", "🧪", "🧿", "💎"
]

def update_profile_name():
    """Updates the Twitter Display Name with a random emoji."""
    while True:
        try:
            # 1. Pick a random emoji
            emoji = random.choice(EMOJI_LIST)
            
            # 2. Create the new name string (e.g., "Gemini 🚀")
            new_name = f"{BASE_NAME} {emoji}"
            
            # 3. Update the profile (API v1.1)
            api.update_profile(name=new_name)
            
            print(f"✅ Profile name updated to: {new_name}")
            
            # 4. Wait for 60 seconds
            print("⏳ Waiting 60 seconds...")
            time.sleep(60)

        except tweepy.errors.TooManyRequests:
            print("⚠️ Rate Limit Hit! Sleeping for 15 minutes to cool down...")
            time.sleep(900)  # Sleep 15 mins
            
        except Exception as e:
            print(f"❌ Error: {e}")
            # If a critical error occurs, wait 1 minute before retrying to avoid crash loops
            time.sleep(60)

if __name__ == "__main__":
    print("🤖 Name Changer Bot Starting...")
    update_profile_name()
