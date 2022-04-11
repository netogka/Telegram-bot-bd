import telebot, wikipedia, re
from telebot import types

bot = telebot.TeleBot("ТОКЕН")
wikipedia.set_lang("ru")

def ask(message):
    if message.text.lower() == "журнализация":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Тунель №1")
        button2 = types.KeyboardButton("Тунель №2")
        back = types.KeyboardButton("Выйти")
        markup.add(button1, back, button2)
        bot.send_message(message.chat.id,text="Вы правильно подобрали пароль!!! Дверь открылась, перед Вами два тунеля, в которые можно пройти. Выберите один из них.",reply_markup=markup)
    elif message.text.lower() == "администратор бд":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Продолжить проходить квест")
        back = types.KeyboardButton("Выйти")
        markup.add(button1, back)
        bot.send_message(message.chat.id,text="Поздравляю, Вы доказали, что вы не заражённый и Вас пропустили в безопасную зону, но будьте начеку!",reply_markup=markup)
    elif message.text.lower() == "сущность":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Вернуться к тунелям")
        back = types.KeyboardButton("Выйти")
        markup.add(button1,back)
        bot.send_message(message.chat.id,text="Поздравляю, Вы правильно ответили, но Вы в тупике.",reply_markup=markup)
        bot.send_message(message.chat.id, "😭")
    elif message.text.lower() == "три" or message.text =="3":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Выйти")
        markup.add(back)
        bot.send_message(message.chat.id, text="Поздравляю, Вы прошли квест, теперь Вы знаете основы БД и СУБД.",reply_markup=markup)
    elif message.text == "Выйти":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Поиск в Wikipedia🔍")
        button2 = types.KeyboardButton("Документация📚")
        button3 = types.KeyboardButton("Скачать книгу📕")
        button4 = types.KeyboardButton("Квест🏃")
        back = types.KeyboardButton("Главное меню🚪")
        markup.add(button1, button2, button3, button4, back)
        bot.send_message(message.chat.id, text="Вы вышли из квеста.", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Пароль неверный!!!Попробуйте ещё раз")
        bot.register_next_step_handler(message, ask)
def kvest(message):
    if message.text == "Квест🏃" or message.text == "/quest":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Запустить")
        button2 = types.KeyboardButton("Выйти")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Нажми кнопку Запустить, если желаете пройти квест", reply_markup=markup)
    elif message.text == "Запустить":
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        button1 = types.KeyboardButton("Дверь №1")
        button2 = types.KeyboardButton("Дверь №2")
        button3 = types.KeyboardButton("Дверь №3")
        back = types.KeyboardButton("Выйти")
        markup.add(button1, button2, button3,back)
        bot.send_message(message.chat.id, "Ну что начинаем")
        bot.send_message(message.chat.id,text="Работает сирена...\nВы проснулись в заброшенном МРК, понимаете, что Вы находитесь в бункере. Перед Вами три двери:\n1.Тупик.\n2.Ведёт на этаж выше.\n3.Ведёт Вас на улицу к смертельно-опасному вирусу.\nПеред Вами сложный выбор, время идёт.",reply_markup=markup)
    elif message.text == "Дверь №1":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Начать заново")
        back = types.KeyboardButton("Выйти")
        markup.add(button1,back)
        bot.send_message(message.chat.id, "Вы открываете дверь видя перед собой луч свет, вдыхаете ядовитые пары, которые передаются воздушно-капельным путём, Вы умираете на улице, как и все жители планеты Земля.", reply_markup=markup)
        bot.send_message(message.chat.id, "😷")
    elif message.text == "Дверь №2":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Дверь №1")
        button2 = types.KeyboardButton("Дверь №2")
        button3 = types.KeyboardButton("Дверь №3")
        back = types.KeyboardButton("Выйти")
        markup.add(button1, button2, button3, back)
        bot.send_message(message.chat.id, "Вы выбрали дверь, которая ведёт в тупик, попробуйте снова.")
        bot.send_message(message.chat.id,"😭", reply_markup=markup)
    elif message.text == "Дверь №3":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Выйти")
        markup.add(back)
        bot.send_message(message.chat.id, "Вы открываете дверь видя перед собой электронный замок c клавиатурой, который можно открыть только правильно подобрав пароль! Чтобы подобрать пароль нужно ответить на вопрос.", reply_markup=markup)
        bot.send_message(message.chat.id, "Как называется функция СУБД, которая записывает последнее изменение в журнал БД?")
        bot.register_next_step_handler(message, ask)
    elif message.text == "Начать заново":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Дверь №1")
        button2 = types.KeyboardButton("Дверь №2")
        button3 = types.KeyboardButton("Дверь №3")
        back = types.KeyboardButton("Выйти")
        markup.add(button1, button2, button3, back)
        bot.send_message(message.chat.id,text="Работает сирена...\nВы проснулись в заброшенном МРК, понимаете, что Вы находитесь в бункере. Перед Вами три двери:\n1.Тупик;\n2.Ведёт на этаж выше;\n3.Ведёт Вас на улицу к смертельно-опасному вирусу;\nПеред Вами сложный выбор, время идёт.",reply_markup=markup)

    elif message.text =="Выйти":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Поиск в Wikipedia🔍")
        button2 = types.KeyboardButton("Документация📚")
        button3 = types.KeyboardButton("Скачать книгу📕")
        button4 = types.KeyboardButton("Квест🏃")
        back = types.KeyboardButton("Главное меню🚪")
        markup.add(button1, button2, button3, button4, back)
        bot.send_message(message.chat.id,text="Вы вышли из квеста.",reply_markup=markup)
    elif message.text == "Тунель №1":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("⬅")
        button2 = types.KeyboardButton("⬆")
        button3 = types.KeyboardButton("➡")
        back = types.KeyboardButton("Выйти")
        markup.add(button1, button2,button3,back)
        bot.send_message(message.chat.id,text="Воу! Перед вами развилка, нужно выбрать правильное направление пути:\nНалево\nПрямо\nНаправо\nПредупреждаю, там может ждать опасность!", reply_markup=markup)
    elif message.text == "Вернуться к развилке":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("⬅")
        button2 = types.KeyboardButton("⬆")
        button3 = types.KeyboardButton("➡")
        back = types.KeyboardButton("Выйти")
        markup.add(button1, button2, button3, back)
        bot.send_message(message.chat.id,text="Воу! Перед вами развилка, нужно выбрать правильное направление пути:\nНалево\nПрямо\nНаправо\nПредупреждаю, там может ждать опасность!",reply_markup=markup)
    elif message.text == "⬅" or message.text == "➡":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Вернуться к развилке")
        back = types.KeyboardButton("Выйти")
        markup.add(button1,back)
        bot.send_message(message.chat.id, "Увы, тупик.")
        bot.send_message(message.chat.id, "😭", reply_markup=markup)
    elif message.text == "⬆":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Выйти")
        markup.add(back)
        bot.send_message(message.chat.id, "Перед Вами стоит военный, который не пропустит Вас в безопасную зону без подтвержения, что вы не заражённый!!!", reply_markup=markup)
        bot.send_message(message.chat.id, "Чтобы он Вас пропустил, требуется ответить на вопрос:\nКак называется лицо, отвечающее за выработку требований к базе данных, её проектирование, реализацию, эффективное использование и сопровождение?")
        bot.register_next_step_handler(message, ask)
    elif message.text == "Тунель №2":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Выйти")
        markup.add(back)
        bot.send_message(message.chat.id,text="Ой ой ой, ЗОМБИ беги!!! Чтобы скрыться от зомби, ответьте на вопрос",reply_markup=markup)
        bot.send_message(message.chat.id, text="Как называется объект, о котором в системе будет накапливаться информация?")
        bot.register_next_step_handler(message, ask)
    elif message.text == "Вернуться к тунелям":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Тунель №1")
        button2 = types.KeyboardButton("Тунель №2")
        back = types.KeyboardButton("Выйти")
        markup.add(button1, back, button2)
        bot.send_message(message.chat.id,text="Вы правильно подобрали пароль!!! Дверь открылась, перед вами два тунеля в которые можно пройти выберите один из них", reply_markup=markup)
    elif message.text == "Продолжить проходить квест":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        run = types.KeyboardButton("Бежать")
        back = types.KeyboardButton("Выйти")
        markup.add(run,back)
        bot.send_message(message.chat.id,"S-O-S!!! На безопасную зону напали, срочно нужно уходить.",reply_markup=markup)
    elif message.text == "Бежать":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Открыть люк")
        button2 = types.KeyboardButton("Не открывать")
        back = types.KeyboardButton("Выйти")
        markup.add(button1, button2,back)
        bot.send_message(message.chat.id,"Перед Вами лестница, а за ней люк. Если Вы его откроете, то там Вас может ждать, что угодно! Выбор за вами.",reply_markup=markup)
    elif message.text == "Открыть люк":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Выйти")
        markup.add(back)
        bot.send_message(message.chat.id,"Чтобы открыть, введите пароль.",reply_markup=markup)
        bot.send_message(message.chat.id, "Пароль: Сколько существует нормальных форм?")
        bot.register_next_step_handler(message, ask)
    elif message.text == "Не открывать":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Начать заново")
        back = types.KeyboardButton("Выйти")
        markup.add(button1,back)
        bot.send_message(message.chat.id, "Вы погибли!", reply_markup=markup)
        bot.send_message(message.chat.id, "😷")
    else:
        bot.send_message(message.chat.id, text="Увы, я такое не умею.")

def get_text_messages(message):
    if message.text == "Нет":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Задать вопрос❓")
        button2 = types.KeyboardButton("🆘HELP🆘")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=markup)
    elif message.text == "Задать вопрос❓" or message.text == "/reference":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как тебя зовут?")
        btn2 = types.KeyboardButton("Что ты можешь?")
        back = types.KeyboardButton("Главное меню🚪")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, "Задай мне вопрос...", reply_markup=markup)
    elif message.text == "Как тебя зовут?":
        bot.send_message(message.chat.id, "Меня зовут БДэшечка.")
    elif message.text == "Что ты можешь?":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Поиск в Wikipedia🔍")
        button2 = types.KeyboardButton("Документация📚")
        button3 = types.KeyboardButton("Скачать книгу📕")
        button4 = types.KeyboardButton("Квест🏃")
        back = types.KeyboardButton("Главное меню🚪")
        markup.add(button1, button2, button3, button4, back)
        bot.send_message(message.chat.id, "Поиск в Wikipedia🔍\nОтправить учебник📕\nРассказать многое о БД и СУБД📚\nКвест🏃", reply_markup=markup)
    elif message.text == "Скачать книгу📕" or message.text == "/book":
        bot.send_message(message.from_user.id, "Подождите\nЗагружаю книгу...")
        f = open(r'book.pdf', 'rb')
        bot.send_document(message.chat.id, f, timeout=150)
    elif message.text == "Главное меню🚪":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Задать вопрос❓")
        button2 = types.KeyboardButton("🆘HELP🆘")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=markup)
    elif message.text == "🆘HELP🆘" or message.text == "/help":
        bot.send_message(message.chat.id, "Я бот который может:\n- осуществить поиск в Wikipedia🔍;\n- отправить учебник📕;\n- рассказать многое о БД и СУБД📚;\n-предложить квест🏃.")
    else:
        documents(message)

