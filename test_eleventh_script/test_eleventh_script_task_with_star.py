# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import urllib.request
import os.path


driver = webdriver.Chrome()
sbis = 'https://sbis.ru/'
file_name = 'sbis_plugin.exe'


def test_check_download():
    try:
        driver.get(sbis)
        sleep(1)
        assert driver.current_url == sbis, 'Неверный адрес сайта'
        download_link = driver.find_element(By.CSS_SELECTOR, '[href="/download?tab=ereport&innerTab=ereport25"]')
        action_chains = ActionChains(driver)
        action_chains.move_to_element(download_link)
        action_chains.perform()
        cookie_agreement_close = driver.find_element(By.CSS_SELECTOR, '[class="sbis_ru-CookieAgreement__close"]')
        cookie_agreement_close.click()
        assert download_link.is_displayed(), 'Не найдена ссылка Скачать СБИС'
        download_link.click()
        sleep(1)
        sbis_plugin_btn = driver.find_element(By.CSS_SELECTOR, '[data-id="plugin"]')
        assert sbis_plugin_btn.is_displayed(), 'Не найден раздел СБИС плагин'
        sbis_plugin_btn.click()
        download_plugin = driver.find_element(By.CSS_SELECTOR, '[data-for="plugin"]'
                                                               ' [class="sbis_ru-DownloadNew-loadLink"] a')
        assert download_plugin.is_displayed(), 'Не найдена ссылка для скачивания'
        download_plugin_link = download_plugin.get_attribute('href')
        urllib.request.urlretrieve(download_plugin_link, file_name)
        file_found = False
        for i in range(10):
            sleep(1)
            if not os.path.exists(f'{file_name.replace(".exe", "")}.crdownload') and os.path.exists(file_name):
                if os.path.isfile(file_name):
                    file_size = round((os.path.getsize(file_name) / 1024) / 1024, 2)
                    print(file_size, 'мб')
                    file_found = True
                    break
        assert file_found, f"Файл {file_name} - Не найден"

    finally:
        driver.quit()
