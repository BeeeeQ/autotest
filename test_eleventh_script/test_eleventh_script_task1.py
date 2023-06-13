# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
sbis = 'https://sbis.ru/'
tensor = 'https://tensor.ru/'
tensor_about = 'https://tensor.ru/about'
sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'
try:
    driver.get(sbis)
    sleep(1)
    assert driver.current_url == sbis, 'Неверный адрес сайта'
    assert driver.title == sbis_title, 'Неверный заголовок сайта'
    contacts = driver.find_element(By.CSS_SELECTOR, '[href="/contacts"]')
    assert contacts.is_displayed(), 'Раздел "Контакты" не отображается'
    contacts.click()
    sleep(2)
    tensor_logo = driver.find_element(By.CSS_SELECTOR, '[class="sbisru-Contacts__logo-tensor mb-8"]')
    assert tensor_logo.is_displayed(), 'Баннер Тензор не отображается'
    tensor_logo.click()
    driver.switch_to.window(driver.window_handles[1])
    news_block = driver.find_element(By.CSS_SELECTOR, '[class="tensor_ru-Index__block4-content tensor_ru-Index__card"]')
    assert news_block.is_displayed(), 'Блок новости Сила в людях не отображается'
    more_link = driver.find_element(By.CSS_SELECTOR, 'p [href="/about"]')
    action_chains = ActionChains(driver)
    action_chains.move_to_element(more_link)
    action_chains.perform()
    cookie_agreement_close = driver.find_element(By.CSS_SELECTOR, '[class="tensor_ru-CookieAgreement__close '
                                                                  'icon-Close ws-flex-shrink-0 ws-flexbox '
                                                                  'ws-align-items-center"]')
    cookie_agreement_close.click()
    assert more_link.is_displayed(), 'Линк подробнее не отображается'
    more_link.click()
    sleep(2)
    assert driver.current_url == tensor_about, f'Текущий адрес "{driver.current_url}" ' \
                                               f'не соответствует ссылке "{tensor_about}"'
finally:
    driver.quit()
