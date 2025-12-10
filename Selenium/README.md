Twitter/X Name Changer Bot
This is a Python script that uses Selenium to automatically update your Twitter (X) display name with a random emoji every hour. It connects to your existing Chrome profile, so you do not need to log in again.
⚠️ Important Prerequisites
 * Python Installed: You must have Python installed on your computer.
 * Google Chrome: You must have Google Chrome installed.
Installation
 * Install Selenium:
   Open your Command Prompt (Windows) or Terminal (Mac/Linux) and run the following command to install the required library:
   pip install selenium

 * Save the Script:
   Save the corrected Python code provided in the chat as browser_bot.py.
Configuration (Optional)
The script is designed to automatically find your Chrome profile on Windows.
 * If you are on Mac/Linux: You must manually edit the CHROME_PROFILE_PATH variable in the script.
 * If the script crashes on Windows: You may need to manually set your path.
   * Open Chrome and type chrome://version in the address bar.
   * Look for the Profile Path.
   * Copy the path (excluding the final \Default folder) and paste it into the CHROME_PROFILE_PATH variable in the script.
How to Run
CRITICAL STEP: You must CLOSE ALL GOOGLE CHROME WINDOWS before running this script.
If Chrome is open, the script will crash because it cannot access your user profile while it is locked by the main browser.
 * Close Chrome.
 * Open your terminal/command prompt.
 * Navigate to the folder where you saved the script.
 * Run the bot:
   python browser_bot.py

Troubleshooting
"Chrome is likely running..."
If you see an error saying the user data directory is in use:
 * Double-check that all Chrome windows are closed.
 * Check your Task Manager to ensure no background Chrome processes are running.
"selenium.common.exceptions.NoSuchElementException"
 * X (Twitter) frequently changes their website code. If the bot stops finding the "Save" button or the "Name" box, the CSS selectors in the script may need to be updated.
"chromedriver executable needs to be in PATH"
 * Modern Selenium (v4.6+) handles this automatically. If you see this error, run pip install --upgrade selenium to get the latest version.
