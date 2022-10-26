import datetime


def opertion_logger(id, username, menu, text):
    time = datetime.datetime.now().strftime('%d.%m.%y || %H:%M')
    with open('log.txt', 'a', encoding='utf_8') as file:
        file.write(f'{time} || {id} || {username} || {menu} || {text}\n')
