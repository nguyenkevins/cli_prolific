from bs4 import BeautifulSoup
from selenium import webdriver
import time


UPDATE_TIME = 60
WAIT_TIME = 5
URL = "https://www.prolific.co/auth/accounts/login/?next=/openid/authorize%3Fclient_id%3D447610%26redirect_uri%3Dhttps%253A%252F%252Fapp.prolific.co%252Foauth%252Fcallback%26response_type%3Did_token%2520token%26scope%3Dopenid%2520profile%26state%3D85100f30d51e46379ba066fa344fa28d%26nonce%3D4901ebbd69454e09b568f5fb478c8226"
userID = ""
passID = ""

# Get options for chrome and make it headless when testing
# with the console message interupting
options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
options.add_argument('log-level=3')
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
options.add_argument('headless')

# initialize the driver
driver = webdriver.Chrome(chrome_options=options)

# Selenium Driver for Chrome
try:
    path = r'chromedriver'
    print("Detected Window OS")
    print("Using Windows Driver")
except:
    try:
        path = r'chromedriver'
        print("Detected MacOS")
        print("Using MacOC Driver")
    except:
        try:
            path = r'linux/chromedriver'
            print("Detected Linux OS")
            print("Using Linux Driver")
        except:
            print("Error Occured... Most likely a bug!")

driver.get(URL)
driver.find_element_by_name('username').send_keys(userID)
print("Username input...")
driver.find_element_by_name('password').send_keys(passID)
print("Password input...")
driver.find_element_by_tag_name('button').click()
print("Sign-In Success!")
time.sleep(WAIT_TIME)

driver.find_element_by_tag_name('button').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
results = soup.find(id="Lead-3-QuoteHeader-Proxy")

time.sleep(WAIT_TIME)
print("Initiating update message...")
while 1>0:
    try:
        phrase = driver.find_element_by_class_name('list').get_attribute("innerHTML")
        if 'list-item' in phrase:
            print("Study Available!")
        else:
            print("Study Not Available...")
        time.sleep(UPDATE_TIME)
        driver.get("https://app.prolific.co/studies")
    except:
        print("Study Not Available...")
        time.sleep(UPDATE_TIME)
        driver.get("https://app.prolific.co/studies")

print(count)

print("debug phase")
os.system("pause")
