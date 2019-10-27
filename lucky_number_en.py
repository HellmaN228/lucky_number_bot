import telebot
global year
global mounth
global day
global answer
bot = telebot.TeleBot(token = 'token')
@bot.message_handler(commands=['instagram'])
def handler_start(message):
        bot.send_message(message.chat.id,'www.instagram.com/pp_andr')
@bot.message_handler(commands=['start'])
def handler_start(message):
        print(message.chat.id)
        print(message.from_user.first_name)
        bot.send_message(message.chat.id,'Hi, I will give you a lucky number \nEnter the year of birth')
        bot.register_next_step_handler(message, handler_entering_year)

def handler_entering_year(message):
    if not message.text.isdigit():
        bot.send_message(message.chat.id, "I remind you to enter a number")
        return bot.register_next_step_handler(message, handler_entering_year)   #проверка 1
    global year
    year = message.text #забираем число
    print(year)
    if int(year)>3000 or int(year)<1000:
        bot.send_message(message.chat.id, "Year in the range from 1000 to 3000. Try again") #проверка 2
        return bot.register_next_step_handler(message, handler_entering_year)
    bot.send_message(message.chat.id, "Fine! Now indicate the month when you were born :)")
    bot.register_next_step_handler(message, handler_entering_month)

    
def handler_entering_month(message):
    if not message.text.isdigit():
        bot.send_message(message.chat.id, "I remind you to enter a number")
        return bot.register_next_step_handler(message, handler_entering_month)   #проверка 2
    global mounth
    mounth=message.text #забираем число
    print(mounth)
    if int(mounth)>12 or int(mounth)<1:
        bot.send_message(message.chat.id, "Month numbers range from 1 to 12. Try again") #проверка 2
        return bot.register_next_step_handler(message, handler_entering_month)

    bot.send_message(message.chat.id, "Fine! Now indicate the day you were born :)")
    bot.register_next_step_handler(message, headler_day)

def headler_day(message):
    if not message.text.isdigit():
        bot.send_message(message.chat.id, "I remind you to enter a number")
        return bot.register_next_step_handler(message, headler_day)   #проверка 3
    day=message.text #забираем число
    print(day)
    if int(day)>31 or int(day)<1:
        bot.send_message(message.chat.id, "Day numbers range from 1 to 31. Try again") #проверка 3
        return bot.register_next_step_handler(message, headler_day)

    bot.send_message(message.chat.id, "Fine! Now we will honor everything and give you the result)")
    summ = sum(map(int, str(year)))
    summ += sum(map(int, str(mounth)))
    summ += sum(map(int, str(day)))
    summ = sum(map(int, str(summ)))
    if(summ > 9):
            summ = sum(map(int, str(summ)))
    if(summ == 0):
        answer = ""
    elif(summ == 1):
            answer = "Number 1 is referred to as the leader. Such people are confident in themselves and in their actions. They are very faithful to their principles and people. You can rely on them in almost any situation"
    elif(summ == 2):
    		answer = "Number 2 is easy to charm, it's frivolous and romantic person. Great chance to hurt such a person, they are characterized by increased sensitivity and sensitivity to even the little things. These are very creative people, often artists, sculptors, designers or writers are obtained from them."
    elif(summ == 3):
            answer = "For number 3, insight and a sharp mind are characteristic. Such a person is not so easy to fool, but she is too demanding on herself, which makes it difficult to enjoy the delights of life"
    elif(summ == 4):
            answer = "Number 4 is a pretender. He is what people want him to be. At work, he is an impeccable worker, at home - an exemplary family man, he maintains cold impregnability and loves personal space. Only a few are allowed to recognize him for who he is."
    elif(summ == 5):
            answer = "Fives lead an active lifestyle. Such people are the soul of the company. It is difficult to surprise them with something. They are very rarely offended, always positive and have an excellent sense of humor, they are generous and generous, especially for relatives and friends. However, if you seriously offend such a person, you will lose his respect for a long time"
    elif(summ == 6):
            answer = "If you like a person whose lucky number is 6, be extremely careful with him, such an individual is very jealous and quick-tempered, but he can easily get out of a hopeless situation. Such people are also very spontaneous."
    elif(summ == 7):
            answer = "Sevens prefer a solitary lifestyle. They are very suspicious by nature, it is very difficult to gain their trust, and if you stumble somewhere, they will no longer give a second chance. These are very pedantic people, punctual and follow the rules. They can be entrusted with any work and be completely sure that it will be completed on time and with high quality."
    elif(summ == 8):
            answer = "Number 8 seeks pleasure and entertainment in life. They are rarely serious and often difficult to understand if they joke or really think so. Such people are stubborn and categorical when they consider that they are right in a given situation"
    elif(summ == 9):
            answer = "Nines - romance to the bone. Very kind and sentimental. Have a highly developed imagination"
    bot.send_message(message.chat.id, 'Your number: %d\n[Determination of character by number]\n%s.'%(summ,answer,))

if __name__ == '__main__':
     bot.polling(none_stop=True)
     while True:
        try:
                main()
        except:
                print("Something broke..")