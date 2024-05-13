from selenium import webdriver
from selenium.webdriver import ChromeOptions, ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
import time
import logging
import sys
import os

logging.basicConfig(
  level=logging.INFO,
  format='[%(asctime)s] %(levelname)s [%(name)s] %(message)s',
  datefmt='%Y-%m-%d %H:%M:%S %Z',
)
logger = logging.getLogger(__name__)

options = ChromeOptions()
index_html_filepath = os.path.realpath(sys.argv[1])
url = f'file://{index_html_filepath}'
logger.info(f'{url=!r}')
driver_path = ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
logger.info(f'{driver_path=!r}')
driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(40)
