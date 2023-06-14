# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from time import sleep

sbis_site = 'https://fix-online.sbis.ru/'
log = 'belyaevairina'
pas = 'Jrnz,hm2016'
my_contact = 'Беляшкина'
message = 'Домашнее задание 11'
driver = webdriver.Chrome()
driver.maximize_window()
try:
    # открываем сайт https://fix-online.sbis.ru/
    driver.get(sbis_site)

    # авторизуемся
    sleep(3)
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(log, Keys.ENTER)
    sleep(3)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(pas, Keys.ENTER)
    sleep(10)

    # переходим в реестр Контакты
    contacts = driver.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"]')
    assert contacts.is_displayed(), 'Пункт аккордеона Контакты не отображается'
    sleep(3)
    contacts.click()
    sleep(3)
    contacts_tab = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle')
    contacts_tab.click()
    sleep(3)

    # отправляем сообщение самому себе
    dialogs_tab = driver.find_element(By.CSS_SELECTOR, '[title="Диалоги"]')
    assert driver.current_url == 'https://fix-online.sbis.ru/page/dialogs', 'Не перешли на вкладку Диалоги'
    plus_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    sleep(3)
    plus_btn.click()
    sleep(3)
    search = driver.find_element(By.CSS_SELECTOR, '.controls-Search__nativeField_caretEmpty_theme_default')
    search.send_keys(my_contact, Keys.ENTER)
    sleep(3)
    contacts_row = driver.find_element(By.CSS_SELECTOR, '.msg-addressee-item')
    sleep(3)
    contacts_row.click()
    sleep(3)
    text_field = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    text_field.send_keys(message)
    sleep(3)
    send_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    sleep(3)
    send_btn.click()
    sleep(3)

    # проверяем, что сообщение появилось в реестре
    sent_messages = driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item p')
    assert sent_messages[0].text == message, 'Отправленное сообщение отсутствует в реестре'

    # удаляем сообщение и проверяем что оно удалилось
    action_chains = ActionChains(driver)
    action_chains.move_to_element(sent_messages[0])
    action_chains.perform()
    delete_btn = driver.find_element(By.CSS_SELECTOR, ".controls-icon_style-danger")
    delete_btn.click()
    sleep(3)
    sent_messages = driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item p')
    assert sent_messages[0].text != message, 'Отправленное сообщение отсутствует в реестре'

finally:
    driver.quit()