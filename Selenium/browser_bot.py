import time
import random
import os # Added to help find path automatically
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # REQUIRED for clearing text properly
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- CONFIGURATION ---
# 1. Your Base Name
BASE_NAME = "YourName" 

# 2. Your Chrome Profile Path 
# I have updated this to AUTOMATICALLY find your Windows user path.
# If this doesn't work, manually type your path like: r"C:\Users\Matt\AppData..."
CHROME_PROFILE_PATH = os.path.join(os.environ['LOCALAPPDATA'], r"Google\Chrome\User Data")

# 3. Which Chrome Profile? (Usually "Default" or "Profile 1")
PROFILE_DIRECTORY = "Default" 
# ---------------------

EMOJI_LIST = [
    "🤖", "👾", "🚀", "🌙", "⭐", "🔥", "💿", "💾", "📡", "🔋",
    "🕹️", "🖥️", "⚡", "🕶️", "🦾", "🌌", "🧬", "🧪", "🧿", "💎"
]

def get_driver():
    """Sets up Chrome with your real user profile."""
    options = Options()
    options.add_argument(f"--user-data-dir={CHROME_PROFILE_PATH}")
    options.add_argument(f"--profile-directory={PROFILE_DIRECTORY}")
    options.add_argument("--disable-extensions")
    # This prevents the "Chrome is being controlled by automated software" bar
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    # Keeps the browser open even if script crashes (optional but helpful)
    options.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome(options=options)
    return driver

def update_name_browser():
    print("🚀 Launching Browser...")
    
    # Note: You must close all other Chrome windows before running this!
    try:
        driver = get_driver()
    except Exception as e:
        print("❌ Error opening Chrome. Make sure all Chrome windows are CLOSED.")
        print(f"Details: {e}")
        return

    while True:
        try:
            print("🔗 Navigating to Profile...")
            # Go directly to settings profile to trigger the modal
            driver.get("https://x.com/settings/profile")
            
            # Use WebDriverWait consistently rather than sleep
            wait = WebDriverWait(driver, 15)

            # 1. Find the Name Input Field
            # X uses 'name="displayName"' for the input box
            name_input = wait.until(EC.presence_of_element_located((By.NAME, "displayName")))
            
            # 2. Determine new name
            emoji = random.choice(EMOJI_LIST)
            new_name = f"{BASE_NAME} {emoji}"
            
            # 3. Clear and Type (The React-Safe Way)
            name_input.click()
            time.sleep(0.5)
            
            # Select All (Ctrl+A) and Backspace
            # We use os.name to check if Mac ('posix') or Windows ('nt') for the command key
            cmd_ctrl = Keys.COMMAND if os.name == 'posix' else Keys.CONTROL
            
            name_input.send_keys(cmd_ctrl + "a")
            time.sleep(0.5)
            name_input.send_keys(Keys.BACKSPACE)
            time.sleep(0.5)
            
            # Type new name
            name_input.send_keys(new_name)
            
            print(f"📝 Typed: {new_name}")
            time.sleep(1)

            # 4. Find and Click Save
            # We wait until it is CLICKABLE
            save_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="Profile_Save_Button"]')))
            save_btn.click()
            
            print("✅ Saved!")
            
            # 5. Wait 1 hour (To avoid ban)
            print("⏳ Waiting 1 hour...")
            time.sleep(3600) 
            
            # Refresh page to keep session alive slightly, then loop
            driver.refresh()

        except Exception as e:
            print(f"❌ Error: {e}")
            print("Trying again in 60 seconds...")
            time.sleep(60)

if __name__ == "__main__":
    print("⚠️  WARNING: CLOSE ALL CHROME WINDOWS BEFORE RUNNING THIS")
    update_name_browser()
            # X uses 'name="displayName"' for the input box
            wait = WebDriverWait(driver, 10)
            name_input = wait.until(EC.presence_of_element_located((By.NAME, "displayName")))
            
            # 3. clear current name and type new one
            emoji = random.choice(EMOJI_LIST)
            new_name = f"{BASE_NAME} {emoji}"
            
            # Clear input (Using backspace loop is safer on X than .clear())
            name_input.click()
            # Select all text (Control+A or Command+A)
            # We'll just force value via JS to be less buggy
            driver.execute_script("arguments[0].value = '';", name_input)
            name_input.send_keys(new_name)
            
            print(f"📝 Typed: {new_name}")
            time.sleep(1)

            # 4. Find and Click Save
            # Button usually has data-testid="Profile_Save_Button"
            save_btn = driver.find_element(By.CSS_SELECTOR, '[data-testid="Profile_Save_Button"]')
            save_btn.click()
            
            print("✅ Saved!")
            
            # 5. Wait 1 hour (To avoid ban)
            print("⏳ Waiting 1 hour...")
            time.sleep(3600) 
            
            # Refresh page to keep session alive slightly, then loop
            driver.refresh()

        except Exception as e:
            print(f"❌ Error: {e}")
            print("Trying again in 60 seconds...")
            time.sleep(60)

if __name__ == "__main__":
    print("⚠️  WARNING: CLOSE ALL CHROME WINDOWS BEFORE RUNNING THIS")
    update_name_browser()
