import telebot
import config
import os
from flask import Flask, request

bot = telebot.TeleBot(config.token)

server = Flask(__name__)

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
        bot.reply_to(message, '/structure - список студенчских организаций\n'
                              '/courses - бесплатные курсы для студентов\n'
                              '/events - мероприятия ИТ-клуба ПГУТИ', reply_markup=command_key)
    elif message.text == "/structure":
        bot.reply_to(message, 'https://new.vk.com/itclub_psuti - Студенческий ИТ-клуб ПГУТИ\n'
                              'https://new.vk.com/profkom_psuti - Профком студентов ПГУТИ\n'
                              'https://new.vk.com/club15473107 - Студеческий Молодежный Центр\n'
                              'https://new.vk.com/sto_psuti - Штаб студенческих отрядов ПГУТИ "Сеть Связи"')
    elif message.text == "/courses":
        bot.reply_to(message, 'Студенческий ИТ-клуб организует бесплатные курсы для студентов, подробности и начало курса можно узнать в группах в ВК.\n'
                              'https://new.vk.com/java_in_it - курсы по Java\n'
                              'https://new.vk.com/web_kypc - Веб-разработка\n'
                              'https://new.vk.com/jump_in_it - Акселератор студенческих проектов. Акселератор - это образовательная программа, способствующая ускоренному развитию студенческих проектов.\n'
                              'https://new.vk.com/init_cropdev - Кроссплатформенная разработка. Второй в мире курс по разработке кросс платформенных приложений на основе веб технологий. Если твой слоган "Написал один раз, запустил везде", то тебе к нам.'
)
    elif message.text == "/events":
        bot.reply_to(message, 'https://new.vk.com/fb_psuti - ФОРТ БОЯРД. Не упусти возможность узнать все тайны ПГУТИ!\n'
                              'https://new.vk.com/gigabyte_2016  - Турнир по скоростной сборке компьютеров "Собери компьютер"\n'
                              'https://new.vk.com/studday_psuti - StudDay. День студента ПГУТИ позволит учащимся школ стать настоящим студентом на целый день!\n'
                              'https://new.vk.com/brain_psuti - Легендарный "Что?Где?Когда?"\n'
                              'https://new.vk.com/olymp_psuti - Студенческая Олимпиада в сфере Инфокоммуникационных технологий')
    elif message.text == "/itclub":
        bot.send_photo(message.from_user.id, photo="https://pp.vk.me/c622728/v622728138/e6fe/oyZ3Ap2FO9E.jpg")

    else:
        bot.send_message(message.from_user.id, 'Вы ввели неверную команду. Для справки введите /help.')

@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://itclub-telegram-bot.herokuapp.com/bot")
    return "!", 200

server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
server = Flask(__name__)




