# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from datetime import datetime
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Chrome()
fix = 'https://fix-online.sbis.ru/'
sbis_site = 'https://fix-online.sbis.ru/'
sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'
user_login, user_password = 'бот', 'БотА12'
user = 'Бот Алексей'
msg_text = f'Текст сообщения {datetime.now()}'
try:
    driver.maximize_window()
    driver.get(fix)
    sleep(1)

    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    # login.send_keys(user_login, Keys.ENTER)
    assert login.get_attribute('value') == user_login
    sleep(1)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    # password.send_keys(user_password, Keys.ENTER)
    sleep(4)
    contacts = driver.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"]')
    assert contacts.is_displayed(), 'Не отображается раздел Контакты'
    contacts.click()
    sleep(2)
    contacts_btn = driver.find_element(By.CSS_SELECTOR, '[name="headTitle"]')
    assert contacts_btn.is_displayed(), 'Не отображается кнопка Контакты'
    contacts_btn.click()
    sleep(2)
    add_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    assert add_btn.is_displayed(), 'Не отображается кнопка +'
    add_btn.click()
    sleep(1)
    search_contact_field = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-Render__field"] [type="text"]')
    search_contact_field.send_keys(user)
    sleep(1)
    user_in_search = driver.find_element(By.CSS_SELECTOR, f'[data-qa="person-Information__fio"][title="{user}"]')
    assert user_in_search.is_displayed(), f'Не найден сотрудник по запросу {user}'
    user_in_search.click()
    sleep(1)
    text_field = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    assert text_field.is_displayed(), 'Не отображается поле для ввода сообщения'
    text_field.send_keys(msg_text)
    sleep(2)
    send_btn = driver.find_element(By.CSS_SELECTOR, '[title="Отправить"]')
    assert send_btn.is_displayed(), 'Не отображается кнопка отправки сообщения'
    send_btn.click()
    sleep(1)
    my_msg = driver.find_element(By.CSS_SELECTOR, '.msg-entity-text p')
    assert my_msg.is_displayed(), 'Не найдено отправленное сообщение'
    assert my_msg.text == msg_text, f'Текст сообщения не равен эталонному - {msg_text}'
    action_chains = ActionChains(driver)
    action_chains.move_to_element(my_msg)
    action_chains.context_click(my_msg)
    action_chains.perform()
    sleep(0.5)
    delete_btn = driver.find_element(By.CSS_SELECTOR, '[title="Перенести в удаленные"]')
    assert delete_btn.is_displayed(), 'Не найден пункт меню Удалить'
    delete_btn.click()
    sleep(2)
    my_msg = driver.find_element(By.CSS_SELECTOR, '.msg-entity-text p')
    assert my_msg.text != msg_text, f'Сообщение не пропало после удаления'
    sleep(1)
finally:
    driver.quit()
