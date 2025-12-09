# 🤖 Selenium Twitter Name Rotator (No API Keys)

A Python script that automates your Twitter (X) display name to include changing emojis.

**Unlike standard bots, this does NOT use the Twitter API.** instead, it uses **Selenium** to launch your real Chrome browser, navigate to settings, and change the name exactly like a human would.

### ✨ Features
* **Zero API Keys:** No developer account or application approval needed.
* **Persistent Login:** Uses your existing Chrome profile, so you don't need to save passwords in the script or deal with 2FA/Captchas.
* **Anti-Ban Safety:** Includes timers to prevent aggressive spam flagging.

---

## ⚠️ Important Disclaimers

1.  **Chrome Must Be Closed:** You cannot run this script while you are using Chrome. Selenium needs exclusive access to your user profile folder.
2.  **Ban Risk:** While safer than API bots, automated actions can still flag Twitter's spam systems. Use the default 1-hour timer.
