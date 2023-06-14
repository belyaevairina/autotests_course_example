# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

sbis_site = 'https://sbis.ru/'
tensor_site = 'https://tensor.ru/'
tensor_site_about = 'https://tensor.ru/about'
driver = webdriver.Chrome()
try:
    #открываем сайт https://sbis.ru/
    driver.get(sbis_site)

    # переходим в раздел Контакты
    driver.find_element(By.CSS_SELECTOR, 'a[href="/contacts"]').click()
    sleep(2)

    # находим баннер Тензор и кликаем по нему
    banner = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor')
    banner.is_displayed(), 'Баннер не отображается'
    banner.click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == tensor_site, 'Не перешли на страницу https://tensor.ru/'

    # проверяем, что на открывшейся странице есть блок новости "Сила в людях"
    block = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content')
    block.is_displayed(), 'Блок не отображается'
    sleep(2)

    # переходим в этом блоке в "Подробнее" и проверяем, что открывается https://tensor.ru/about
    link = driver.find_element(By.CSS_SELECTOR, 'a[href="/about"]')
    driver.execute_script("return arguments[0].scrollIntoView(true);", link)
    link.is_displayed(), 'Отсутствует ссылка Подробнее'
    link.click()
    sleep(2)
    assert driver.current_url == tensor_site_about, 'Не перешли на страницу https://tensor.ru/about'
finally:
    driver.quit()