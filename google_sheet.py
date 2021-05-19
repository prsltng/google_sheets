from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from multiprocessing import Pool
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
driver = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH") , options=chrome_options)

link = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']   # задаем ссылку на Гугл таблици
my_creds = ServiceAccountCredentials.from_json_keyfile_name('E:/work/creds.json', link) #формируем данные для входа из нашего json файла
client = gspread.authorize(my_creds)    # запускаем клиент для связи с таблицами
sheet = client.open('sheet').sheet1    # открываем нужную на таблицу и лист
print_p = pprint.PrettyPrinter()    # описываем прити принт


def buy_BTC():
    print("OK")
    driver.get('https://p2p.binance.com/ru/trade/buy/BTC')
    time.sleep(1)

    driver.find_element_by_xpath("//div[@class=' css-17ehxay']").click()
    time.sleep(1)

    driver.find_element_by_xpath("//li[@id='RUB']").click()
    

    driver.find_element_by_xpath("//div[@id='C2Cpaymentfilter_searchbox_payment']").click()
    time.sleep(2)

    driver.find_element_by_xpath("//li[@id='Тинькофф']").click()
    time.sleep(4)

    sheet.update_cell(1, 1, driver.find_elements_by_xpath("//div[@class='css-1m1f8hn']")[0].text)
def buy_USDT():
    driver.get('https://p2p.binance.com/ru/trade/buy/USDT')
    time.sleep(1)

    driver.find_element_by_xpath("//div[@class=' css-17ehxay']").click()
    time.sleep(1)

    if driver.find_element_by_xpath("//li[@id='RUB']"):
        driver.find_element_by_xpath("//li[@id='RUB']").click()
    

    driver.find_element_by_xpath("//div[@id='C2Cpaymentfilter_searchbox_payment']").click()
    time.sleep(5)

    driver.find_element_by_xpath("//li[@id='Тинькофф']").click()
    time.sleep(2)

    sheet.update_cell(1, 2, driver.find_elements_by_xpath("//div[@class='css-1m1f8hn']")[0].text)

def buy_BUSD():
    print('OK')
    driver.get('https://p2p.binance.com/ru/trade/buy/BUSD')
    time.sleep(1)

    driver.find_element_by_xpath("//div[@class=' css-17ehxay']").click()
    time.sleep(1)

    if driver.find_element_by_xpath("//li[@id='RUB']"):
        driver.find_element_by_xpath("//li[@id='RUB']").click()


    driver.find_element_by_xpath("//div[@id='C2Cpaymentfilter_searchbox_payment']").click()
    time.sleep(5)

    driver.find_element_by_xpath("//li[@id='Тинькофф']").click()
    time.sleep(2)

    sheet.update_cell(1, 3, driver.find_elements_by_xpath("//div[@class='css-1m1f8hn']")[0].text)
def buy_BNB():
    driver.get('https://p2p.binance.com/ru/trade/buy/BNB')
    time.sleep(1)

    driver.find_element_by_xpath("//div[@class=' css-17ehxay']").click()
    time.sleep(1)

    if driver.find_element_by_xpath("//li[@id='RUB']"):
        driver.find_element_by_xpath("//li[@id='RUB']").click()


    driver.find_element_by_xpath("//div[@id='C2Cpaymentfilter_searchbox_payment']").click()
    time.sleep(5)

    driver.find_element_by_xpath("//li[@id='Тинькофф']").click()
    time.sleep(2)

    sheet.update_cell(1, 4, driver.find_elements_by_xpath("//div[@class='css-1m1f8hn']")[0].text)

def buy_ETH():
    driver.get('https://p2p.binance.com/ru/trade/buy/ETH')
    time.sleep(1)

    driver.find_element_by_xpath("//div[@class=' css-17ehxay']").click()
    time.sleep(1)

    if driver.find_element_by_xpath("//li[@id='RUB']"):
        driver.find_element_by_xpath("//li[@id='RUB']").click()

    driver.find_element_by_xpath("//div[@id='C2Cpaymentfilter_searchbox_payment']").click()
    time.sleep(5)

    driver.find_element_by_xpath("//li[@id='Тинькофф']").click()
    time.sleep(2)

    sheet.update_cell(1, 5, driver.find_elements_by_xpath("//div[@class='css-1m1f8hn']")[0].text)

def buy_DAI():
    driver.get('https://p2p.binance.com/ru/trade/buy/DAI')
    time.sleep(1)

    driver.find_element_by_xpath("//div[@class=' css-17ehxay']").click()
    time.sleep(1)

    if driver.find_element_by_xpath("//li[@id='RUB']"):
        driver.find_element_by_xpath("//li[@id='RUB']").click()


    driver.find_element_by_xpath("//div[@id='C2Cpaymentfilter_searchbox_payment']").click()
    time.sleep(5)

    driver.find_element_by_xpath("//li[@id='Тинькофф']").click()
    time.sleep(2)

    sheet.update_cell(1, 6, driver.find_elements_by_xpath("//div[@class='css-1m1f8hn']")[0].text)

