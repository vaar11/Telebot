import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# import datetime

# Введите свой токен бота здесь
bot = telebot.TeleBot("5697165027:AAH7TJ7Xy2uGdh3b_hUG0iSYEGlzQcchpT8")


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    # Создаем клавиатуру
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    # Добавляем кнопки на клавиатуру
    keyboard.add(KeyboardButton('Расписание'), KeyboardButton('Домашнее задание'))
    keyboard.add(KeyboardButton('Справочный материал'), KeyboardButton('Столовая'))

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}! Выберите действие:",
                     reply_markup=keyboard)


# Обработчик кнопок
@bot.message_handler(content_types=['text'])
def handle_text(message):
    # Обрабатываем нажатие на кнопку
    if message.text == 'Расписание':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton('Понедельник'), KeyboardButton('Вторник'))
        markup.add(KeyboardButton('Среда'), KeyboardButton('Четверг'))
        markup.add(KeyboardButton('Пятница'), KeyboardButton("Вернуться в главное меню"))
        bot.send_message(message.chat.id, "Выберите день", reply_markup=markup)
    if message.text == "Вернуться в главное меню":
        handle_start(message)
    if message.text == "Понедельник":
        table_monday = open("img_1.png", 'rb')
        bot.send_photo(message.chat.id, table_monday)
    if message.text == 'Вторник':
        table_tuesday = open('img_2.png', 'rb')
        bot.send_photo(message.chat.id, table_tuesday)
    if message.text == 'Среда':
        table_wenesday = open('img_3.png', 'rb')
        bot.send_photo(message.chat.id, table_wenesday)
    if message.text == 'Четверг':
        table_thursday = open("img_4.png", 'rb')
        bot.send_photo(message.chat.id, table_thursday)
    if message.text == 'Пятница':
        table_friday = open('img_5.png', 'rb')
        bot.send_photo(message.chat.id, table_friday)

    if message.text == 'Домашнее задание':
        bot.send_message(message.chat.id,
                         "Геометрия:пп 38-39, № 326(б), 330, 339. \nФизика:Параграф 84 прочитать\n Английский язык:  стр 124-125 упр3-читать,упр2-писать,стр 164 упр1-4-писать,учить лексику модуля 7а-7в\n История:    Прочитать стр. 148-155, ответить на вопросы на стр. 154. Тест цдз рекомендован к выполнению.")

    if message.text == 'Справочный материал':
        keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard1.add(KeyboardButton('Математика'), KeyboardButton('Физика'))
        keyboard1.add(KeyboardButton('История'), KeyboardButton('Обществознание'))
        keyboard1.add(KeyboardButton('Вернуться в главное меню'))
        bot.send_message(message.chat.id, "Выберите:  ", reply_markup=keyboard1)
    if message.text == 'Математика':
        keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard2.add(KeyboardButton('Алгебра'), KeyboardButton('Геометрия'))
        keyboard2.add(KeyboardButton('Вернуться в главное меню'))
        bot.send_message(message.chat.id, 'Выберите', reply_markup=keyboard2)
    if message.text == 'Алгебра':
        material_math = open('algebra_spravka.pdf', 'rb')
        material_math1 = open('img.png', 'rb')
        bot.send_document(message.chat.id, material_math)
        bot.send_photo(message.chat.id, material_math1)
        material_math.close()
        material_math1.close()
    if message.text == 'Геометрия':
        geometry = open('geometry.pdf', 'rb')
        bot.send_document(message.chat.id, geometry)
        geometry.close()
    if message.text == 'История':
        keyboard5 = ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard5.add(KeyboardButton('Даты(19 век)'), KeyboardButton('Даты(20 век)'))
        keyboard5.add(KeyboardButton('Вернуться в главное меню'))
        bot.send_message(message.chat.id, 'Выберите:', reply_markup=keyboard5)
    if message.text == 'Даты(19 век)':
        his_19 = open('photo_2023-11-23_15-13-57 (2).jpg', 'rb')
        bot.send_photo(message.chat.id, his_19)
        his_19.close()
    if message.text == 'Даты(20 век)':
        his_20 = open('photo_2024-01-25_18-51-40.jpg', 'rb')
        bot.send_photo(message.chat.id, his_20)
        his_20.close()
    if message.text == 'Физика':
        keyboard3 = ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard3.add(KeyboardButton('Кинематика'), KeyboardButton('Механика'))
        keyboard3.add(KeyboardButton('Термодинамика'), KeyboardButton('Электростатика'))
        keyboard3.add(KeyboardButton('Механические колебания и волны'), KeyboardButton('Динамика'))
        keyboard3.add(KeyboardButton('Вернуться в главное меню'))
        # phys = open("формулы-с-пояснениями.pdf", 'rb')
        bot.send_message(message.chat.id, 'Выберите раздел', reply_markup=keyboard3)
    if message.text == 'Кинематика':
        # kinematics_2 = open('Кинематика за 8 мин.mp4','rb')
        kinematics = open('Kinematika.pdf', 'rb')
        bot.send_document(message.chat.id, kinematics)
        # bot.send_video(message.chat.id,timeout=3)
    if message.text == 'Механика':
        mech = open('mech.pdf.pdf', 'rb')
        bot.send_document(message.chat.id, mech)
        mech.close()
    if message.text == 'Термодинамика':
        thermodynamics = open('Osnovy_termodinamiki.pdf', 'rb')
        bot.send_document(message.chat.id, thermodynamics)
        thermodynamics.close()
    if message.text == 'Электростатика':
        electrostatics = open('Elektrostatika.pdf', 'rb')
        bot.send_document(message.chat.id, electrostatics)
        electrostatics.close()
    if message.text == 'Механические колебания и волны':
        mech_vib = open('Mekhanicheskie_kolebania_i_volny.pdf', 'rb')
        bot.send_document(message.chat.id, mech_vib)
        mech_vib.close()
    if message.text == 'Динамика':
        dynamics = open('Dinamika.pdf', 'rb')
        bot.send_document(message.chat.id, dynamics)
        dynamics.close()
    if message.text == 'Основные даты по истории(19 век)':
        his_19 = open('даты 19 век.png', 'rb')
        bot.send_document(message.chat.id, his_19)
        his_19.close()
    if message.text == 'Основные даты по истории(20 век)':
        his_20 = open('даты 20 век.jpg', 'rb')
        bot.send_document(message.chat.id, his_20)
        his_20.close()
    if message.text == 'Обществознание':
        keyboard4 = ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard4.add(KeyboardButton('Человек'), KeyboardButton('Общество'))
        keyboard4.add(KeyboardButton('Познание'), KeyboardButton('Социальная связь'))
        keyboard4.add(KeyboardButton('Экономика'), KeyboardButton('Право'))
        keyboard4.add(KeyboardButton('Политика'), KeyboardButton('Вернуться в главное меню'))
        bot.send_message(message.chat.id, 'Выберите раздел:', reply_markup=keyboard4)
    tabl_chelovek = open('Chelovek_Vse_tablitsy.docx', 'rb')
    tabl_obsh = open('Obschestvo_Vse_tablitsy.docx', 'rb')
    tabl_poznanie = open('Poznanie_Vse_tablitsy.docx', 'rb')
    tabl_socsvyaz = open('Sotsialnaya_svyaz_Vse_tablitsy.docx', 'rb')
    tabl_economy = open('Ekonomika_Vse_tablitsy.docx', 'rb')
    tabl_pravo = open('Pravo_Vse_tablitsy.docx', 'rb')
    tabl_polit = open('Politika_Vse_tablitsy.docx', 'rb')
    if message.text == 'Человек':
        bot.send_document(message.chat.id, tabl_chelovek)
        tabl_chelovek.close()
        bot.send_message(message.chat.id, 'Материал по теме: "Человек"')
    if message.text == 'Общество':
        bot.send_document(message.chat.id, tabl_obsh)
        tabl_obsh.close()
        bot.send_message(message.chat.id, 'Материал по теме: "Общество"')
    if message.text == 'Познание':
        bot.send_document(message.chat.id, tabl_poznanie)
        tabl_poznanie.close()
        bot.send_message(message.chat.id, 'Материал по теме: "Познание"')
    if message.text == 'Социальная связь':
        bot.send_document(message.chat.id, tabl_socsvyaz)
        tabl_socsvyaz.close()
        bot.send_message(message.chat.id, 'Материал по теме: "Социальная связь"')

    if message.text == 'Экономика':
        bot.send_document(message.chat.id, tabl_economy)
        tabl_economy.close()
        bot.send_message(message.chat.id, 'Материал по теме: "Экономика"')
    if message.text == 'Право':
        bot.send_document(message.chat.id, tabl_pravo)
        tabl_pravo.close()
        bot.send_message(message.chat.id, 'Материал по теме: "Право"')
    if message.text == 'Политика':
        bot.send_document(message.chat.id, tabl_polit)
        tabl_polit.close()
        bot.send_message(message.chat.id, 'Материал по теме: "Политика"')

    if message.text == 'Столовая':
        bot.send_message(message.chat.id,
                         "Завтрак(122,90₽): Какао на молоке/Чай \n Хлеб из муки пшеничной \n Яблоко \n Молоко сгущенное с сахаром/Джем \n Лимон(ломтик) \n Запеканка из творога \n Сахар порционный\n Обед(228,96₽): Хлеб пшеничный \n Хлеб ржано-пшеничный \n Свекла отварная \n Огурец соленый \n Масло растительное \n Соус томатный \n Напиток из сухофруктов/Чай \n Гречка отварная рассыпчатая \n Суп Минестроне/Булон куриный с зеленью \n Митболы \n Сахар порционный \n Кукуруза консервированная")


# Запускаем бота
bot.polling(none_stop=True)
