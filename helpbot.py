from config_bot import HTML_BOT, LOG_BOT, ADD_NEWS
from time import asctime

LOG_File = True

def mistake(response, text):

    if response.status_code != 200:
            exit(1)
    elif not response.text:
            print("ОШИБКА Куда_то попал, выход из программы : ", text)
            exit(1)

def file_html(HTML, number, bot_html=HTML_BOT):

    if bot_html:
        number += 1
        file = open ('log/html/bot' + str(number) + '.html', 'w')
        file.write(HTML + '\n')
        file.close()
        return number
    else:
        return number

def log_bot (log, bot_log=LOG_BOT):

    global LOG_File
    global ADD_NEWS
    if bot_log:
        file = open ('log/log.txt', 'a')
        if LOG_File:
            file.write("------------------------------------------------------------------------------------------------" + '\n')
            file.write(str(asctime()) + "     ADD_NEWS:" + str(ADD_NEWS) + '\n'+ '\n')
            LOG_File = False
        file.write(log + '\n')
        file.close()