def sell_BTC():
    driver.get('https://p2p.binance.com/ru/trade/sell/BTC')
    time.sleep(1)

    driver.find_element_by_xpath("//div[@class=' css-17ehxay']").click()
    time.sleep(1)

    driver.find_element_by_xpath("//li[@id='RUB']").click()
    

    driver.find_element_by_xpath("//div[@id='C2Cpaymentfilter_searchbox_payment']").click()
    time.sleep(2)

    driver.find_element_by_xpath("//li[@id='Тинькофф']").click()
    time.sleep(4)

    sheet.update_cell(1, 7, driver.find_elements_by_xpath("//div[@class='css-1m1f8hn']")[0].text)
def sell_USDT():
    driver.get('https://p2p.binance.com/ru/trade/sell/USDT')
    time.sleep(1)

    driver.find_element_by_xpath("//div[@class=' css-17ehxay']").click()
    time.sleep(1)

    if driver.find_element_by_xpath("//li[@id='RUB']"):
        driver.find_element_by_xpath("//li[@id='RUB']").click()
    

    driver.find_element_by_xpath("//div[@id='C2Cpaymentfilter_searchbox_payment']").click()
    time.sleep(5)

    driver.find_element_by_xpath("//li[@id='Тинькофф']").click()
    time.sleep(2)

    sheet.update_cell(1, 8, driver.find_elements_by_xpath("//div[@class='css-1m1f8hn']")[0].text)

def sell_BUSD():
    driver.get('https://p2p.binance.com/ru/trade/sell/BUSD')
    time.sleep(1)

    driver.find_element_by_xpath("//div[@class=' css-17ehxay']").click()
    time.sleep(1)

    if driver.find_element_by_xpath("//li[@id='RUB']"):
        driver.find_element_by_xpath("//li[@id='RUB']").click()


    driver.find_element_by_xpath("//div[@id='C2Cpaymentfilter_searchbox_payment']").click()
    time.sleep(5)

    driver.find_element_by_xpath("//li[@id='Тинькофф']").click()
    time.sleep(2)

    sheet.update_cell(1, 9, driver.find_elements_by_xpath("//div[@class='css-1m1f8hn']")[0].text)
def sell_BNB():
    driver.get('https://p2p.binance.com/ru/trade/sell/BNB')
    time.sleep(1)

    driver.find_element_by_xpath("//div[@class=' css-17ehxay']").click()
    time.sleep(1)

    if driver.find_element_by_xpath("//li[@id='RUB']"):
        driver.find_element_by_xpath("//li[@id='RUB']").click()


    driver.find_element_by_xpath("//div[@id='C2Cpaymentfilter_searchbox_payment']").click()
    time.sleep(5)

    driver.find_element_by_xpath("//li[@id='Тинькофф']").click()
    time.sleep(2)

    sheet.update_cell(1, 10, driver.find_elements_by_xpath("//div[@class='css-1m1f8hn']")[0].text)

def sell_ETH():
    driver.get('https://p2p.binance.com/ru/trade/sell/ETH')
    time.sleep(1)

    driver.find_element_by_xpath("//div[@class=' css-17ehxay']").click()
    time.sleep(1)

    if driver.find_element_by_xpath("//li[@id='RUB']"):
        driver.find_element_by_xpath("//li[@id='RUB']").click()

    driver.find_element_by_xpath("//div[@id='C2Cpaymentfilter_searchbox_payment']").click()
    time.sleep(5)

    driver.find_element_by_xpath("//li[@id='Тинькофф']").click()
    time.sleep(2)

    sheet.update_cell(1, 11, driver.find_elements_by_xpath("//div[@class='css-1m1f8hn']")[0].text)

def sell_DAI():
    driver.get('https://p2p.binance.com/ru/trade/sell/DAI')
    time.sleep(1)

    driver.find_element_by_xpath("//div[@class=' css-17ehxay']").click()
    time.sleep(1)

    if driver.find_element_by_xpath("//li[@id='RUB']"):
        driver.find_element_by_xpath("//li[@id='RUB']").click()


    driver.find_element_by_xpath("//div[@id='C2Cpaymentfilter_searchbox_payment']").click()
    time.sleep(7)

    driver.find_element_by_xpath("//li[@id='Тинькофф']").click()
    time.sleep(2)

    sheet.update_cell(1, 12, driver.find_elements_by_xpath("//div[@class='css-1m1f8hn']")[0].text)

sell_DAI()
functions = {
    'buy_BNB': buy_BNB,
    'buy_BTC': buy_BTC,
    'buy_BUSD': buy_BUSD,
    'buy_DAI': buy_DAI,
    'buy_ETH': buy_ETH,
    'buy_USDT': buy_USDT,
    'sell_BNB': sell_BNB,
    'sell_BTC': sell_BTC,
    'sell_BUSD': sell_BUSD,
    'sell_DAI': sell_DAI,
    'sell_ETH': sell_ETH,
    'sell_USDT': sell_USDT
}

def main(out):
    while True:
        functions[out]()

if __name__ == "__main__":
    function_names = ['buy_BNB', 'buy_BTC', 'buy_BUSD', 'buy_DAI', 'buy_ETH', 'buy_USDT', 'sell_BNB', 'sell_BTC', 'sell_BUSD', 'sell_DAI', 'sell_ETH', 'sell_USDT']
    with Pool(12) as pars:
        pars.map(main, function_names)    
