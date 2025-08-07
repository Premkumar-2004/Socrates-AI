from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup WebDriver with Chrome Profile (Keeps you logged in)
options = webdriver.ChromeOptions()
options.add_argument("C:\\Users\\91765\\AppData\\Local\\Google\\Chrome\\User Data\\Default")  # Chrome User Data path

options.add_experimental_option("detach", True)  # Keeps browser open

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 15)  # Increased wait time for stability

# Open Stytch website
driver.get("https://stytch.com/")

# Click "Login" button
try:
    login_selector = "body > div.sc-4c59d76f-0.imWyOR > header > nav > div:nth-child(2) > ul > div:nth-child(1) > li > a"
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, login_selector))).click()
    print("Clicked Login button.")
except Exception as e:
    print(f"Error clicking Login button: {e}")

# Click "Continue with Google"
try:
    google_selector = "#oauth-google > div > span"
    google_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, google_selector)))
    
    # Normal Click
    try:
        google_button.click()
    except:
        # Fallback to JavaScript Click
        driver.execute_script("arguments[0].click();", google_button)
    
    print("Clicked 'Continue with Google'.")
except Exception as e:
    print(f"Error clicking 'Continue with Google': {e}")

# **Google Login Process**
try:
    # Enter Email
    email_selector = "#identifierId"
    email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, email_selector)))
    email_input.send_keys("premboddu70@gmail.com")

    # Click "Next" after entering email
    email_next_selector = "#identifierNext > div > button > span"
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, email_next_selector))).click()
    print("Entered Email & clicked Next.")

    # Enter Password
    password_selector = "#password input"
    password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, password_selector)))
    password_input.send_keys("premkumar@456")

    # Click "Next" after entering password
    password_next_selector = "#passwordNext > div > button > span"
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, password_next_selector))).click()
    print("Entered Password & clicked Next.")

except Exception as e:
    print(f"Google Login failed: {e}")

# Click "Create Organization"
try:
    create_org_selector = "#stytch-b2b-ui-984029 > stytch-b2b-ui > div > section > span > div > div > div.sc-bczRLJ.gTRWmK > div:nth-child(4) > button"
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, create_org_selector))).click()
    print("Clicked 'Create Organization'.")
except Exception as e:
    print(f"Error clicking 'Create Organization': {e}")

# **Fill Organization Details**
try:
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#first-name-inputuq2g5a"))).send_keys("Premkumar")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#last-name-inputtck5cy"))).send_keys("Boddu")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#company-name-inputp73obi"))).send_keys("Socrates")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#attribution-inputwnr5xq"))).send_keys("News Channels")
    print("Filled Organization Details.")

    # Click "Next"
    next_button_selector = "#__next > div > div > div > div.css-1szyi91 > div > div.css-wonra7 > div > div.css-wphhoa > span > div > div > button"
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, next_button_selector))).click()
    print("Clicked Next.")

    # Click "Get Started"
    get_started_button_selector = "#__next > div > div > div > div.css-1szyi91 > div > div.css-wonra7 > div > div.css-wphhoa > span > div > div > button"
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, get_started_button_selector))).click()
    print("Clicked 'Get Started'.")

except Exception as e:
    print(f"Error filling details: {e}")

print("✅ Automation Completed!")
driver.quit()  # Closes the browser
