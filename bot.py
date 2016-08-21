import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    command_key = telebot.types.ReplyKeyboardMarkup(True, True)
    command_key.row('/help')
    bot.send_message(message.from_user.id, 'Привет, ' + message.from_user.first_name + '!' + ' Жми /help чтобы узнать о возможостях бота.', reply_markup=command_key)

@bot.message_handler(content_types=['text'])
def mess_text(message):
    if message.text == "/help":
        command_key = telebot.types.ReplyKeyboardMarkup(True, True)
        command_key.row("/structure")
        command_key.row("/courses")
        command_key.row("/events")
        command_key.row("/help")
        bot.reply_to(message, config.help, reply_markup=command_key)
    elif message.text == "/structure":
        bot.reply_to(message, config.structure)
    elif message.text == "/courses":
        bot.reply_to(message, config.courses)
    elif message.text == "/events":
        bot.reply_to(message, config.events)
    else:
        bot.send_message(message.from_user.id, 'Вы ввели неверную команду. Для справки введите /help.')

bot.polling(none_stop=True)


"""
@bot.message_handler(commands=['courses'])
def courses(message):
    bot.reply_to(message, '''Студенческий ИТ-клуб организует бесплатные курсы для студентов, подробности и начало курса можно узнать в группах в ВК.
https://new.vk.com/java_in_it - курсы по Java
https://new.vk.com/web_kypc - Веб-разработка
https://new.vk.com/jump_in_it - Акселератор студенческих проектов. Акселератор - это образовательная программа, способствующая ускоренному развитию студенческих проектов.
https://new.vk.com/init_cropdev - Кроссплатформенная разработка. Второй в мире курс по разработке кросс платформенных приложений на основе веб технологий. Если твой слоган "Написал один раз, запустил везде", то тебе к нам.
''')

@bot.message_handler(commands=['structure'])
def structure(message):
    bot.reply_to(message, '''https://new.vk.com/itclub_psuti - Студенческий ИТ-клуб ПГУТИ
https://new.vk.com/profkom_psuti - Профком студентов ПГУТИ
https://new.vk.com/club15473107 - Студеческий Молодежный Центр
https://new.vk.com/sto_psuti - Штаб студенческих отрядов ПГУТИ "Сеть Связи"
''')

@bot.message_handler(commands='events')
def events(message):
    bot.reply_to(message, '''https://new.vk.com/fb_psuti - ФОРТ БОЯРД. Не упусти возможность узнать все тайны ПГУТИ!
https://new.vk.com/gigabyte_2016  - Турнир по скоростной сборке компьютеров "Собери компьютер"
https://new.vk.com/studday_psuti - StudDay. День студента ПГУТИ позволит учащимся школ стать настоящим студентом на целый день!
https://new.vk.com/brain_psuti - Легендарный "Что?Где?Когда?"
https://new.vk.com/olymp_psuti - Студенческая Олимпиада в сфере Инфокоммуникационных технологий
''')
"""
