import pytest
from selenium import webdriver
import time
from bs4 import BeautifulSoup

def test_positive():
    #Открытие нужной страницы в браузере Chrome
    link = "https://zooshoptest.ru/contactszooshop24/"
    browser = webdriver.Chrome()
    browser.get(link)

    #Нахождение кнопки "Обратная связь" (по названию класса элемента) и открытие формы
    button_1 = browser.find_element_by_class_name("shop_menuone_top_right_svyaz_cont")
    button_1.click()
    #Нахождение(по имени элемента) и заполнение поля "Имя"
    input_name = browser.find_elements_by_name("name")
    input_name[1].click()
    input_name[1].clear()
    input_name[1].send_keys("Ivan")

    # Нахождение(по имени элемента) и заполнение поля "Фамилия"
    input_lastname = browser.find_elements_by_name("lastname")
    input_lastname[1].click()
    input_lastname[1].clear()
    input_lastname[1].send_keys("Petrov")

    # Нахождение(по имени элемента) и заполнение поля "Телефон"
    input_phone = browser.find_elements_by_name("phone")
    input_phone[1].click()
    input_phone[1].send_keys("87777777777")

    # Нахождение(по тэгу элемента) и заполнение поля "Комментарий"
    input_comment = browser.find_elements_by_tag_name("textarea")
    input_comment[1].send_keys("Ok")

    # Нахождение кнопки "Отправить"(по названию класса элемента) и отправление формы
    button = browser.find_elements_by_class_name("b24-form-btn-block")
    button[5].click()
    # Ожидание отправки формы
    time.sleep(2)

    # Парсинг страницы
    soup = BeautifulSoup(browser.page_source, "lxml")
    check = soup.find(class_='b24-form-state-text')
    # Проверка была ли отправлена форма успешна
    assert check == "Отправлено"

    # Закрытие браузера
    time.sleep(30)
    browser.quit()
