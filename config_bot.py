import os

if os.path.exists('config.env'):
    print('Импорт настроек config.env')
    for line in open('config.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1].replace("\"", "")
else:
    print("НЕТ config.env ! Создайте файл")
    exit(1)

user = os.environ.get('user')
password = os.environ.get('password')
URL = os.environ.get('URL')
URL_LOGIN = URL + os.environ.get('URL_LOGIN')
URL_ADDNEWS = URL + "/admin.php?mod=addnews&action=addnews"
URL_EDITNEWS = URL + "/admin.php?mod=editnews&action=list"

# Неправильные данные
# user = "hkbklor1"
# password = "knknnjknjj"

TIMEPAUS = 0 # Number of seconds between requests. Количество секунд между запросами.
ADD_NEWS = False # Добавлять новость или нет
HTML_BOT = True # Записывать в файл HTML запросы или нет.
LOG_BOT = True # Записывать в файл log действий или нет.

title_news = "Логика"

short_story = "Ло́гика- «наука о правильном мышлении"

full_story = ("Ло́гика (др.-греч. λογική — «наука о правильном мышлении», «способность к рассуждению» от др.-греч. λόγος — «рассуждение»,\
 «мысль», «разум») — раздел философии, нормативная наука о формах, методах и законах интеллектуальной познавательной деятельности,\
  формализуемых на логическом языке. Поскольку это знание получено разумом, логика также определяется как наука о формах и законах мышления.\
   Так как мышление оформляется в языке в виде рассуждения, частными случаями которого являются доказательство и опровержение, логика иногда \
   определяется как наука о способах рассуждения или наука о способах доказательств и опровержений. Логика как наука изучает методы достижения\
    истины в процессе познания опосредованным путём, не из чувственного опыта, а из знаний, полученных ранее можно определить как науку о способах \
    получения выводного знания.\
Одна из главных задач логики — определить, как прийти к выводу из предпосылок (правильное рассуждение) и получить истинное знание \
о предмете размышления, чтобы глубже разобраться в нюансах изучаемого предмета мысли и его соотношениях с другими аспектами рассматриваемого явления.\
В любой науке логика, как мышление о мышлении, служит одним из основных инструментов. Кроме философии,\
 логика также является подразделом математики, а булева алгебра одной из основ информатики.")