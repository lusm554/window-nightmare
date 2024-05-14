from selenium import webdriver
from selenium.webdriver import ChromeOptions, ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
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

def parse_cli_args():
  index_html_filepath = os.path.realpath(sys.argv[1])
  open_windows_cnt = int(sys.argv[2])
  popup_url = sys.argv[3]
  logger.info(f'{open_windows_cnt=}')
  logger.info(f'{index_html_filepath=}')
  logger.info(f'{popup_url=}')
  return index_html_filepath, open_windows_cnt, popup_url

def get_driver_path():
  driver_path = ChromeDriverManager().install()
  return driver_path

def get_driver():
  driver_path = get_driver_path()
  options = ChromeOptions()
  service = Service(executable_path=driver_path)
  driver = webdriver.Chrome(
    service=service,
    options=options,
  )
  return driver

def main():
  index_html_filepath, open_windows_cnt, popup_url = parse_cli_args()
  driver = get_driver()
  url = f'file://{index_html_filepath}'
  driver.get(url)
  driver.execute_script(f'window.windows_cnt = {open_windows_cnt}')
  driver.execute_script(f'window.popup_url = {popup_url!r}')
  driver.execute_script('main()')
  time.sleep(40)

if __name__ == '__main__':
  main()
