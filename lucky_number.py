import telebot
global year
global mounth
global day
global answer
bot = telebot.TeleBot(token = '507782457:AAECKqyHyNIGiZTd_8Oufy5OqQgQHHVGo7Y')
@bot.message_handler(commands=['instagram'])
def handler_start(message):
        bot.send_message(message.chat.id,'www.instagram.com/pp_andr')
@bot.message_handler(commands=['start'])
def handler_start(message):
        print(message.chat.id)
        print(message.from_user.first_name)
        bot.send_message(message.chat.id,'Привет, я буду предоставлять Вам счастливое число\nВведите год рождения')
        bot.register_next_step_handler(message, handler_entering_year)

def handler_entering_year(message):
    if not message.text.isdigit():
        bot.send_message(message.chat.id, "Напоминаю, что нужно ввести число")
        return bot.register_next_step_handler(message, handler_entering_year)   #проверка 1
    global year
    year = message.text #забираем число
    print(year)
    if int(year)>3000 or int(year)<1000:
        bot.send_message(message.chat.id, "Год в диапазоне от 1000 до 3000. Попробуй еще раз") #проверка 2
        return bot.register_next_step_handler(message, handler_entering_year)
    bot.send_message(message.chat.id, "Отлично! Теперь укажи месяц, когда Вы народились:)")
    bot.register_next_step_handler(message, handler_entering_month)

    
def handler_entering_month(message):
    if not message.text.isdigit():
        bot.send_message(message.chat.id, "Напоминаю, что нужно ввести число")
        return bot.register_next_step_handler(message, handler_entering_month)   #проверка 1
    global mounth
    mounth=message.text #забираем число
    print(mounth)
    if int(mounth)>12 or int(mounth)<1:
        bot.send_message(message.chat.id, "Номера месяца в диапазоне от 1 до 12. Попробуй еще раз") #проверка 2
        return bot.register_next_step_handler(message, handler_entering_month)

    bot.send_message(message.chat.id, "Отлично! Теперь укажи день, когда Вы народились:)")
    bot.register_next_step_handler(message, headler_day)

def headler_day(message):
    if not message.text.isdigit():
        bot.send_message(message.chat.id, "Напоминаю, что нужно ввести число")
        return bot.register_next_step_handler(message, headler_day)   #проверка 1
    day=message.text #забираем число
    print(day)
    if int(day)>31 or int(day)<1:
        bot.send_message(message.chat.id, "Номера дня в диапазоне от 1 до 31. Попробуй еще раз") #проверка 2
        return bot.register_next_step_handler(message, headler_day)

    bot.send_message(message.chat.id, "Отлично! Теперь мы прощитаем все и выдадим Вам результат)")
    summ = sum(map(int, str(year)))
    summ += sum(map(int, str(mounth)))
    summ += sum(map(int, str(day)))
    summ = sum(map(int, str(summ)))
    if(summ > 9):
            summ = sum(map(int, str(summ)))
    if(summ == 0):
        answer = ""
    elif(summ == 1):
            answer = "О номере 1 отзываются как о лидере. Такие люди уверены в себе и в своих действиях. Они очень верны своим принципам и людям. На них можно положиться практически в любой ситуации"
    elif(summ == 2):
    		answer = "Номер 2 легко очаровать, это легкомысленные и романтичные особы. Велик шанс ранить такого человека, им свойственна повышенная впечатлительность и чувствительность даже к мелочам. Это очень творческие люди, из них нередко получаются художники, скульпторы, дизайнеры или писатели."
    elif(summ == 3):
            answer = "Для числа 3 свойственна проницательность и острый ум. Такую личность не так-то просто обдурить, однако она чересчур требовательна к себе, что мешает наслаждаться прелестями жизни"
    elif(summ == 4):
            answer = "Цифра 4 — притворщик. Он такой, каким хотят его видеть люди. На работе он безукоризненный работник, дома — примерный семьянин, он сохраняет холодную неприступность и любит личное пространство. Лишь некоторым позволено узнать его таким, какой он есть."
    elif(summ == 5):
            answer = "Пятерки ведут активный образ жизни. Такие люди — душа компании. Их сложно чем-то удивить. Они очень редко обижаются, всегда на позитиве и обладают превосходным чувством юмора, они щедры и великодушны, в особенности для близких и друзей. Однако если вы серьезно обидите такого человека — уважение его вы надолго потеряете"
    elif(summ == 6):
            answer = "Если вам нравится человек, счастливая цифра которого 6, будьте с ним предельно осторожны, такой индивид очень ревнив и вспыльчив, но ему не составит труда выпутаться из безысходной ситуации. Такие люди также очень спонтанны"
    elif(summ == 7):
            answer = "Семерки предпочитают одиночный образ жизни. Они очень подозрительны по своей натуре, завоевать их доверие очень сложно, а если где-то оступиться, второго шанса они больше не дадут. Это очень педантичные люди, пунктуальны и соблюдают правила. Им можно доверить любую работу и быть полностью уверенным, что она будет выполнена в срок и качественно"
    elif(summ == 8):
            answer = "Номер 8 ищет в жизни удовольствие и развлечение. Они редко бывают серьезными и часто сложно понять, шутят они или правда так думают. Такие люди упрямы и категоричны, когда считают, что в той или иной ситуации правы"
    elif(summ == 9):
            answer = "Девятки — романтики до мозга костей. Очень добрые и сентиментальные. Обладают высокоразвитым воображением"
    bot.send_message(message.chat.id, 'Ваше число: %d\n[Определение характера по цифре]\n%s.'%(summ,answer,))

if __name__ == '__main__':
     bot.polling(none_stop=True)
     while True:
        try:
                main()
        except:
                print("Что-то сломалось..")