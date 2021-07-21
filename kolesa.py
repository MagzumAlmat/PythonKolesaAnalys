# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import logging
import sys
from wsgiref import headers
import time
import telebot
from bs4 import BeautifulSoup

DOMAIN = 'kolesa.kz'

from bs4 import BeautifulSoup
bot = telebot.TeleBot('1125914898:AAHedexJQzX87tUZh1OlWKBcOog5MeyZAoQ')
import requests
import lxml
import re
import time
#startYear = '1990'
#endYear = '1992'
#city = 'almaty'


hrefs = []
rastamozhen = []
description = []
sredStoimDescrList = []
sort='&sort_by=price-asc'

Number=0
HOST = 'https://' + DOMAIN


#bot.send_message(,text='введите /start для начала работе или /help для просмотра команд Бота')

@bot.message_handler(commands=['/start'])

def start_message(message):
    bot.register_next_step_handler(message, get_city)
    print(message.chat)


@bot.message_handler(commands=['/help'])
def start_message(message):
    bot.send_message(message.chat.id,"Some description....")
    #print(message.chat)

@bot.message_handler(content_types=['text'])
def get_city(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Almaty', 'Symkent', 'Nur-sultan')
    bot.send_message(message.chat.id, 'Обработка. Выберите город', reply_markup=keyboard)
    bot.register_next_step_handler(message, send_city)





@bot.message_handler(content_types=['text'])
def send_city(message):
    print(message.text,'--я внутри send_city')
    global City
    global R
    City = message.text
    R = message.text.lower()
    if message.text.lower() == 'nur-sultan':
       bot.register_next_step_handler(message,send_text)
       keyboard = telebot.types.ReplyKeyboardMarkup(True)
       keyboard.row('Toyota', 'BMW', 'Crysler')
       bot.send_message(message.chat.id, 'Обработка. Выберите марку', reply_markup=keyboard)
    #global Mark=

    elif message.text.lower() == 'almaty':
        bot.register_next_step_handler(message, send_text)
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Toyota', 'BMW', 'Crysler')

        bot.send_message(message.chat.id, 'Обработка. Выберите марку', reply_markup=keyboard)
    elif message.text.lower() == 'shymkent':
        bot.register_next_step_handler(message, send_text)
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Toyota', 'BMW', 'Crysler')
        bot.send_message(message.chat.id, 'Обработка. Выберите марку', reply_markup=keyboard)

    elif message.text.lower() == '/help':

        bot.send_message(message.chat.id, "Some description....")

    else:
        bot.send_message(message.chat.id,'Вы ввели неверные данные')



bot.message_handler(regexp = 'Simple Keyboard') # regexp - ловит регулярные выражения.
def back(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Toyota', 'BMW', 'Crysler')
    bot.send_message(message.chat.id, 'Обработка. Выберите марку', reply_markup=keyboard)



#@bot.message_handler(regexp = 'Back to main menu') #Кнопку "Назад" можно сделать по разному. Это самый простой способ.
#def back_button(message):
#    Keyboard.start_keyboard(message)



@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message.text,'Выбранная марка======================')
    global Mark
    Mark=message.text.lower()
    if message.text.lower() == 'toyota':
       bot.register_next_step_handler(message,choise)
       keyboard = telebot.types.ReplyKeyboardMarkup(True)
       keyboard.row('camry', 'caldina', 'supra')
       bot.send_message(message.chat.id, 'Обработка. Выберите модель например '+ message.text +' /Camry /Caldina /Supra',reply_markup=keyboard)

    elif message.text.lower() == 'bmw':
        bot.send_message(message.chat.id, 'Пока!')
    elif message.text.lower() == 'crysler':
        bot.send_message(message.chat.id, 'Пока!')


@bot.message_handler(content_types=['text'])
def choise(message):

    global ModelOfCar
    ModelOfCar=message.text.lower()
    if message.text.lower() == 'camry':
        bot.register_next_step_handler(message, choseStartYear)
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('1990-1992', '1992-1994', '1994-1996')
        keyboard.row('1996-1998', '1998-2000','2000-2002','2002-2004')
        keyboard.row('2004-2006','2006-2008','2008-2010','2010-2012')
        keyboard.row('2012-2014','2014-2016','2016-2018','2018-2020')
        bot.send_message(message.chat.id,
                         'Обработка. Введите фильтр по годам через дефис,либо выберите фильтр в меню ниже ' + message.text + 'Например: 1990-1993',

                         reply_markup=keyboard)

    elif message.text.lower() == 'caldina':
        bot.register_next_step_handler(message, choseStartYear)
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('1990-1992', '1992-1994', '1994-1996')
        keyboard.row('1996-1998', '1998-2000', '2000-2002', '2002-2004')
        keyboard.row('2004-2006', '2006-2008', '2008-2010', '2010-2012')
        keyboard.row('2012-2014', '2014-2016', '2016-2018', '2018-2020')
        bot.send_message(message.chat.id,
                         'Обработка. Введите фильтр по годам через дефис,либо выберите фильтр в меню ниже ' + message.text + 'Например: 1990-1993',

                         reply_markup=keyboard)

    elif message.text.lower() == 'supra':
        bot.register_next_step_handler(message, choseStartYear)
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('1990-1992', '1992-1994', '1994-1996')
        keyboard.row('1996-1998', '1998-2000', '2000-2002', '2002-2004')
        keyboard.row('2004-2006', '2006-2008', '2008-2010', '2010-2012')
        keyboard.row('2012-2014', '2014-2016', '2016-2018', '2018-2020')
        bot.send_message(message.chat.id,
                         'Обработка. Введите фильтр по годам через дефис,либо выберите фильтр в меню ниже ' + message.text + 'Например: 1990-1993',

                         reply_markup=keyboard)

    elif message.text.lower() == 'bmw':
        bot.send_message(message.chat.id, 'Пока!')
    elif message.text.lower() == 'crysler':
        bot.send_message(message.chat.id, 'Пока!')


    print(ModelOfCar,'THIS IS MODEL OF CAR')


def choseModel(message):

    print('я внутри chooseModel-----' ,ModelOfCar,'msg.text')
    #print('я внутри ' ,message,'msg')
    #return (ModelOfCar)



################################################################################################


def pager(stYFromBot, enYFromBot, page, R,Mark,ModelOfCar):
        print('pager работает')
        print(stYFromBot,'stYFromBot')
        print(enYFromBot,'enYFromBot')
        print(R,'R City')

        #Mark=Mark.lower(Mark)
        #Mark=str(Mark)
        #ModelOfCar=ModelOfCar.lower(ModelOfCar)
        #ModelOfCar=str(ModelOfCar)
        print(type(Mark), Mark)
        print(type(ModelOfCar), ModelOfCar)
        print(type(page), page)
        print(type(sort), sort)
        # url="https://kolesa.kz/cars/bmw/520/"+city+"/?year[from]="+startYear+"&year[to]="+endYear+page""
        #city=City.lower()

        url = "https://kolesa.kz/cars/"+Mark+"/"+ModelOfCar+"/"+R+"/?auto-custom=2&year[from]="+stYFromBot+"&year[to]="+enYFromBot+page+sort
        req = requests.get(url, headers)
        soup = BeautifulSoup(req.content, 'html.parser')

        for link2 in soup.find_all('div', class_='finded'):  # все дивы оесть обьявления
            link2 = link2.get_text()
            l1 = int(re.search(r'\d+', link2).group(0))
            # print(link2,'обьявления')    #ДДОРАБОТАТЬ ПОИСК СТРАНИЦ
            # if len(link2)<112:
            # link2=link2[80:84]
            # link2=link2.replace(" ","")
            # else:
            # link2=link2[80:82]
            # link2=link2.replace(" ","")

            # link2=int(link2)
            print(l1)
            Number = l1
            print('this is number',Number)




def scrap(stYFromBot,  enYFromBot, page, R,Mark,ModelOfCar):
    print('я внутри scrap' ,R)
    #Mark=Mark.lower
    print(Mark)
    #ModelOfCar=ModelOfCar.lower
    print(ModelOfCar)
    #print(headers,'This is header',page,'This is page')
    print(type(R))
    print(type(stYFromBot),stYFromBot)
    print(type(enYFromBot),enYFromBot)
    print(type(sort),sort)
    # https://kolesa.kz/cars/bmw/520/almaty/?year[from]=1992&year[to]=1995
    # url="https://kolesa.kz/cars/bmw/520/"+city+"/?year[from]="+startYear+"&year[to]="+endYear+page""
    url = "https://kolesa.kz/cars/"+Mark+"/"+ModelOfCar+"/"+R+"/?auto-custom=2&year[from]="+stYFromBot+"&year[to]="+enYFromBot+page+sort
    print('Cформированный урл',type(url))
    #https: // kolesa.kz / cars / toyota / camry / almaty /?year[from]=1990 & year[to] = 1995 & sort_by = price - asc
    #https: // kolesa.kz / cars / Toyota / Camry / almaty /?auto - custom=2&year[from]=1990&year[to]=1995 & page = 1 & sort_by = price - asc
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    i = 0
    links_to_handle_recursive = []

    for link in soup.find_all('div', class_='a-info-top'):  # все дивы оесть обьявления
        # for price in links:
        d = link.find('span', class_='price')
        d = d.get_text()
        #print(d)

        original = d  # замена символа
        removed = original.replace("₸", " ")  # замена символа

        removed = removed[21:30]  # срез
        removed = removed.replace(" ", "")  # замена пробела на удаленный пробел
        # removed=removed[:8]                          #удаление символа вконце
        removed = int(removed)
        print(removed,'Это данные')

        # print(removed)
        # prices.append(removed)

        t = link.find('a')  # все ссылки с обьектами
        l = t.get('href')  # cписок ссылок
        # print(HOST+l)
        hrefs.append(HOST + l)
        #print(len(hrefs),'количетво ссылок внутри массива')
        #hrefs.append(removed)  # добавление цен в общий массив ссылок
        #bot.send_message(message.chat.id)

    # print(calc,'программа приняла решение')

    # if number<20:
    #    calc=2

    # elif number/20 == 0:
    #    print(calc,'------количество страниц')

    # else:
    #    calc=number/20 == 0 False:
    #        calc=number+1
########################################################################################################
global sr

@bot.callback_query_handler(func=lambda call: True)
def choseStartYear(message):
    global stYFromBot
    global enYFromBot
    global startYear
    startYear = message.text

    stYFromBot =startYear[0:4]
    enYFromBot = startYear[5:9]
    print('я внутри chose start year-----',startYear,enYFromBot)
    pager(stYFromBot, enYFromBot, '&page=1', R,Mark,ModelOfCar)
    co = 0
    l1 = 0
    calc = 0
    link2 = 0

   #print(Number,'------количество обьявлений')

    if Number < 20:
        calc = 2
    else:
        calc = (Number // 20)+1
    if Number == 20:
        calc = 2
    bot.send_message(message.chat.id, 'Обработка запроса может занять несколько секунд...')
    #print(calc, '------колво страниц')

    for x in range(1, calc):
        print(x,'Количество страниц выдал расчет по страницам ')
        scrap(stYFromBot,enYFromBot,'&page='+str(x) + '',R,Mark,ModelOfCar)

    counter = 0
    mark = []
    price = []
    what_city = []
    cityArray = []
    outputData = []
    customs = []
    custom_answer = []
    print(hrefs,'this is hrefs111111111111111111111111111111')
    hrefCount =0
    hrefCount=len(hrefs)
    #bot.send_message(message.chat.id, 'Нашел следующие объявления:', hrefs)
    global sr
    for n in hrefs:
        #print(n,"внутри hrefs-количество циклов")
        #print(len(hrefs), 'Количество ССЫЛОК в массиве')
        #print(hrefs)
        counter = counter + 1
        url = n
        req = requests.get(url, headers)
        soup = BeautifulSoup(req.content, 'html.parser',timeout=5)

        for link2 in soup.find_all('h1', class_='offer__title'):  # все дивы оесть обьявления
            link2 = link2.get_text()
            # l1=int(re.search(r'\d+', link2).group(0))
        #print(len(link2))
        mark.append(link2)

        for link3 in soup.find_all('div', class_='offer__price'):  # все дивы оесть обьявления
            link3 = link3.get_text()
            # print(link3,'Полный текст цены',len(link3),'--количество символов')
            # l1=int(re.search(r'\d+', link2).group(0))
            original = link3
            # link3 = original.replace("₸", " ")        #замена символа
            link3 = link3[4:14]  # срез
            link3 = link3.replace(" ", "")  # замена пробела на удаленный пробел
            # removed=removed[:8]                          #удаление символа вконце
            # link3=int(link3)
        #print(link3)    #ДДОРАБОТАТЬ ПОИСК СТРАНИЦ
        #print(len(link3),'Количество Прайсов в массиве')
        #print(price,'This is price   why nul?')

        price.append(link3)
        for link4 in soup.find_all('div', class_='offer__parameters'):  # все дивы оесть обьявления
            link4 = link4.dl.dt.get_text()

            # for item in link4:
            # print(item)
            # l1=int(re.search(r'\d+', link2).group(0))
            # print(link4)
        what_city.append(link4)
        for link5 in soup.find_all('div', class_='offer__parameters'):  # все дивы оесть обьявления
            link5 = link5.dl.dd.get_text()
            link5 = link5.replace(" ", "")
            # link5=link5[0:5]
            # for item in link4:
            # print(item)
            # l1=int(re.search(r'\d+', link2).group(0))
        # print(link4,end=link5)
        cityArray.append(link5)

        for link6 in soup.find_all('dt', title='Растаможен в Казахстане'):  # все дивы оесть обьявления

            link6 = link6.get_text()
            # link6=link6.replace(" ","")
            # link5=link5[0:5]
            # for item in link4:
            # print(item)
            # l1=int(re.search(r'\d+', link2).group(0))

        # print(link6)
        customs.append(link6)
        for link7 in soup.find_all('dd', class_='value'):  # все дивы оесть обьявления
            link7 = link7.get_text()
            link7 = link7.replace(" ", "")
            if link7 != 'Да':
                link7 = 'Нет'
            rastamozhen.append(link7)
        custom_answer.append(link7)


        for link8 in soup.find_all('span',class_='kolesa-score-label'):
                link8 = link8.get_text()
                #link8 = link8[3:7]
                # for item in link4:
                # print(item)
                # l1=int(re.search(r'\d+', link2).group(0))
                #print('this is link8',link8)
        sredStoimDescrList.append(link8)

    tenPercent = 0
    twentyPercent = 0
    s = 0

    mlen = len(price)
    print(mlen, 'количество штук прайсов')
    for i in range(mlen):
        # print(m1[i][1])
        s = int(price[i]) + int(s)
        int(s)

    srednStoimost = s / mlen
    print(srednStoimost, 'средняя стоимость')

    srednStoimost=int(srednStoimost)
    sr=str(srednStoimost)

    print(type(price), price)
    print(type(sr),type(srednStoimost))

    m1 = list(zip(mark, price, sredStoimDescrList, what_city, cityArray, customs, custom_answer, hrefs))
    # print(m1)

    for i in range(len(m1)):
        #print(i)
        outputData.append(m1[i][7])
        outputData.append(m1[i][1])
        outputData.append(m1[i][2])
        outputData.append(m1[i][5])
        outputData.append(m1[i][6])

        #outputData.append(m1[i][2])
        #outputData.append(m1[i][3])
        #outputData.append(m1[i][4])
        #outputData.append(m1[i][5])
        #outputData.append(m1[i][6])
        #outputData.append(m1[i][7])

    #print(outputData)

    outputSomeData(message,outputData)

def outputSomeData(message,outputData):
    print('я внутри outputSomeDATA',message.text)
    bot.send_message(message.chat.id,'Cредняя стоимость машин:  '+sr)
    bot.send_message(message.chat.id, 'Сортировка машин по цене, сначала самые дешевые. ' )
    for i in range(len(outputData)):
        #print(i)
        bot.send_message(message.chat.id,outputData[i])
    #message.text=outputData
    #print(message,'0000---', message.text)
    #for i in len(outputData):
    #print(message, '0000---', message.text)
    #bot.send_message(message.chat.id, message.text)

    bot.send_message(message.chat.id, 'Чтобы приступить к новому поиску наберите /start')

    @bot.message_handler(content_types=['text'])
    def delete_message(message):
        if message.text.lower() == '/clear':
            bot.delete_message(message.chat.id, message.message_id)
    #message.text=outputData
    #print(type(outputData))
    #bot.send_message(message.chat.id,'Нашел следующие объявления:', message.text)


    #bot.send_message(message.chat.id,'Нашел следующие объявления:',outputData)
    #keyboard = telebot.types.ReplyKeyboardMarkup(True)
    #keyboard.row('1990-1995', '1995-2000', '2000-2010', '2010-2020')

   #bot.register_next_step_handler(message, choseEndYear(message.text))

#time.sleep(2)

bot.polling(none_stop=True)
#
#
# while True:
#     try:
#       bot.polling(none_stop=True)
#     except:
#       print('bolt')
#       logging.error('error: {}'.format(sys.exc_info()[0]))
#       time.sleep(50)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
