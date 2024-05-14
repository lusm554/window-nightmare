from selenium import webdriver
from selenium.webdriver import ChromeOptions, ActionChains
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

def parse_args():
  index_html_filepath = os.path.realpath(sys.argv[1])
  return index_html_filepath

def get_driver_path():
  driver_path = ChromeDriverManager().install()
  return driver_path

def main():
  index_html_filepath = parse_args()
  options = ChromeOptions()
  url = f'file://{index_html_filepath}'
  logger.info(f'{url=!r}')
  logger.info(f'{driver_path=!r}')
  driver_path = get_driver_path()
  driver = webdriver.Chrome(options=options)
  driver.get(url)
  driver.execute_script(f'window.windows_cnt = 1')
  driver.execute_script('main()')
  time.sleep(40)

if __name__ == '__main__':
  main()