def documents(message):
    if message.text == "Документация📚" or message.text == "/db":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("1 раздел")
        button2 = types.KeyboardButton("2 раздел")
        button3 = types.KeyboardButton("3 раздел")
        button4 = types.KeyboardButton("4 раздел")
        button5 = types.KeyboardButton("5 раздел")
        button6 = types.KeyboardButton("6 раздел")
        button7 = types.KeyboardButton("7 раздел")
        back = types.KeyboardButton("Вернуться назад⬅")
        markup.add(button1, button2, button3, button4, button5, button6, button7, back)
        bot.send_message(message.chat.id, "Выберите раздел книги, чтобы узнать подробнее.", reply_markup=markup)

    elif message.text == "Вернуться назад⬅":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Поиск в Wikipedia🔍")
        button2 = types.KeyboardButton("Документация📚")
        button3 = types.KeyboardButton("Скачать книгу📕")
        button4 = types.KeyboardButton("Квест🏃")
        back = types.KeyboardButton("Главное меню🚪")
        markup.add(button1, button2, button3, button4, back)
        bot.send_message(message.chat.id, "Вы вернулись в меню с функциями", reply_markup=markup)

    elif message.text == "1 раздел":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("1.1 История развития представлений о БД")
        button2 = types.KeyboardButton("1.2 Основные функции и типовая организаци современной СУБД")
        button3 = types.KeyboardButton("1.3 Ранние подходы к организации СУБД")
        button4 = types.KeyboardButton("1.4 Общие понятие реляционного подхода к организации БД")
        button5 = types.KeyboardButton("1.5 Базисные средства манипулирования данными")
        button6 = types.KeyboardButton("1.6 Проектирование реляционных БД")
        back = types.KeyboardButton("Назад к разделам⬅")
        markup.add(button1, button2, button3, button4, button5, button6, back)
        bot.send_message(message.chat.id, "Выберите тему первого раздела, которая Вас интересует.", reply_markup=markup)

    elif message.text == "1.1 История развития представлений о БД":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Банк данных")
        button2 = types.KeyboardButton("Информационная система")
        button3 = types.KeyboardButton("База данных")
        button4 = types.KeyboardButton("СУБД")
        button5 = types.KeyboardButton("Приложения")
        button6 = types.KeyboardButton("Словарь данных")
        button7 = types.KeyboardButton("Администратор БД")
        button8 = types.KeyboardButton("Вычислительная система")
        button9 = types.KeyboardButton("Обслуживающий персонал")
        back = types.KeyboardButton("Назад к темам⬅")
        markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, back)
        bot.send_message(message.chat.id, "Выберите термин, определение которого Вы хотите узнать.", reply_markup=markup)

    elif message.text == "Банк данных":
        bot.send_message(message.chat.id,
                         text="Банк данных является разновидностью ИС, в которой реализованы функции централизованного хранения и накопления обрабатываемой информации, организованной в одну или несколько БД.")
    elif message.text == "Информационная система":
        bot.send_message(message.chat.id,
                         "Информационная система(ИС) - это аппаратно-программные средства, задействованные для решения некоторых прикладных задач.")
    elif message.text == "База данных":
        bot.send_message(message.chat.id,
                         "База данных(БД) представляет собой совокупность специальным образом организованных данных, хранимых в памяти ВС и отображающих состояние объектов и их взаимосвязи в рассматриваемой предметной области.")
    elif message.text == "СУБД":
        bot.send_message(message.chat.id,
                         "СУБД — комплекс языковых и программных средств, предназначенных для создания, ведения и совместного использования БД многими пользователями.")
    elif message.text == "Приложения":
        bot.send_message(message.chat.id,"Приложения представляют собой программу или комплекс программ, обеспечивающих автоматизацию обработки информации для прикладной задачи.")
    elif message.text == "Словарь данных":
        bot.send_message(message.chat.id,
                         "Словарь данных представляет собой подсистему банка данных, предназначенную для централизованного хранения информации о структурах данных, взаимосвязях файлов, типах данных,форматах их представления, принадлежности данных пользователя, кодак зашиты и разграничения доступа.")
    elif message.text == "Администратор БД":
        bot.send_message(message.chat.id,
                         "Администратор БД — лицо или группа лиц, отвечающая за выбор требований к БД, ее проектирование. создание, эффективное использование и сопровождение.")
    elif message.text == "Вычислительная система":
        bot.send_message(message.chat.id,
                         "Вычислительная система представляет собой совокупность взаимосвязанных и согласованно действующих ЭВМ, процессора и других устройств, обеспечивающих автоматизацию процессов приема, обработки и выдачи информации потребителю.")
    elif message.text == "Обслуживающий персонал":
        bot.send_message(message.chat.id, "Обслуживающий персонал выполняет функции поддержания работы технических и программных средств.")

    elif message.text == "1.2 Основные функции и типовая организаци современной СУБД":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Основные функции современной СУБД")
        button2 = types.KeyboardButton("Типовая организация современной СУБД")
        back = types.KeyboardButton("Назад к темам⬅")
        markup.add(button1, button2, back)
        bot.send_message(message.chat.id, "Выберите раздел темы, информация о котором Вас интересует.", reply_markup=markup)

    elif message.text == "Основные функции современной СУБД":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("1.Непосредственное управление данными во внешней памяти")
        button2 = types.KeyboardButton("2.Управление буферами оперативной памяти")
        button3 = types.KeyboardButton("3.Управление транзакциями")
        button4 = types.KeyboardButton("4.Журнализация")
        button5 = types.KeyboardButton("5.Поддержка языков БД")
        back = types.KeyboardButton("Назад к теме 1.2⬅")
        markup.add(button1, button2, button3, button4, button5, back)
        bot.send_message(message.chat.id, "Выберите подраздел темы для получения дополнительной информации.", reply_markup=markup)

    elif message.text == "1.Непосредственное управление данными во внешней памяти":
        bot.send_message(message.chat.id,"Функция включает обсепечение необходимых структур внешней памяти как для хранения данных, непосредственно входящих в БД, так и для служебных целей.")
    elif message.text == "2.Управление буферами оперативной памяти":
        bot.send_message(message.chat.id, "Буферизация данных в оперативной памяти предназначена для увеличения скорости работы СУБД с БД, обращения к элементу данных.")
    elif message.text == "3.Управление транзакциями":
        bot.send_message(message.chat.id, "Транзакция - последовательность операций над БД, рассматриваемых СУБД как единое целое. Понятие необходимо для поддержания логической целостности БД.")
    elif message.text == "4.Журнализация":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Аппаратные/Программные сбои")
        button2 = types.KeyboardButton("Журнал")
        button3 = types.KeyboardButton("Архивная копия")
        back = types.KeyboardButton("Назад к \"Основные функции СУБД\"⬅")
        markup.add(button1, button2, button3, back)
        bot.send_message(message.chat.id, "Надежность хранения данных во внешней памяти - возможность восстановления последнего согласованного состояния БД после любого аппаратного или программного сбоя.",reply_markup=markup)
    elif message.text == "Аппаратные/Программные сбои":
        bot.send_message(message.chat.id, "Аппаратные сбои:\n-мягкие сбои - внезапная остановка работы компьютера;\n-жесткие сбои - потеря информации на носителях внешней памяти.\nПрограммные сбои: аварийное завершение работы СУБД.")
    elif message.text == "Журнал":
        bot.send_message(message.chat.id, "Журнал - особая часть БД, недоступная пользователям СУБД и поддерживаемая с особой тщательностью, в которую поступают записи обо всех изменениях основной части БД.")
    elif message.text == "Архивная копия":
        bot.send_message(message.chat.id, "Архивная копия - полная копия БД к моменту начала заполнения журнала")
    elif message.text == "5.Поддержка языков БД":
        bot.send_message(message.chat.id, "Выделялись язык определения схемы БД (SDL), язык манипулирования данными (DML). Единый интегрированный язык, содержащий все необходимые средства для работы с БД - SQL.")
    elif message.text == "Типовая организация современной СУБД":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Ядро СУБД")
        button2 = types.KeyboardButton("Компилятор языка БД")
        button3 = types.KeyboardButton("Утилиты БД")
        back = types.KeyboardButton("Назад к теме 1.2⬅")
        markup.add(button1, button2, button3, back)
        bot.send_message(message.chat.id, "В современной реляционной СУБД можно выделить: ядро, компилятор языка БД, подсистема поддержки времени выполнения, набор утилит.",reply_markup=markup)
    elif message.text == "Ядро СУБД":
        bot.send_message(message.chat.id, "Ядро отвечает за управление данными во внешней памяти, буферами оперативной памяти, транзакциями и журнализацию.\nКомпоненты:\n-менеджер данных;\n-менеджер буферов;\n-менеджер транзакций;\n-менеджер журнала.")
    elif message.text == "Компилятор языка БД":
        bot.send_message(message.chat.id, "Основная функция - компиляция операторов языка БД в некоторую выполняемую программу.")
    elif message.text == "Утилиты БД":
        bot.send_message(message.chat.id, "Отдельные утилиты БД - процедуры, которые слишком накладно выполнять с использвоанием языка БД (загрузка и выгрузка БД), программируются с использованием интерфейса ядра СУБД.")

    elif message.text == "1.3 Ранние подходы к организации СУБД":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Ранние системы")
        button2 = types.KeyboardButton("Инвертированные списки")
        button3 = types.KeyboardButton("Иерархические системы")
        button4 = types.KeyboardButton("Сетевые системы")
        button5 = types.KeyboardButton("Достоинства")
        button6 = types.KeyboardButton("Недостатки")
        back = types.KeyboardButton("Назад к темам⬅")
        markup.add(button1, button2, button3, button4, button5, button6, back)
        bot.send_message(message.chat.id, "Выберите необходимый раздел темы для осведомления.", reply_markup=markup)

    elif message.text == "Ранние системы":
        bot.send_message(message.chat.id, "Ранние системы:\n1.Основанные на инвертированных списках.\n2.Иерархические.\n3.Сетевые.")
    elif message.text == "Инвертированные списки":
        bot.send_message(message.chat.id, "Простота организации БД; ряд ограничений на количество файлов для хранения данных, количество связей между ними, длину записи и количество ее полей. Хранимые таблицы и пути доступа к ним видны пользователям.")
    elif message.text == "Иерархические системы":
        bot.send_message(message.chat.id, "Упорядоченный набор нескольких экземпляров одного типа дерева, который состоит из одного \"корневого\" типа записи и упорядоченного набора из нуля или более типов поддеревьев - иерархически организованный набор типов записи.")
        img = open('erarBD.png', 'rb')
        bot.send_photo(message.chat.id, img, "Схема иерархической БД")
    elif message.text == "Сетевые системы":
        bot.send_message(message.chat.id, "Организация данных - расширение иерархического подхода, однако потомок может иметь любое число предков. Состоит из набора записей и набора связей между ними. Тип связи определяется для предка и потомка. Экзепмпляр типа связи состоит из одного экземпляра типа записи предка и упорядоченного набора экземпляров типа записи потомка.")
        img = open('setBD.png', 'rb')
        bot.send_photo(message.chat.id, img, "Схема сетевой БД")
    elif message.text == "Достоинства":
        bot.send_message(message.chat.id, "Достоинства:\n1.Развитые средства управления данными вовнешней памяти на низком уровне.\n2.Возможность построения вручную эффективных прикладных систем.\n3.Возможность экономии памяти за счет разделения подобъектов.")
    elif message.text == "Недостатки":
        bot.send_message(message.chat.id, "Недостатки\n1.Сложное пользование.\n2.Необходимы знания о физической организации\n3.Прикладные системы зависят от физической организации.\n4.Логика перегружена деталями организации доступа к БД.")

    elif message.text == "1.4 Общие понятие реляционного подхода к организации БД":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Сущность")
        button2 = types.KeyboardButton("Отношение")
        button3 = types.KeyboardButton("Свойства отношений")
        button4 = types.KeyboardButton("Первичный/внешний ключ")
        button5 = types.KeyboardButton("Индекс")
        button6 = types.KeyboardButton("Ссылочная целостность")
        button7 = types.KeyboardButton("Консистентность данных")
        back = types.KeyboardButton("Назад к темам⬅")
        markup.add(button1, button2, button3, button4, button5, button6, button7, back)
        bot.send_message(message.chat.id, "Выберите раздел темы, который Вам интересен.", reply_markup=markup)

    elif message.text == "Сущность":
        bot.send_message(message.chat.id, "Сущность - объект любой природы, данные о котором хранятся в БД. Данные хранятся в отношении.")
    elif message.text == "Отношение":
        img = open('otn.png', 'rb')
        bot.send_photo(message.chat.id, img, "Пример отношения \"Сотрудники\"")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Атрибут")
        button2 = types.KeyboardButton("Домен")
        button3 = types.KeyboardButton("Схема отношений")
        button4 = types.KeyboardButton("Кортеж")
        button5 = types.KeyboardButton("Степень отношения")
        button6 = types.KeyboardButton("Мощность отношения")
        back = types.KeyboardButton("Назад к теме 1.4⬅")
        markup.add(button1, button2, button3, button4, button5, button6, back)
        bot.send_message(message.chat.id, "Выберите понятие, которое Вас интересует.", reply_markup=markup)
    elif message.text == "Атрибут":
        bot.send_message(message.chat.id, "Атрибут - свойство, характеризующее сущность. В структуре таблицы каждый атрибут именуется и ему в соответствие ставится заголовок некоторого столбца таблицы.")
    elif message.text == "Домен":
        bot.send_message(message.chat.id, "Домен - множество всех возможных значений оперделенного атрибута отношений.")
    elif message.text == "Схема отношений":
        bot.send_message(message.chat.id, "Схема отношений - список имен атрибутов.")
    elif message.text == "Кортеж":
        bot.send_message(message.chat.id, "Кортеж - строка таблицы. Множество кортежей отношений - содержимое отношения.")
    elif message.text == "Степень отношения":
        bot.send_message(message.chat.id, "Степень(-арность) отношения - количество столбцов таблицы.")
    elif message.text == "Мощность отношения":
        bot.send_message(message.chat.id, "Мощность отношения - количество строк таблицы.")
    elif message.text == "Свойства отношений":
        bot.send_message(message.chat.id, "Основные свойтсва отношений:\n1.В отношении нет одинаковых кортежей.\n2.Кортежи не упорядочены(сверху вниз), строки могут идти в различном порядке.\n3.Атрибуты не упорядочены (слева направо), столбцы могут идти в различном порядке.\nТаблица задает отношение, если она имеет простую структуру, нет одинаковых строк, столбец содержит данные одного типа, простые типы данных.")
    elif message.text == "Первичный/внешний ключ":
        bot.send_message(message.chat.id, "Первичным ключом называются атрибуты отншения, однозначно идентифицирующие каждый из его кортежей. Может быть составным (сложным) - состоять из нескольких атрибутов.\nВнешний ключ устанавливает связи между отношениями, ссылки на первичные ключи.")
    elif message.text == "Индекс":
        bot.send_message(message.chat.id, "Индекс - средство ускорения операций поиска записей в таблице и других операций (выборка, модификация, сортировка).")
    elif message.text == "Ссылочная целостность":
        bot.send_message(message.chat.id, "Ссылочная целостность - свойство реляционной БД, которое заключается в отсутствии в отношении внешних ключей, ссылающихся на несуществующие кортежи. Условие сохранения ссылочной целостности - поддержка транзакций. Механизм триггеров прдназначен для поддержания ссылочной целостности, созается над потенциально опасной операцией, проводит необходимые проверки или изменяет данные в связанных таблицах.")
    elif message.text == "Консистентность данных":
        bot.send_message(message.chat.id, "Консистентность данных - согласованность данных друг с другом, их целостность, а также внутренняя непротиворечивость. Условия целостности данных записываются в виде правил и введены триггеры - процедуры, которые вызываются до и/или после выполнения запроса.")

    elif message.text == "1.5 Базисные средства манипулирования данными":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Реляционная алгебра")
        button2 = types.KeyboardButton("Объединение")
        button3 = types.KeyboardButton("Вычитание")
        button4 = types.KeyboardButton("Пересечение")
        button5 = types.KeyboardButton("Произведение")
        button6 = types.KeyboardButton("Выборка")
        button7 = types.KeyboardButton("Проекция")
        button8 = types.KeyboardButton("Деление")
        button9 = types.KeyboardButton("Соединение")
        button10 = types.KeyboardButton("Реляционное исчисление")
        back = types.KeyboardButton("Назад к темам⬅")
        markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, back)
        bot.send_message(message.chat.id, "Выберите раздел темы для получения требуемых навыков.", reply_markup=markup)

    elif message.text == "Реляционная алгебра":
        bot.send_message(message.chat.id,"Реляционная алгебра - процедурный язык обработки реляционных таблиц (пошаговый принцип создания таблиц, содержащих ответы на запросы). Описывает выполняемые над отношениями действия.")
    elif message.text == "Объединение":
        bot.send_message(message.chat.id, "Объединением двух совместимых отношений R1 и R2 одинаковой размерности (R1 UNION R2) является отношение R, содержащее все элементы исходных значений (за исключением повторений).")
        img = open('obet2.png', 'rb')
        img2 = open('obet.png', 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_photo(message.chat.id, img2)
    elif message.text == "Вычитание":
        bot.send_message(message.chat.id, "Вычитание совместимых отношений R1 и R2 одинаковой размерности (R1 MINUS R2) есть отношение, тело которого состоит из множества кортежей, принадлежащих R1, но не принадлежащих отношению R2.")
        img = open('vuch.png', 'rb')
        bot.send_photo(message.chat.id, img)
    elif message.text == "Пересечение":
        bot.send_message(message.chat.id, "Пересечение двух совместимых отношений R1 и R2 одинаковой размерности (R1 INTERSECT R2) порождает отношение R с телом, включающим в себя кортежи, одновременно принадлежащие обоим исходным отношениям.")
        img = open('peresech.png', 'rb')
        bot.send_photo(message.chat.id, img)
    elif message.text == "Произведение":
        bot.send_message(message.chat.id, "Произведение отношения R1 степени k1 и отношения R2 степени k2 (R1 TIMES R2), которые не имеют одинаковых имен атрибутов, есть такое отношение R степени (k1 + k2), заголовок которого представляет сцепление заголовков отношений R1 и R2, а тело - имеет кортежи, такие, что первые k1 элементов кортежей принадлежат множеству R1, а последние k2 элементов - множеству R2.")
        img = open('proez2.png', 'rb')
        img2 = open('proez.png', 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_photo(message.chat.id, img2)
    elif message.text == "Выборка":
        bot.send_message(message.chat.id, "Выборка (R WHERE f) отношения R по формуле f представляет собой новое отношение с таким же заголовком и телом, состоящим из таких кортежей отношения R, которые удовлетворяют истинности логического выражения, заданного формулой f.")
        img = open('vuborka2.png', 'rb')
        img2 = open('vuborka.png', 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_photo(message.chat.id, img2)
    elif message.text == "Проекция":
        bot.send_message(message.chat.id, "Проекция отношения A на атрибуты X, Y, ..., Z (A[X, Y, ..., Z]), где множество {X, Y, ..., Z} является подмножеством полного списка атрибутов заголовка отношения A, представляет собой отношение с заголовком X, Y, ..., Z и телом, содержащим кортежи отношения A, за исключением повторяющихся кортежей. Повторение одинаковых атрибутов в спсике X, Y, ..., Z запрещается.")
        img = open('proe2.png', 'rb')
        img2 = open('proe.png', 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_photo(message.chat.id, img2)
    elif message.text == "Деление":
        bot.send_message(message.chat.id, "Результатом деления отношения R1 с атрибутами A и B на отношение R2 с атрибутом B (R1 DIVIDEBY R2), где A и B простые или составные атрибуты, причем атрибут B - общий атрибут, определенный на одном и том же домене (множестве доменов составного атрибута), является отношением R с заголовком A и телом, состоящим из кортежей r таких, что в отношении R1 имеются кортежи (r, s), причем множество значений s включает множество значений атрибута B отношения R2.")
        img = open('del2.png', 'rb')
        img2 = open('del.png', 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_photo(message.chat.id, img2)
    elif message.text == "Соединение":
        bot.send_message(message.chat.id, "Cf(R1, R2) отношений R1 и R2 по условию, заданному формулой f, представляет собой отношение R, которое можно получить путем декартова произведения отношений R1 и R2 с последующим применением к результату операции выборки по формуле f.")
        img = open('soed.png', 'rb')
        bot.send_photo(message.chat.id, img)
    elif message.text == "Реляционное исчисление":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Предикат")
        button2 = types.KeyboardButton("Формы")
        back = types.KeyboardButton("Назад к теме 1.5⬅")
        markup.add(button1, button2, back)
        bot.send_message(message.chat.id, "Реляционное исчисление - это непроцедурный язык обработки отношений, в котором результирующая таблица ответа на запрос формируется за один шаг. Происходит от части символьной логики - исчисление предикатов.")
    elif message.text == "Предикат":
        bot.send_message(message.chat.id, "Предикат - истинностная функция с аргументами (при подстановке вместо аргументов значений эта функция становится выражением, называемым суждением, которое может быть истинным или ложным).")
    elif message.text == "Формы":
        bot.send_message(message.chat.id, "Две формы:\n1.Реляционное исчисление кортежей. Основанно на переменных кортежей данного отношения. Задача: нахождение таких кортежей, для которых предикат является истинным.\n2.Реялционное исчисление доменов. Используются переменные, значения которых берутся из доменов. Задача: определить принадлежат ли значения указанному отношению.")

    elif message.text == "1.6 Проектирование реляционных БД":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Проектирование БД")
        button2 = types.KeyboardButton("Методология проектирования")
        button3 = types.KeyboardButton("Концептуальное проектирование")
        button4 = types.KeyboardButton("Логическое проектирование")
        button5 = types.KeyboardButton("Первая нормальная форма (1НФ)")
        button6 = types.KeyboardButton("Вторая нормальная форма (2НФ)")
        button7 = types.KeyboardButton("Третья нормальная форма (3НФ)")
        button8 = types.KeyboardButton("Физическое проектирование")
        back = types.KeyboardButton("Назад к темам⬅")
        markup.add(button1, button2, button3, button4, button5, button6, button7, button8, back)
        bot.send_message(message.chat.id, "Выберите интересующий Вас раздел темы.", reply_markup=markup)
    elif message.text == "Проектирование БД":
        bot.send_message(message.chat.id,"Проектирование БД - процесс, который для заданного набора данных, относящихся к некоторой предметной области, позволяет выбрать и построить соответствующую оптимальную структуру.")
    elif message.text == "Методология проектирования":
        bot.send_message(message.chat.id, "Методология проектирования - структурированный подход, предусматривающий использование специализированных процедур, технических приемов, инструментов, документации и нацеленный на поддержку и упрощение процесса проектирования.")
    elif message.text == "Концептуальное проектирование":
        bot.send_message(message.chat.id, "Коцептуальное проектирование БД - это процедура конструирования информационной модели, не зависящей от каких-либо физических условий реализации.\nПодходы:\n1.Функциональный подход к проектированию БД.\n2.Предметный подход к проектированию БД.\n3.Проектирование с использованием метода \"сущность-связь\".")
    elif message.text == "Логическое проектирование":
        bot.send_message(message.chat.id, "Логическое проектирование БД - процесс конструирования информационной модели на основе выбора из существующих логических моделей данных, но не зависимой от конкретной СУБД и прочих физических условий реализации.\nЭтапы:\n1.Построение адекватной логической модели.\n2.Создание и проверка глобальной логической модели данных на основе локальных логических моделей.")
    elif message.text == "Первая нормальная форма (1НФ)":
        bot.send_message(message.chat.id, "Требования:\n1.Отсутствие повторяющихся записей (первичный ключ).\n2.Отсутствие повторяющихся групп полей (сущности).\n3.Атрибуты и строки не упорядочены.\n4.Значения атрибутов атомарны.")
    elif message.text == "Вторая нормальная форма (2НФ)":
        bot.send_message(message.chat.id, "Требования:\n1.Удовлетворение условиям 1НФ.\n2.Любое неключевое поле однозначно идентифицируется полным набором ключевых полей.")
    elif message.text == "Третья нормальная форма (3НФ)":
        bot.send_message(message.chat.id, "Требования:\n1.Удовлетворение условиям 2НФ.\n2.Ни одно из неключевых полей таблицы не идентифицируется с помощью другого неключевого поля.")
    elif message.text == "Физическое проектирование":
        bot.send_message(message.chat.id, "Физическое проектирование БД - процесс реализации БД, размещаемой во вторичной памяти вычислительной системы, при котором выполняется отображение созданной глобальной логической модели на особенностях конкретной СУБД.\nЭтапы:\n1.Перенос глобальной логической модели в среду целевой СУБД.\n2.Проектирование физического представления БД.\n3.Разработка механизмов защиты.\n4.Организация мониторинга и настройка функционирования системы.")

    elif message.text == "Назад к теме 1.2⬅":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Основные функции современной СУБД")
        button2 = types.KeyboardButton("Типовая организация современной СУБД")
        back = types.KeyboardButton("Назад к разделам⬅")
        markup.add(button1, button2, back)
        bot.send_message(message.chat.id, text="Вы вернулись к теме 1.2", reply_markup=markup)
    elif message.text == "Назад к теме 1.4⬅":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Сущность")
        button2 = types.KeyboardButton("Отношение")
        button3 = types.KeyboardButton("Свойства отношений")
        button4 = types.KeyboardButton("Первичный/внешний ключ")
        button5 = types.KeyboardButton("Индекс")
        button6 = types.KeyboardButton("Ссылочная целостность")
        button7 = types.KeyboardButton("Консистентность данных")
        back = types.KeyboardButton("Назад к темам")
        markup.add(button1, button2, button3, button4, button5, button6, button7, back)
        bot.send_message(message.chat.id, text="Вы вернулись к теме 1.4", reply_markup=markup)
    elif message.text == "Назад к теме 1.5⬅":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Реляционная алгебра")
        button2 = types.KeyboardButton("Объединение")
        button3 = types.KeyboardButton("Вычитание")
        button4 = types.KeyboardButton("Пересечение")
        button5 = types.KeyboardButton("Произведение")
        button6 = types.KeyboardButton("Выборка")
        button7 = types.KeyboardButton("Проекция")
        button8 = types.KeyboardButton("Деление")
        button9 = types.KeyboardButton("Соединение")
        button10 = types.KeyboardButton("Реляционное исчисление")
        back = types.KeyboardButton("Назад к темам⬅")
        markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, back)
        bot.send_message(message.chat.id, text="Вы вернулись к теме 1.5", reply_markup=markup)
    elif message.text == "Назад к \"Основные функции СУБД\"⬅":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Основные функции современной СУБД")
        button2 = types.KeyboardButton("Типовая организация современной СУБД")
        back = types.KeyboardButton("Назад к разделам⬅")
        markup.add(button1, button2, back)
        bot.send_message(message.chat.id, text="Вы вернулись к подразделу \"Основные функции СУБД\"", reply_markup=markup)
    elif message.text == "Назад к темам⬅":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("1.1 История развития представлений о БД")
        button2 = types.KeyboardButton("1.2 Основные функции и типовая организаци современной СУБД")
        button3 = types.KeyboardButton("1.3 Ранние подходы к организации СУБД")
        button4 = types.KeyboardButton("1.4 Общие понятие реляционного подхода к организации БД")
        button5 = types.KeyboardButton("1.5 Базисные средства манипулирования данными")
        button6 = types.KeyboardButton("1.6 Проектирование реляционных БД")
        back = types.KeyboardButton("Назад к разделам⬅")
        markup.add(button1, button2, button3, button4, button5, button6, back)
        bot.send_message(message.chat.id, text="Вы вернулись к темам 1 раздела", reply_markup=markup)
    elif message.text == "Назад к разделам⬅":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("1 раздел")
        button2 = types.KeyboardButton("2 раздел")
        button3 = types.KeyboardButton("3 раздел")
        button4 = types.KeyboardButton("4 раздел")
        button5 = types.KeyboardButton("5 раздел")
        button6 = types.KeyboardButton("6 раздел")
        button7 = types.KeyboardButton("7 раздел")
        back = types.KeyboardButton("Вернуться назад⬅")
        markup.add(button1, button2, button3, button4, button5, button6, button7, back)
        bot.send_message(message.chat.id, text="Вы вернулись к разделам", reply_markup=markup)
    else:
        kvest(message)

def wiki_text(message):
    if message.text == "Назад⬅":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Поиск в Wikipedia🔍")
        button2 = types.KeyboardButton("Документация📚")
        button3 = types.KeyboardButton("Скачать книгу📕")
        button4 = types.KeyboardButton("Квест🏃")
        back = types.KeyboardButton("Главное меню🚪")
        markup.add(button1, button2, button3, button4, back)
        bot.send_message(message.chat.id, text="Вы вернулись к главному меню", reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Поиск в Wikipedia🔍")
        button2 = types.KeyboardButton("Документация📚")
        button3 = types.KeyboardButton("Скачать книгу📕")
        button4 = types.KeyboardButton("Квест🏃")
        back = types.KeyboardButton("Главное меню🚪")
        markup.add(button1, button2, button3, button4, back)
        bot.send_message(message.from_user.id, "Вот что нашлось по вашему запросу:", reply_markup=markup)
        bot.send_message(message.from_user.id, getwiki(message.text))

def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not ('==' in x):
                if (len((x.strip())) > 3):
                    wikitext2 = wikitext2 + x + '.'
            else:
                break
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
        return 'В энциклопедии нет информации об этом.'


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Задать вопрос❓")
    btn2 = types.KeyboardButton("🆘HELP🆘")
    book = types.InlineKeyboardButton(text="Скачать книгу", callback_data="book")
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, 'Привет, {0.first_name}! Меня зовут БДэшечка, я помогу тебе разобраться с дисциплиной \"Базы данных и Системы управления базами данных\"!'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text', 'document', 'audio'])
def text_message(message):
    if message.text == "Поиск в Wikipedia🔍" or message.text == "/Wikipedia":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Назад⬅")
        markup.add(btn1)
        bot.send_message(message.from_user.id, '{0.first_name}, отправь мне любое слово, и я найду его значение на Wikipedia.'.format(message.from_user), reply_markup=markup)
        bot.register_next_step_handler(message, wiki_text)
    else:
        get_text_messages(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "book":
        bot.send_message(call.message.from_user.id, "Подождите \nЗагружаю книгу...")
        f = open(r'СУБД учебник.pdf', 'rb')
        bot.send_document(call.message.chat.id, f, timeout=150)


bot.polling(none_stop=True, interval=0)