from selenium import webdriver
import re, requests, time, json
from colorama import Fore, Style
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from clear import clear
class TempMailGEN:
    
    @staticmethod
    def load():
      with open('config.json', 'r') as jfile:
          data = json.load(jfile)
      return(data)


    @staticmethod
    def get_email():
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=100,100")
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)

        try:
            driver.get("https://temp-mail.io/fr")
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "email"))
            )

            email_input = driver.find_element(By.ID, "email")
            email = email_input.get_attribute("value")

            print(f'{Fore.GREEN}[LOG] => TEMP EMAIL: {email}{Style.RESET_ALL}')
            return email
        except Exception as e:
            print(f'{Fore.RED}[ERROR] => {e}{Style.RESET_ALL}')
            return None


    @staticmethod
    def search(frome, msg):
        if 'Steam' in frome:
            url_pattern = r'https://store\.steampowered\.com/account\S*'
            match = re.search(url_pattern, msg)
            if match:
                extracted_url = match.group(0)
                return extracted_url
        return "UNKNOWN"

    @staticmethod
    def get_mail(email):
        url = f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages'
        try:
            req = requests.get(url)
            req.raise_for_status()
            print(f'{Fore.GREEN}[LOG] => FETCHED MAILS for {email}{Style.RESET_ALL}')
            for message in req.json():
                print('=' * 200)
                print(f'ID >> {message["id"]} | FROM >> {message["from"]}')
                print(f'SUBJECT >> {message["subject"]}')
                print(TempMailGEN.search(message['from'], message['body_text']))
                print('=' * 200)
        except requests.RequestException as e:
            print(f'{Fore.RED}[ERROR] => {e}{Style.RESET_ALL}')


#if __name__ == "__main__":
#    config = TempMailGEN.load()
#    email = TempMailGEN.get_email()
#
#    while True:
#        if email:
#            TempMailGEN.get_mail(email)
#        time.sleep(10)
#        clear()
