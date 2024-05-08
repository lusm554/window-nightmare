from selenium import webdriver
from selenium.webdriver import ChromeOptions, ActionChains
import time
import logging
import sys

logging.basicConfig(
  level=logging.ERROR,
  format='[%(asctime)s] %(levelname)s [%(name)s] %(message)s',
  datefmt='%Y-%m-%d %H:%M:%S %Z',
)
logger = logging.getLogger(__name__)

options = ChromeOptions()
url = f'file://{sys.argv[1]}'
print(url)
driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(40)
