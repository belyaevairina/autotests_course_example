# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import os

options = Options()
options.add_experimental_option("prefs", {
    "download.default_directory": os.getcwd(),
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

sbis_site = 'https://sbis.ru/'
driver = webdriver.Chrome(options=options)
driver.maximize_window()
try:
    # открыаем https://sbis.ru/
    driver.get(sbis_site)
    sleep(2)

    # в футере находим "Скачать СБИС" и переходим по ней
    sbis_download = driver.find_element(By.LINK_TEXT, "Скачать СБИС")
    sleep(3)
    sbis_download.location_once_scrolled_into_view
    sbis_download.click()
    sleep(3)

    # скачиваем СБИС Плагин для вашей ОС в папку с данным тестом
    tab_plugin = driver.find_element(By.CSS_SELECTOR, '[data-id="plugin"]')
    tab_plugin.click()
    sleep(2)
    sbis_plugin = driver.find_element(By.CSS_SELECTOR, '[href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')
    assert sbis_plugin.is_displayed(), 'Не отображается блок для скачивания полной версии СБИС Плагина'
    link_sbis_plugin = sbis_plugin.get_attribute("href")
    driver.get(link_sbis_plugin)
    sleep(10)

    # проверяем, что плагин скачался
    file_name = Path(link_sbis_plugin).name
    plugin_path = os.path.join(os.getcwd(), file_name)
    assert os.path.exists(plugin_path), 'Плагин не скачан'

    # выводим на печать размер скачанного файла в мегабайтах
    print(f'Размер скачанного файла = {round(os.path.getsize(plugin_path) / 1024 ** 2, 2)} Mb')
finally:
    driver.quit()