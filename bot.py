
from config_bot import *

from helpbot import mistake, file_html, log_bot

from bs4 import BeautifulSoup, SoupStrainer
from requests import  Session
from time import sleep

number_HTML = 0
form_value = ''
list_dict_news = dict()
session = Session()

# Cтраницa Входа
response = session.get(URL_LOGIN)
print("LOG_BOT:", LOG_BOT)
print(URL_LOGIN  + "    status_code :  " + str(response.status_code))
number_HTML = file_html(response.text + '\n', number_HTML) # Запись в файл HTML
mistake(response,"Запрос страницы Входа")
log_bot ("Запрос страницы Входа")

soup = BeautifulSoup(response.content, 'html.parser', parse_only=SoupStrainer('input'))

for tag in soup:
    # Проверяем вошел или нет
    if tag.get('name') == 'subaction':
        form_value = str(tag.get('value'))
        print("Нужен вход :" + form_value) #del
        # запрос Вход
        sleep(TIMEPAUS)
        response = session.post( URL_LOGIN,  data  =  { 'username': user, 'password': password, "subaction": "dologin"})
        log_bot("Вход status_code :  " + str(response.status_code))
        number_HTML = file_html(response.text + '\n', number_HTML) # Запись в файл HTML
        mistake(response,"запрос Вход")

        soup = BeautifulSoup(response.content, 'html.parser', parse_only=SoupStrainer('div'))
        if soup.find('div', {'class':"error"}):
                error_login = soup.find('div', {'class':"error"}).text
                print("ОШИБКА   :       " + error_login)
                log_bot("ОШИБКА   :       " + error_login)
                exit(1)
        elif soup.find('div', {'class':"navigation"}):
                name_login = soup.find('div', {'class':"navigation"}).text
                print("Успешный вход.                 " + name_login)
                log_bot("Успешный вход.                 " + name_login)
        else:
                print("Куда_то попал, выход из программы " )
                log_bot("Проверяем вошел или нет. Куда_то попал, выход из программы: URL_LOGIN")
                exit(1)

if ADD_NEWS:
        # Запрос добавления новости
        response = session.get(URL_ADDNEWS)
        number_HTML = file_html(response.text + '\n', number_HTML) # Запись в файл HTML
        print("-------------------------------------------")
        print(URL_ADDNEWS  + "    status_code :  " + str(response.status_code))
        log_bot(URL_ADDNEWS  + "    status_code :  " + str(response.status_code))
        mistake(response,"Запрос добавления новости")

        soup = BeautifulSoup(response.content, 'html.parser', parse_only=SoupStrainer('input'))

        user_hash = ''
        for tag in soup:
                if tag.get('name') == 'user_hash':
                        user_hash = str(tag.get('value'))

        #  Добавление новости
        response = session.post(URL_ADDNEWS,  data  =  { "user_hash":user_hash, 'title': title_news, 'allow_date':"yes", 'short_story': short_story,
                "full_story": full_story, "approve":"1", 'mod': 'addnews', 'action': "doaddnews", 'submit': "Добавить"})
        number_HTML = file_html(response.text + '\n', number_HTML) # Запись в файл HTML
        log_bot(URL_ADDNEWS  + "Добавление новости:  " + str(response.status_code))
        mistake(response,"Добавление новости")
else:
        print("НЕ добавляем новость. config_bot ADD_NEWS =", ADD_NEWS)
        log_bot("НЕ добавляем новость. config_bot ADD_NEWS")

# Запрос редактирования новости
response = session.get(URL_EDITNEWS)
number_HTML = file_html(response.text + '\n', number_HTML) # Запись в файл HTML
print("-------------------------------------------")
print(URL_EDITNEWS  + "    status_code :  " + str(response.status_code))
log_bot(URL_EDITNEWS  + "    status_code :  " + str(response.status_code))
mistake(response,"Запрос редактирования новости")

soup = BeautifulSoup(response.content, 'html.parser', parse_only=SoupStrainer('a'))
for href in soup:
        # print(href.text)
        if href.get('title') == 'Редактировать данную новость':
                if href.text == title_news:
                        print("Новость Добавлена : ", URL + href.get('href'))

for href in soup:
        # print(href.text)
        if href.get('title') == 'Редактировать данную новость':
                # print(href.text,href.get('href'))
                list_dict_news.update({str(href.get('href')):str(href.text)})
log_bot("Новости на сайте: " + str(list_dict_news))
# for news in list_dict_news:
#         print(news,"      ",list_dict_news.get(news))

if number_HTML > 0 :
        print("Записано " + str(number_HTML) + " файла HTML")
        log_bot("Записано " + str(number_HTML) + " файла HTML")

print("Конец")
log_bot("Конец")