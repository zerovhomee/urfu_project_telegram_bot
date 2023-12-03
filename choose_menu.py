from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

BOT_TOKEN = '6431964212:AAEFA-isNUFeEf8WajXSg-Ycb5wNGYJP3rY'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

button_start = KeyboardButton(text='Выбрать курс самостоятельно')
button_job_info = KeyboardButton(text = 'Подробное описание специальности')

@dp.message(CommandStart())
async def start_message(message: Message):
    keyboard_start = ReplyKeyboardMarkup(
        keyboard=[[button_start],
                  [button_job_info]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Привет!</b>\n'
        '\n'
        '<b>Это бот, созданный для помощи начинающим it-специалистам</b> '
        '<b>в поиске информации для обучения. У бота на выбор есть две функции:</b>\n'
        '\n'
        '1. Поболтать с Chat GPT и спросить его про то, что вас интересует\n'
        '2. Выбрать курс самостоятельно с помощью данного бота\n'
        '\n'
        '<i>Чтобы воспользоваться второй функцией, нажмите кнопку</i> '
        '<i>"Выбрать курс самостояльно"</i>\n'
        '\n'
        '<i>Чтобы поболтать с gpt, выберите команду /choose из меню слева</i>\n'
        '\n'
        '<b>Если вы не знаете, с чего начать для вас есть функция</b> '
        '<b>"Подробное описание специальности" где вы можете ознакомиться </b>'
        '<b>с тем, чем занимается каждый специалист и сможете выбрать то, что вам\n</b>'
        '<b>больше по душе</b>\n'
        '\n'
        '<b>Если вы нашли ошибку или у вас есть пожелания по работе бота </b>\n'
        '<b>Вы можете связаться с <a href="https://t.me/zerovhomee">автором</a></b>',
        parse_mode='HTML',
        reply_markup=keyboard_start
    )


button_devops_job = KeyboardButton(text='DevOps инженер')

button_frontend_job = KeyboardButton(text='Frontend разработчик')

button_backend_job = KeyboardButton(text='Backend разработчик')

button_mobile_job = KeyboardButton(text='Mobile-разработчик')

button_qa_job = KeyboardButton(text='QA-тестировщик')

button_gamedev_job = KeyboardButton(text='GameDeveloper')

button_datascience_job = KeyboardButton(text='DataScientist')

button_machine_learning_job = KeyboardButton(text='ML специалист')

button_systemengineer_job = KeyboardButton(text='System Engineer')

button_job_menu = KeyboardButton(text = 'Меню специальностей')

@dp.message(F.text == 'Подробное описание специальности')
async def job_info(message: Message):
    keyboard_job_info = ReplyKeyboardMarkup(
        keyboard=[[button_devops_job, button_frontend_job, button_backend_job],
            [button_mobile_job, button_qa_job, button_gamedev_job],
            [button_datascience_job, button_machine_learning_job, button_systemengineer_job]],
        resize_keyboard=True
    )
    await message.answer(
        text = 'Выберите специальность',
        reply_markup=keyboard_job_info
    )



@dp.message(F.text == 'DevOps инженер')
async def devopsjob(message: Message):
    keyboard_devopsjob = ReplyKeyboardMarkup(
        keyboard=[[button_start],
                  [button_job_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '  Основная цель DevOps (Development and Operations) - ускорить процесс\n'
        'разработки программного обеспечения, повысить его качество и \n'
        'улучшить коммуникацию между различными командами. Это позволяет\n'
        'компаниям быстрее реагировать на требования рынка, минимизировать \n'
        'ошибки и достигать более высокой эффективности в разработке и\n'
        'эксплуатации приложений.\n'
        '\n'
        '  DevOps включает в себя использование методологий Agile и Continuous\n'
        'Integration/Continuous Delivery (CI/CD). Agile подразумевает гибкую \n'
        'методологию разработки, которая акцентируется на частых итерациях и \n'
        'вовлечении заинтересованных сторон. CI/CD позволяет\n'
        'автоматизировать процессы разработки и развертывания приложений, \n'
        'что ускоряет время выхода на рынок и повышает качество.',
        reply_markup=keyboard_devopsjob
    )



@dp.message(F.text == 'Frontend разработчик')
async def frontendjob(message: Message):
    keyboard_frontendjob = ReplyKeyboardMarkup(
        keyboard=[[button_start],
                  [button_job_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '  Front-End - это раздел веб-разработки, отвечающий за создание того, что \n'
        'пользователи видят и с чем взаимодействуют на веб-сайтах и \n'
        'приложениях\n'
        '\n'
        '  Frontend-разработчики работают с языками программирования, такими \n'
        'как HTML (гипертекстовый язык разметки), CSS (каскадные таблицы\n'
        'стилей) и JavaScript, чтобы создавать интерактивные и отзывчивые \n'
        'пользовательские интерфейсы. \n'
        '\n'
        '  Frontend-разработчики также могут использовать различные \n'
        'фреймворки и библиотеки, такие как React, Angular и Vue.js, для более \n'
        'эффективной разработки интерфейсов. Они также занимаются \n'
        'оптимизацией производительности и адаптивным дизайном, чтобы \n'
        'обеспечить хорошую работу интерфейса на разных устройствах и веб-браузерах',
        reply_markup=keyboard_frontendjob
    )



@dp.message(F.text == 'Backend разработчик')
async def backendjob(message: Message):
    keyboard_backendjob = ReplyKeyboardMarkup(
        keyboard=[[button_start],
                  [button_job_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '  Backend - это термин, используемый веб-разработкой для обозначения \n'
        'части веб-приложения, отвечающей за обработку данных и \n'
        'взаимодействие с базой данных. Он отвечает за логику работы\n'
        'приложения, обработку запросов от клиентской стороны, хранение и \n'
        'извлечение данных из базы данных, а также обеспечение безопасности \n'
        'и масштабируемости системы.\n'
        '\n'
        '  Backend-разработчики обычно работают с серверными языками \n'
        'программирования, такими как Python, Java, PHP, Ruby или Node.js, а \n'
        'также с базами данных, такими как MySQL, PostgreSQL или MongoDB. \n'
        'Они разрабатывают API (Application Programming Interface), которое \n'
        'определяет способы взаимодействия клиентской стороны с сервером. \n'
        'API предоставляет различные эндпоинты, через которые клиентская \n'
        'сторона может отправлять запросы на сервер и получать ответы.',
        reply_markup=keyboard_backendjob
    )




@dp.message(F.text == 'Mobile-разработчик')
async def mobilejob(message: Message):
    keyboard_mobilejob = ReplyKeyboardMarkup(
        keyboard=[[button_start],
                  [button_job_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = 'Mobile developer (разработчик мобильных приложений) — это\n'
        'специалист по созданию программного обеспечения для мобильных \n'
        'устройств, таких как смартфоны и планшеты. Работа включает в себя\n'
        'проектирование, разработку, тестирование и поддержку мобильных \n'
        'приложений.\n'
        '\n'
        'Разработчики обычно специализируются либо на iOS (языки Swift или\n'
        'Objective-C, инструменты разработки Xcode), либо на Android (языки Java \n'
        'или Kotlin, Android Studio), хотя некоторые работают с обеими \n'
        'платформами или используют кросс-платформенные инструменты, \n'
        'такие как Flutter, React Native или Xamarin.',
        reply_markup=keyboard_mobilejob
    )




@dp.message(F.text == 'QA-тестировщик')
async def qajob(message: Message):
    keyboard_qajob = ReplyKeyboardMarkup(
        keyboard=[[button_start],
                  [button_job_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = 'QA Tester, или специалист по контролю качества программного \n'
        'обеспечения (Quality Assurance Tester), отвечает за обнаружение ошибок \n'
        'и проблем в программном обеспечении до того, как оно станет доступно\n'
        'конечным пользователям. Основная задача QA Tester — гарантировать, \n'
        'что продукт отвечает установленным требованиям и критериям качества.\n'
        '\n'
        'Цель работы QA Tester состоит в том, чтобы помочь команде доставить \n'
        'наиболее функциональный и надежный продукт пользователю,\n'
        'минимизируя количество дефектов и недочетов при его использовании.',
        reply_markup=keyboard_qajob
    )




@dp.message(F.text == 'GameDeveloper')
async def gamedevjob(message: Message):
    keyboard_gamedevjob = ReplyKeyboardMarkup(
        keyboard=[[button_start],
                  [button_job_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '"Game developer" (разработчик игр) — это специалист, \n'
        'который занимается созданием видеоигр. \n'
        '\n'
        'Разработчики игр могут работать одни (инди-разработчики) или в \n'
        'составе крупных студий. Размер проектов может варьироваться от \n'
        'простых мобильных или инди-игр до массивных тройных А-проектов с \n'
        'огромными бюджетами и командами.',
        reply_markup=keyboard_gamedevjob
    )




@dp.message(F.text == 'DataScientist')
async def gamedevjob(message: Message):
    keyboard_datasciencejob = ReplyKeyboardMarkup(
        keyboard=[[button_start],
                  [button_job_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = 'Data science - это область, которая комбинирует методы, инструменты и \n'
        'алгоритмы для извлечения знаний из данных. Она объединяет более \n'
        'традиционные научные и статистические методы с современными \n'
        'технологиями и вычислительной мощью для анализа, интерпретации и \n'
        'вывода практически значимой информации из больших объемов\n'
        'данных. \n'
        '\n'
        'Data science включает в себя процессы сбора данных, их очистки и \n'
        'преобразования, анализа данных, создания моделей, обучение моделей\n'
        'на основе данных и принятие решений на основе полученных\n'
        'результатов. Для работы в области data science требуется знание \n'
        'программирования, статистики, математики и обширные навыки в \n'
        'области обработки данных и работы с различными инструментами и \n'
        'платформами, такими как языки программирования Python или R, \n'
        'инструменты визуализации данных, базы данных и машинное обучение.',
        reply_markup=keyboard_datasciencejob
    )



@dp.message(F.text == 'ML специалист')
async def machinelearningjob(message: Message):
    keyboard_machinelearningjob = ReplyKeyboardMarkup(
        keyboard=[[button_start],
                  [button_job_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = 'Machine learning (ML) — это область искусственного интеллекта, которая \n'
        'включает в себя методы, позволяющие компьютерам учиться на опыте и \n'
        'улучшать свою работу без явного программирования для конкретной \n'
        'задачи. Machine learning модели анализируют большие массивы данных, \n'
        'чтобы находить закономерности и делать предсказания.\n'
        '\n'
        'Машинное обучение используется в самых разных приложениях, \n'
        'начиная от рекомендательных систем и заканчивая автономными \n'
        'автомобилями.',
        reply_markup=keyboard_machinelearningjob
    )




@dp.message(F.text == 'System Engineer')
async def systemengineerjob(message: Message):
    keyboard_systemengineerjob = ReplyKeyboardMarkup(
        keyboard=[[button_start],
                  [button_job_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = 'Системная инженерия (System Engineering) — это междисциплинарная\n'
        'область, связанная с управлением и разработкой сложных систем. Она \n'
        'объединяет принципы и методы различных научных и инженерных\n'
        'дисциплин для создания, анализа и управления системами такими, как \n'
        'информационные системы, технические системы, социотехнические \n'
        'системы и другие.\n'
        '\n'
        'Основная цель системной инженерии заключается в обеспечении\n'
        'оптимальной работы системы в рамках заданных требований. Для этого \n'
        'системные инженеры проводят анализ и моделирование системы, \n'
        'определяют требования к системе, разрабатывают архитектуру системы, \n'
        'осуществляют интеграцию компонентов и проверяют работоспособность \n'
        'системы в целом.',
        reply_markup=keyboard_systemengineerjob
    )




@dp.message(F.text == 'Меню специальностей')
async def job_info(message: Message):
    keyboard_job_info = ReplyKeyboardMarkup(
        keyboard=[[button_devops_job, button_frontend_job, button_backend_job],
            [button_mobile_job, button_qa_job, button_gamedev_job],
            [button_datascience_job, button_machine_learning_job, button_systemengineer_job]],
        resize_keyboard=True
    )
    await message.answer(
        text = 'Выберите специальность',
        reply_markup=keyboard_job_info
    )


button_devops = KeyboardButton(text='DevOps')

button_frontend = KeyboardButton(text='Frontend')

button_backend = KeyboardButton(text='Backend')

button_mobile = KeyboardButton(text='Mobile-разработка')

button_qa = KeyboardButton(text='QA-тестирование')

button_gamedev = KeyboardButton(text='GameDev')

button_datascience = KeyboardButton(text='DataScience')

button_machine_learning = KeyboardButton(text='Machine Learning')

button_systemengineer = KeyboardButton(text='System Engineering')

button_main_menu = KeyboardButton(text = 'Главное меню')


main_menu = ReplyKeyboardMarkup(
    keyboard=[[button_devops, button_frontend, button_backend],
            [button_mobile, button_qa, button_gamedev],
            [button_datascience, button_machine_learning, button_systemengineer]],
    resize_keyboard=True
    )

@dp.message(F.text == 'Выбрать курс самостоятельно')
async def choose_menu(message: Message):
    await message.answer(
        text='Выберите интересующее вас направление',
        reply_markup=main_menu
    )
@dp.message(F.text == 'Главное меню')
async def back_menu_button(message: Message):
    await message.answer(
        text='Выберите интересующее вас направление',
        reply_markup=main_menu
    )
button_frontend_info = KeyboardButton(text = 'Что нужно изучить frontend')
button_frontend_main = KeyboardButton(text = 'Перейти к курсам frontend')

@dp.message(F.text == 'Frontend')
async def frontend_main(message: Message):
    keyboard_frontend = ReplyKeyboardMarkup(
        keyboard=[[button_frontend_info, button_frontend_main],
                  [button_main_menu]],
        resize_keyboard=True
        )
    await message.answer(
        text='Хотите узнать что нужно изучить или сразу перейдете к курсам?',
        reply_markup=keyboard_frontend
    )

@dp.message(F.text == 'Что нужно изучить frontend')
async def what_to_know_frontend(message: Message):
    keyboard_frontend_info = ReplyKeyboardMarkup(
        keyboard=[[button_frontend_main],
                  [button_main_menu]],
        resize_keyboard=True
        )
    await message.answer(
        text='<b>Основные технологии:</b>\n'
        '\n'
        'HTML5 & CSS3\n'
        'Flex и Grid CSS\n'
        'CSS препроцессоры\n'
        'Git & GitHub\n'
        'Знание о веб-технологиях и сети интернет\n'
        'JavaScript\n'
        'JavaScript Core (DOM, AJAX, JSON)\n'
        'REST API\n'
        'Алгоритмы и структуры данных\n'
        'Фреймворки JavaScript(React/Vue/Angular)\n'
        'Инструменты управления состоянием программы (State Management)\n'
        'TypeScript\n'
        'Основы Figma\n'
        'Английский язык\n'
        '\n'
        '<b>Необязательные технологии</b>\n'
        '\n'
        'Паттерны проектирования JavaScript\n'
        'Линтеры\n'
        'Тестирование\n'
        'Webpack\n'
        'Gulp/Grunt\n'
        'SOLID принципы\n',
        parse_mode='HTML',
        reply_markup = keyboard_frontend_info
    )
button_frontend_youtube = KeyboardButton(text = 'Видео с Youtube Frontend')
button_frontend_courses = KeyboardButton(text = 'Курсы Frontend')
button_frontend_books = KeyboardButton(text = 'Книги Frontend')

@dp.message(F.text == 'Перейти к курсам frontend')
async def choose_menu_frontend(message: Message):
    keyboard_choose_frontend = ReplyKeyboardMarkup(
        keyboard=[[button_frontend_youtube],
                  [button_frontend_courses,button_frontend_books],
                  [button_main_menu]],
        resize_keyboard=True
        )
    await message.answer(
        text='Выберите источник информации',
        reply_markup=keyboard_choose_frontend
    )

@dp.message(F.text == 'Видео с Youtube Frontend')
async def youtube_frontend(message: Message):
    keyboard_youtube_frontend = ReplyKeyboardMarkup(
        keyboard=[[button_frontend_courses,button_frontend_books],
                  [button_main_menu]],
        resize_keyboard=True
        )
    await message.answer(
        text='<b>Ссылки на обучающие youtube - видео</b>\n'
            '\n'
            '1. БЕСПЛАТНЫЙ курс по верстке сайтов. Верстка сайтов с нуля. Канал: Фрилансер по жизни\n'
            'https://youtube.com/playlist?list=PLM6XATa8CAG4F9nAIYNS5oAiPotxwLFIr&si=1aalLThO4Hk_6TnM\n'
            '\n'
            '2. Изучение HTML5 для новичков с нуля!. Канал: школа it Proger\n'
            'https://youtube.com/playlist?list=PLDyJYA6aTY1nlkG0gBj96XDmDSC4Fy1TO&si=oV-ra0wYqZ1gehFs\n'
            '\n'
            '3. Курс по Frontend разработке. Канал: Арокен.ру\n'
            'https://youtube.com/playlist?list=PLNaJj8xMY1XQgYzVhLEFD4WSKqEhj4Sx1&si=bYZDtaAs6hpc868x\n'
            '\n'
            '4. Frontend Web Development Bootcamp Course (JavaScript, HTML, CSS). Канал: FreeCodeCamp\n'
            'https://youtu.be/zJSY8tbf_ys?si=vJjSYu8F1azDFhQy\n'
            '\n'
            '5. Курс практической верстки. Канал: WebDev с нуля\n'
            'https://youtube.com/playlist?list=PLM7wFzahDYnF6V3FOkFMzwAwyJDlVP_kL&si=LLzr3REIQItETwgO\n',
            parse_mode='HTML',
        reply_markup=keyboard_youtube_frontend
    )

@dp.message(F.text == 'Курсы Frontend')
async def courses_frontend(message: Message):
    keyboard_courses_frontend = ReplyKeyboardMarkup(
        keyboard = [[button_frontend_books],
                    [button_frontend_youtube],
                    [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Платные курсы по frontend разработке</b>\n'
        '\n'
        '1. Профессия Frontend-разработчик от Skillbox\n'
        'https://skillbox.ru/course/frontend-developer-service/\n'
        '<a href="https://www.sravni.ru/shkola/skillbox/otzyvy/594949/">Отзывы</a>\n'
        '\n'
        '2. Frontend-разработчик: быстрый старт в профессии от GeekBrains\n'
        'https://gb.ru/geek_university/developer/programmer/frontend\n'
        '<a href="https://gb.ru/professions/frontend_developer/feedbacks">Отзывы</a>\n'
        '\n'
        '3. Frontend-разработчик: расширенный курс от Нетологии\n'
        'https://netology.ru/programs/front-end\n'
        '<a href="https://eduverse.ru/netology/frontend-razrabotcik-s-nulya/reviews">Отзывы</a>\n'
        '\n'
        '4. «Фронтенд-разработчик» от HTML Академии\n'
        'https://htmlacademy.ru/profession/frontender\n'
        '<a href="https://www.sravni.ru/shkola/html-academy/otzyvy/">Отзывы</a>\n'
        '\n'
        '5. Курс «Фронтенд-разработчик» от Хекслет\n'
        'https://ru.hexlet.io/programs/frontend\n'
        '<a href="https://eduverse.ru/hexlet/reviews">Отзывы</a>\n'
        '\n'
        '6. FRONT-END разработчик от itProger\n'
        'https://itproger.com/intensive/front-end\n'
        '<a href="https://t.me/itproger_front">Отзывы</a>\n'
        '\n'
        '<b>Бесплатные курсы:</b>\n'
        '\n'
        '1. Основы вёрстки сайта от Нетологии\n'
        'https://netology.ru/programs/html-css-base#/\n'
        '\n'
        '2. Введение в веб-разработку от codenamecrud\n'
        'https://codenamecrud.ru/\n'
        '\n'
        '3. Основы HTML, CSS и веб-дизайна от Хекслет\n'
        'https://ru.hexlet.io/courses/html\n'
        '\n'
        '4. Foundations of Front-End Web Development от Udemy\n'
        'https://www.udemy.com/course/foundations-of-front-end-development/\n'
        '\n'
        '5. React JS Frontend Web Development for Beginners от Udemy\n'
        'https://www.udemy.com/course/react-tutorial/\n'
        '\n'
        '6. JavaScript для начинающих от Stepik\n'
        'https://stepik.org/course/2223/promo',
        parse_mode='HTML',
        reply_markup=keyboard_courses_frontend
    )

@dp.message(F.text == 'Книги Frontend')
async def books_frontend(message: Message):
    keyboard_books_frontend = ReplyKeyboardMarkup(
        keyboard=[[button_frontend_youtube],
                  [button_frontend_courses],
                  [button_main_menu]],
        resize_keyboard=True
        )
    await message.answer(
        text='<b>Вот несколько рекомендаций по книгам для изучения HTML, CSS и JavaScript:</b>\n'
        '\n'
        '1. "HTML и CSS. Дизайн и разработка веб-сайтов" автора Джона Дакетта\n'
        'https://www.labirint.ru/books/687374/\n'
        '\n'
        '2. "JavaScript и jQuery. Интерактивные веб-страницы" автора Джона Дакетта\n'
        'https://www.labirint.ru/books/583161/\n'
        '\n'
        '3. "Выразительный JavaScript" автора Марейна Хавербеке - \n'
        'https://www.litres.ru/book/mareyn-haverbeke/vyrazitelnyy-javascript-sovremennoe-veb-programmirovanie-50447564/\n'
        '\n'
        '4. "CSS-секреты. Трюки и эффекты" автора Леа Веру -\n'
        'https://razrab.info/book/sekrety-css-lea-veru/\n'
        '\n'
        '5. "Eloquent JavaScript. A Modern Introduction to Programming" автора Марейна Хавербеке\n'
        'https://eloquentjavascript.net/\n',
        parse_mode='HTML',
        reply_markup=keyboard_books_frontend
    )
button_dev_ops_info = KeyboardButton(text = 'Что нужно изучить DevOps')
button_dev_ops_main = KeyboardButton(text = 'Перейти к курсам DevOps')

@dp.message(F.text == 'DevOps')
async def dev_ops_main(message: Message):
    keyboard_dev_ops_main = ReplyKeyboardMarkup(
        keyboard=[[button_dev_ops_info, button_dev_ops_main],
                  [button_main_menu]],
        resize_keyboard=True
        )
    await message.answer(
        text='Хотите узнать что нужно изучить или сразу перейдете к курсам?',
        reply_markup=keyboard_dev_ops_main
    )

@dp.message(F.text == 'Что нужно изучить DevOps')
async def dev_ops_what_to_know(message: Message):
    keyboard_dev_ops_info = ReplyKeyboardMarkup(
        keyboard=[[button_dev_ops_main],
                  [button_main_menu]],
        resize_keyboard=True
        )
    await message.answer(
        text='<b>Основные технологии:</b>\n'
        '\n'
        'Непрерывная разработка и интеграция: Jenkins, TeamCity, GitLab\n'
        'Bamboo, Github Actions, AWS CodePipeline.\n'
        '\n'
        'Архитектура как код: Terraform, Puppet, Ansible.\n'
        '\n'
        'Облачная архитектура: AWS, Google Cloud Platform, Microsoft Azure\n'
        'Huawei Cloud, Яндекс Облако, Mail.ru Cloud Solutions.\n'
        '\n'
        'Мониторинг: Prometheus, Grafana.\n'
        '\n'
        'Системы логирования, трассировки: ELK Stack, Graylog, Grafana, Jaeger.\n'
        '\n'
        'Контейнеризация и оркестрация: Docker, Podman, Kubernetes, Rancher.\n'
        '\n'
        '<b>Если выделять хард-скиллы по технологиям, то:</b>\n'
        '\n'
        '<i>Junior</i>\n'
        '\n'
        'основы Linux-администрирования, git;\n'
        'умение писать простые скрипты для автоматизации на Bash;\n'
        'умение дебажить (отлаживать);\n'
        'знание контейнеризации и оркестрации;\n'
        'базовый мониторинг готовыми средствами.\n'
        '\n'
        '<i>Middle</i>\n'
        '\n'
        'умение разбираться глубоко в производительности систем\n'
        '(не просто поставить MySQL, а посмотреть все настройки, explain медленных запросов и построить индексы);\n'
        'Python/Ruby/Go;\n'
        'более строгие DSL (например, Puppet);\n'
        'знание сетей, балансировка, автоматическое переключение разных компонентов без потери работоспособности;\n'
        'умение дополнять мониторинг под свои нужды.\n'
        '\n'
        '<i>Senior</i>\n'
        '\n'
        'все те же навыки, только глубже проработанные. Здесь навыки зависят от задач компании: написать eBPF для отладки,\n'
        'внедрять Test-driven-development с хорошим покрытием тестами Rspec/Serverspec,\n'
        'отвечать за архитектуру инфраструктуры в целом — всё это относится к DevOps;\n'
        'фокус на выполнение SLA, разбираться в SLO, SLI.\n',
        parse_mode='HTML',
        reply_markup = keyboard_dev_ops_info
    )
button_dev_ops_books = KeyboardButton(text = 'Книги DevOps')
button_dev_ops_youtube = KeyboardButton(text = 'Видео с Youtube DevOps')
button_dev_ops_courses = KeyboardButton(text = 'Курсы DevOps')

@dp.message(F.text == 'Перейти к курсам DevOps')
async def dev_ops_choose_menu(message: Message):
    keyboard_choose_menu = ReplyKeyboardMarkup(
        keyboard=[[button_dev_ops_youtube],
                  [button_dev_ops_courses,button_dev_ops_books],
                  [button_main_menu]],
        resize_keyboard=True
        )
    await message.answer(
        text='Выберите источник информации',
        reply_markup=keyboard_choose_menu
    )

@dp.message(F.text == 'Книги DevOps')
async def dev_ops_books(message: Message):
    keyboard_dev_ops_books = ReplyKeyboardMarkup(
        keyboard=[[button_dev_ops_youtube],
                  [button_dev_ops_courses],
                  [button_main_menu]],
        resize_keyboard=True
        )
    await message.answer(
        text='<b>Книги по DevOps</b>\n'
            '\n'
            '1. Python для сетевых инженеров. Автоматизация сети, программирование и DevOps\n'
            'https://www.labirint.ru/books/874559/\n'
            '\n'
            '2. Проект «Феникс». Как DevOps устраняет хаос и ускоряет развитие компании\n'
            'https://www.labirint.ru/books/777669/\n'
            '\n'
            '3. Ускоряйся! Наука DevOps : Как создавать и масштабировать высокопроизводительные цифровые организации\n'
            'https://www.litres.ru/book/dzhez-hambl/uskoryaysya-naukadevops-50628699/\n'
            '\n'
            '4. Kubernetes для DevOps: развертывание, запуск и масштабирование в облаке\n'
            'https://www.labirint.ru/books/736626/\n'
            '\n'
            '5. Безопасный DevOps. Эффективная эксплуатация систем\n'
            'https://www.labirint.ru/books/713545/\n'
            '\n'
            '6. Operations Anti-Patterns, DevOps Solutions\n'
            'https://clck.ru/36LqQM\n'
            '\n'
            '7. Безопасность контейнеров. Фундаментальный подход к защите контейнеризированных приложений\n'
            'https://clck.ru/36LqsW',
            parse_mode='HTML',
        reply_markup=keyboard_dev_ops_books
    )
@dp.message(F.text == 'Видео с Youtube DevOps')
async def dev_ops_youtube(message: Message):
    keyboard_dev_ops_youtube = ReplyKeyboardMarkup(
        keyboard=[[button_dev_ops_books,button_dev_ops_courses],
                  [button_main_menu]],
        resize_keyboard=True
        )
    await message.answer(
        text='<b>Ссылки на обучающие Youtube - видео:</b>\n'
        '\n'
        '1. Курс DevOps 2019-2020. Канал: Игорь А.Степин\n'
        'https://www.youtube.com/playlist?list=PLwdMROGs6anC_9EPldwVJ30TvwHvvaSiE\n'
        '\n'
        '2. Практики и инструменты DevOps. Канал: ITVDN\n'
        'https://www.youtube.com/playlist?list=PLvItDmb0sZw_xTNDv8Bb1fsivN_Z_4oo9\n'
        '\n'
        '3. Обучение DevOps с нуля. Канал: Skillbox программирование\n'
        'https://www.youtube.com/playlist?list=PLmEQTfkM_pfmE3X3mK1O8RVKUkz6ygHTR\n'
        '\n'
        '4. Курсы: Школа DevOps v.1.0. Канал: DeusOps\n'
        'https://www.youtube.com/playlist?list=PLGQiJX6wM-zzcPye1y7gpyJO0uH7NMNP7\n',
        parse_mode='HTML',
        reply_markup=keyboard_dev_ops_youtube
    )

@dp.message(F.text == 'Курсы DevOps')
async def dev_ops_courses(message: Message):
    keyboard_dev_ops_courses = ReplyKeyboardMarkup(
        keyboard=[[button_dev_ops_books],
                  [button_dev_ops_youtube],
                  [button_main_menu]],
        resize_keyboard=True
        )
    await message.answer(
        text='<b>Бесплатные курсы по DevOps</b>\n'
        '\n'
        '1. «DevOps Culture and Mindset» от Калифорнийского университета в Дейвисе\n'
        'https://clck.ru/36Ltyn\n'
        '\n'
        '2. «Continuous Delivery & DevOps» от Виргинского университета\n'
        'https://clck.ru/36Lu5v\n'
        '\n'
        '<b>Платные курсы:</b>\n'
        '\n'
        '1. DevOps-инженер: быстрый старт в профессии от GeekBrains\n'
        'https://clck.ru/36m24i\n'
        '<a href="https://www.sravni.ru/shkola/geekbrains/otzyvy/">Отзывы</a>\n'
        '\n'
        '2. DevOps-инженер от SkillFactory\n'
        'https://clck.ru/36m27v\n'
        '<a href="https://eduverse.ru/skillfactory/reviews">Отзывы</a>\n'
        '\n'
        '3. Курс «DevOps для эксплуатации и разработки» от Яндекс Практикума\n'
        'https://clck.ru/36m2Dh\n'
        '<a href="https://education.pikabu.ru/courses-dev/yandex-practicum/devops-dlya-ekspluatatsii-i-razrabotki">Отзывы</a>\n'
        '\n'
        '4. DevOps-инженер от Нетологии\n'
        '<a href="https://eduverse.ru/netology/devops-inzener">Отзывы</a>\n'
        'https://clck.ru/36m2K5',
        parse_mode='HTML',
        reply_markup=keyboard_dev_ops_courses
    )

button_data_science_info = KeyboardButton(text = 'Что нужно изучить Data Science')
button_data_science_main = KeyboardButton(text = 'Перейти к курсам Data Science')

@dp.message(F.text == 'DataScience')
async def data_science_main(message: Message):
    keyboard_data_science_main = ReplyKeyboardMarkup(
        keyboard=[[button_data_science_info, button_data_science_main],
                  [button_main_menu]],
        resize_keyboard=True
        )
    await message.answer(
        text='Хотите узнать что нужно изучить или сразу перейдете к курсам?',
        reply_markup=keyboard_data_science_main
    )

button_data_science_courses = KeyboardButton(text = 'Курсы Data Science')
button_data_science_books = KeyboardButton(text = 'Книги Data Science')
button_data_science_youtube = KeyboardButton(text = 'Видео с Youtube Data Science')

@dp.message(F.text == 'Что нужно изучить Data Science')
async def data_science_what_to_know(message: Message):
    keyboard_data_science_info = ReplyKeyboardMarkup(
        keyboard=[[button_data_science_main],
                  [button_main_menu]],
        resize_keyboard=True
        )
    await message.answer(
        text = '<b>Технические навыки Data Science:</b>\n'
        '\n'
        'Основы программирования(Python,R)\n'
        'Английский уровня Advanced Proficiency для чтения технической литературы\n'
        'Библиотеки (pandas, numpy, scikit-learn)\n'
        'Базы данных(MySQL)\n'
        'RestAPI\n'
        'Статистика и математика\n'
        'Владение инструментами обработки больших данных: Apache Spark и Hadoop Mapreduce.\n'
        'Дата-инжиниринг\n'
        'Контернейниразация(Docker,Jenkins)\n'
        'Облачные сервисы(Google Cloud, Amazon AWS)\n'
        'Работа с командной строкой(Linux)\n'
        'Машинное обучение\n'
        'Многофункциональный DL(TensorFlow,PyTorch)\n'
        'Большие языковые модели(GPT,Bard,YaGPT)\n'
        '\n'
        '<b>Требования к джуниору, мидлу и сеньору Data Scientist</b>\n'
        '\n'
        '<i>Junior Data Scientist</i>\n'
        '\n'
        'Базовые знания машинного обучения и статистики. Понимание основных алгоритмов и области их применения.\n'
        'Опыт применения: не обязателен, максимум — учебный проект.\n'
        'Программирование: уверенный Python и базовое знание SQL.\n'
        '\n'
        '<i>Middle Data Scientist</i>\n'
        '\n'
        'Глубокие знания математики.\n'
        'Опыт: 2–3 решённых проекта.\n'
        'Программирование: уверенный Python и знание его особенностей в плане продуктивизации моделей и оптимизации работы.\n'
        'Уверенные знания по культуре проведения экспериментов,'
        'работа с инструментами внедрения и поддержки моделей машинного обучения:'
        'gitLFS, MLFlow, DVC. Знание A/B-тестирования.\n'
        '\n'
        '<i>Senior Data Scientist</i>\n'
        '\n'
        'Глубокие, уверенные знания математики и статистики\n'
        'Опыт: от 5 решённых проектов.\n'
        'Программирование: уверенные Python, SQL.\n'
        'Экспертные знания в своей области\n'
        'Полная самостоятельность от постановки задачи до вывода в продакшен.\n'
        'Способность обучать и менторить младших и продвинутых специалистов\n'
        '\n'
        'Источник: https://practicum.yandex.ru/blog/kto-takoy-data-scientist/',
        parse_mode='HTML',
        reply_markup = keyboard_data_science_info
    )
@dp.message(F.text == 'Перейти к курсам Data Science')
async def data_science_choose_menu(message: Message):
    keyboard_data_science_choose = ReplyKeyboardMarkup(
        keyboard=[[button_data_science_youtube],
                  [button_data_science_books,button_data_science_courses],
                  [button_main_menu]],
        resize_keyboard=True
        )
    await message.answer(
        text = 'Выберите источник информации',
        reply_markup = keyboard_data_science_choose
    )
@dp.message(F.text == 'Видео с Youtube Data Science')
async def data_science_youtube(message: Message):
    keyboard_data_science_youtube = ReplyKeyboardMarkup(
        keyboard = [[button_data_science_books,button_data_science_courses],
                    [button_main_menu]],
        resize_keyboard = True
    )
    await message.answer(
        text = '<b>Обучающие видео с Youtube:</b>\n'
        '\n'
        '1. Learn Data Science Tutorial - Full Course for Beginners. Канал: FreeCodeCamp\n'
        'https://www.youtube.com/watch?v=ua-CiDNNj30&ab_channel=freeCodeCamp.org\n'
        '\n'
        '2. Обучаем Data Science с нуля. Канал: SkillBox программирование\n'
        'https://www.youtube.com/playlist?list=PLmEQTfkM_pfkVyU8BGamAPSdYYYe1e6PZ\n'
        '\n'
        '3. Data Science Уроки. Канал: Masters of $code\n'
        'https://www.youtube.com/playlist?list=PLCp7YGqt4kFqg11gf7ZdQmZJ5CQ1PXNUf',
        parse_mode='HTML',
        reply_markup = keyboard_data_science_youtube
    )
@dp.message(F.text == 'Курсы Data Science')
async def data_science_courses(message: Message):
    keyboard_data_science_courses = ReplyKeyboardMarkup(
        keyboard = [[button_data_science_books],
                    [button_data_science_youtube],
                    [button_main_menu]],
        resize_keyboard = True
    )
    await message.answer(
        text = '<b>Бесплатные курсы по Data Science:</b>\n'
        '\n'
        '1. A Crash Course in Data Science\n'
        'https://www.coursera.org/learn/data-science-course\n'
        '\n'
        '2. Building a Data Science Team\n'
        'https://www.coursera.org/learn/build-data-science-team\n'
        '\n'
        '3. Stepik Contest. Data Science\n'
        'https://stepik.org/course/2607/promo\n'
        '\n'
        '<b>Платные курсы:</b>\n'
        '\n'
        '1. Курс «Специалист по Data Science» от Яндекс Практикума\n'
        'https://practicum.yandex.ru/data-scientist/\n'
        '<a href="https://otzovik.com/reviews/yandeks_praktikum-kurs_specialist_po_data_science/">Отзывы</a>\n'
        '\n'
        '2. Data Scientist: быстрый старт в профессии от GeekBrains\n'
        'https://clck.ru/36m2aX\n'
        '<a href="https://www.sravni.ru/shkola/geekbrains/otzyvy/608925/">Отзывы</a>\n'
        '\n'
        '3. Data Scientist с нуля до PRO от SkillFactory\n'
        'https://clck.ru/36m2cc\n'
        '<a href="https://www.sravni.ru/shkola/skillfactory/otzyvy/511533/?/">Отзывы</a>\n'
        '\n'
        '4. Аналитик данных от Karpov Courses\n'
        'https://karpov.courses/analytics\n'
        '<a href="https://karpov.courses/cases">Отзывы</a>',
        parse_mode='HTML',
        reply_markup = keyboard_data_science_courses
    )

@dp.message(F.text == 'Книги Data Science')
async def data_science_books(message = Message):
    keyboard_data_science_books = ReplyKeyboardMarkup(
        keyboard = [[button_data_science_youtube],
                    [button_data_science_courses],
                    [button_main_menu]],
        resize_keyboard = True
    )
    await message.answer(
        text = '<b>Книги по Data Science</b>\n'
        '\n'
        '1. Дж. Грас – Data Science. Наука о данных с нуля\n'
        'https://clck.ru/36M8At\n'
        '\n'
        '2. П. Брюс, Э. Брюс – Практическая статистика для специалистов Data Science\n'
        'https://clck.ru/36M8HY\n'
        '\n'
        '3. О"Нил, Шатт – Data Science. Инсайдерская информация для новичков\n'
        'https://clck.ru/36M8QF\n'
        '\n'
        '4. Ын, Су – Теоретический минимум по Big Data. Всё что нужно знать о больших данных\n'
        'https://clck.ru/36M8XL\n'
        '\n'
        '5. Силен, Мейсман, Али – Основы Data Science и Big Data. Python и наука о данных\n'
        'https://clck.ru/36M8dk\n'
        '\n'
        '6. Дж. Вандер Плас – Python для сложных задач. Наука о данных и машинное обучение\n'
        'https://clck.ru/36M8mj',
        parse_mode='HTML',
        reply_markup = keyboard_data_science_books
    )
button_mobile_info = KeyboardButton(text = 'Что нужно знать Mobile-разработка')
button_mobile_main = KeyboardButton(text = 'Перейти к курсам Mobile-разработка')

@dp.message(F.text == 'Mobile-разработка')
async def mobile_main(message: Message):
    keyboard_mobile_main = ReplyKeyboardMarkup(
        keyboard = [[button_mobile_info, button_mobile_main],
                    [button_main_menu]],
        resize_keyboard = True
    )
    await message.answer(
        text = 'Хотите узнать что нужно изучить или сразу перейдете к курсам?',
        reply_markup=keyboard_mobile_main
    )

button_mobile_courses = KeyboardButton(text = 'Курсы Mobile-разработка')
button_mobile_books = KeyboardButton(text = 'Книги Mobile-разработка')
button_mobile_youtube = KeyboardButton(text = 'Видео с Youtube Mobile-разработка')

@dp.message(F.text == 'Перейти к курсам Mobile-разработка')
async def mobile_choose_menu(message: Message):
    keyboard_mobile_choose = ReplyKeyboardMarkup(
        keyboard = [[button_mobile_courses,button_mobile_books],
                    [button_mobile_youtube],
                    [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = 'Выберите источник информации',
        reply_markup=keyboard_mobile_choose
    )
@dp.message(F.text == 'Книги Mobile-разработка')
async def mobile_books(message: Message):
    keyboard_mobile_books = ReplyKeyboardMarkup(
        keyboard=[[button_mobile_courses],
                  [button_mobile_youtube],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Книги по мобильной разработке:</b>\n'
        '\n'
        '1. Программирование для Android (Head First). Дэвид и Дон Гриффитс\n'
        'https://clck.ru/36MBEB\n'
        '\n'
        '2. Android. Ян Ф. Дарвин\n'
        'https://clck.ru/36MBP3\n'
        '\n'
        '3. Android. Билл Филлипс, Крис Стюарт, Кристин Марсикано\n'
        'https://clck.ru/36MBWR\n'
        '\n'
        '4. Мобильная разработка. Тереза Нейл\n'
        'https://clck.ru/36MBjJ',
        parse_mode = 'HTML',
        reply_markup=keyboard_mobile_books
    )

@dp.message(F.text == 'Видео с Youtube Mobile-разработка')
async def mobile_youtube(message: Message):
    keyboard_mobile_youtube = ReplyKeyboardMarkup(
        keyboard=[[button_mobile_books,button_mobile_courses],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Обучающие видео с Youtube по мобильной разработке</b>\n'
        '\n'
        '1. Уроки Андроид Студио для начинающих. Канал: школа itProger\n'
        'https://www.youtube.com/playlist?list=PLDyJYA6aTY1nZqYprT1PKtDFthBcZWAMZ\n'
        '\n'
        '2. Курс по Kotlin для начинающих 2021. Канал: Neco Ru\n'
        'https://www.youtube.com/playlist?list=PLmjT2NFTgg1fdHN-9Wn4XYr-IOuadxMm5\n'
        '\n'
        '3. Уроки iOS Swift - Курс Swift 2021 - Swift Start. Канал: iCode School\n'
        'https://www.youtube.com/playlist?list=PLRJuPW6BGThue5qX6AkARnqc8o_80fbQA\n'
        '\n'
        '4. Курс iOS разработки. Канал: LazyLoad Swift & iOS\n'
        'https://www.youtube.com/playlist?list=PLJfJvphK-POx-wz_e9vcMnY3IhHi9MSwH\n'
        '\n'
        '5. Уроки Android Studio для начинающих. Канал: Гоша Дударь\n'
        'https://www.youtube.com/playlist?list=PL0lO_mIqDDFWa-0K21RtmCxTuhGaRiQxr\n'
        '\n'
        '6. Уроки Kotlin Android Studio / Создание Андроид программ. Канал: школа itProger\n'
        'https://www.youtube.com/playlist?list=PLDyJYA6aTY1n6NQeVSeLmfufQ0usaOdDU',
        parse_mode='HTML',
        reply_markup=keyboard_mobile_youtube
    )
@dp.message(F.text == 'Курсы Mobile-разработка')
async def mobile_courses(message: Message):
    keyboard_mobile_courses = ReplyKeyboardMarkup(
        keyboard=[[button_mobile_books],
                  [button_mobile_youtube],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Бесплатные курсы по мобильной разработке</b>\n'
        '\n'
        '1. Разработка мобильных приложений для Android от Stepik\n'
        'https://stepik.org/course/5703/promo\n'
        '\n'
        '2. Разработка Android-приложений на Kotlin от Stepik\n'
        'https://stepik.org/course/4792/promo\n'
        '\n'
        '3. Многопоточность в iOS (Swift) от Stepik\n'
        'https://stepik.org/course/3278/promo\n'
        '\n'
        '<b>Платные курсы по мобильной разработке</b>\n'
        '\n'
        '1. Мобильный разработчик от SkillBox\n'
        'https://skillbox.ru/course/profession-mobdev/\n'
        '<a href="https://www.sravni.ru/shkola/skillbox/otzyvy/614360/">Отзывы</a>\n'
        '\n'
        '2. Android-разработчик от SkillBox\n'
        'https://skillbox.ru/course/profession-android-developer/\n'
        '<a href="https://eduverse.ru/skillbox/android-razrabotcik/reviews">Отзывы</a>\n'
        '\n'
        '3. iOS-разработчик от GeekBrains\n'
        'https://gb.ru/geek_university/developer/programmer/ios\n'
        '<a href="https://eduverse.ru/geek-brains/programmist-ios">Отзывы</a>\n'
        '\n'
        '4. Android-разработчик с нуля до Junior от GeekBrains\n'
        'https://gb.ru/geek_university/developer/programmer/android\n'
        '<a href="https://otzovik.com/reviews/kurs_geekbrains_android-razrabotchik/">Отзывы</a>',
        parse_mode='HTML',
        reply_markup=keyboard_mobile_courses
    )
@dp.message(F.text == 'Что нужно знать Mobile-разработка')
async def mobile_what_to_know(message: Message):
    keyboard_mobile_info = ReplyKeyboardMarkup(
        keyboard=[[button_mobile_main],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Профессиональные навыки и знания</b>\n'
        '\n'
        '<i>Знание языков программирования:</i>\n'
        '\n'
        '<i>Apple iOS</i>: Objectiv-C, Swift, знание Apple Development Guidelines\n'
        '<i>Google Android</i>: Java, Kotlin, Scala,Android SDK,Rest/SOAP, различные API, SQLite и т.д. \n'
        '\n'
        '<i>Для обеих платформ:</i>\n'
        '\n'
        '1. знание структур и алгоритмов\n'
        '2. знание принципов ООП (к которому и относится Java, Objective-C, Swift)\n'
        '3. понимание принципов дизайна и проектирования мобильных приложений\n'
        '4. знание сетевых протоколов\n'
        '5. знание SQL\n'
        '6. навыки работы с App Store и Google Play\n'
        '7. навыки работы с многопоточностью\n'
        '8. Flutter',
        parse_mode='HTML',
        reply_markup=keyboard_mobile_info
    )

button_qa_info = KeyboardButton(text = 'Что нужно знать QA')
button_qa_main = KeyboardButton(text = 'Перейти к курсам QA')

@dp.message(F.text == 'QA-тестирование')
async def qa_main(message: Message):
    keyboard_qa_main = ReplyKeyboardMarkup(
        keyboard=[[button_qa_info,button_qa_main],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = 'Хотите узнать что нужно изучить или сразу перейдете к курсам?',
        reply_markup=keyboard_qa_main
    )

button_qa_courses = KeyboardButton(text = 'Курсы QA')
button_qa_youtube = KeyboardButton(text = 'Видео с Youtube QA')
button_qa_books = KeyboardButton(text = 'Книги QA')

@dp.message(F.text == 'Перейти к курсам QA')
async def qa_choose_menu(message: Message):
    keyboard_qa_choose = ReplyKeyboardMarkup(
        keyboard=[[button_qa_books,button_qa_courses],
                  [button_qa_youtube],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = 'Выберите источник информации',
        reply_markup=keyboard_qa_choose
    )

@dp.message(F.text == 'Курсы QA')
async def qa_courses(message: Message):
    keyboard_qa_courses = ReplyKeyboardMarkup(
        keyboard=[[button_qa_youtube],
                  [button_qa_books],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Платные курсы по QA:</b>\n'
        '\n'
        '1. Тестировщик с нуля до Junior от GeekBrains\n'
        'https://gb.ru/geek_university/developer/qa-engineer\n'
        '\n'
        '2. Профессия Инженер по тестированию от SkillBox\n'
        'https://skillbox.ru/course/profession-test/\n'
        '<a href="https://www.sravni.ru/shkola/geekbrains/otzyvy/608003/">Отзывы</a>\n'
        '\n'
        '3. Курс «Инженер по тестированию» с нуля от SkyPro\n'
        'https://sky.pro/courses/programming/qa-engineer\n'
        '<a href="https://www.sravni.ru/shkola/skypro/otzyvy/667565/">Отзывы</a>\n'
        '\n'
        '4. Инженер по тестированию: расширенный курс от Нетологии\n'
        'https://netology.ru/programs/qa-middle\n'
        '<a href="https://www.sravni.ru/shkola/netologiya/otzyvy/644934/">Отзывы</a>\n'
        '\n'
        '5. Инженер по ручному тестированию от SkillFactory\n'
        'https://skillfactory.ru/qa-engineer-po-ruchnomu-testirovaniyu\n'
        '<a href="https://www.sravni.ru/shkola/skillfactory/otzyvy/596754/">Отзывы</a>\n'
        '\n'
        '6. Онлайн курс QA Manual Engineer от QA at Silicon Valley California\n'
        'https://qasv.us/qamanual\n'
        '<a href="https://www.youtube.com/playlist?list=PL2--666ORKDmi3OPoNLh05YKtZzcKdbh4">Отзывы</a>\n'
        '\n'
        '7. Курс «Инженер по тестированию» от Яндекс Практикума\n'
        'https://practicum.yandex.ru/qa-engineer/\n'
        '<a href="https://otzovik.com/reviews/yandeks_praktikum-kurs_inzhener_po_testironiyu/">Отзывы</a>\n'
        '\n'
        '8. ПРОФЕССИЯ ИНЖЕНЕР ПО ТЕСТИРОВАНИЮ С 0 от Productstar\n'
        'https://productstar.ru/dev-prof-qa\n'
        '<a href="https://eduverse.ru/product-star/reviews">Отзывы</a>\n'
        '\n'
        '9. Инженер по тестированию от Eduson Академии\n'
        'https://eduson.academy/qa-autotester\n'
        '<a href="https://www.sravni.ru/shkola/eduson-academy/otzyvy/691302/">Отзывы</a>\n'
        '\n'
        '10. Тестировщик на Python от SkillFactory\n'
        'https://skillfactory.ru/qa-engineer-python-testirovshchik-programmnogo-obespecheniya\n'
        '<a href="https://www.sravni.ru/shkola/skillfactory/otzyvy/593233/">Отзывы</a>\n'
        '\n'
        '11. Курс Тестировщик от Нетологии\n'
        'https://netology.ru/programs/qa\n'
        '<a href="https://irecommend.ru/content/otzyv-o-kurse-testirovshchik-po-ot-netologii">Отзывы</a>\n'
        '\n'
        '<b>Бесплатные курсы по QA</b>\n'
        '\n'
        '1. Тестирование ПО 2020. С нуля до Junior QA от Stepik\n'
        'https://stepik.org/course/74555/promo\n',
        parse_mode='HTML',
        reply_markup=keyboard_qa_courses
    )

@dp.message(F.text == 'Видео с Youtube QA')
async def qa_youtube(message: Message):
    keyboard_qa_youtube = ReplyKeyboardMarkup(
        keyboard=[[button_qa_books,button_qa_courses],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Видео с Youtube по QA:</b>\n'
        '\n'
        '1. Курс "Тестировщик с нуля. Профессиональный полный курс". Канал: Artsiom Rusau QA Life\n'
        'https://www.youtube.com/playlist?list=PLKbJd47Kcbju2Vhi-FL7AI14vItVmGYk-\n'
        '\n'
        '2. Сложно ли войти в QA в 2023. Канал: АйТиБорода\n'
        'https://www.youtube.com/watch?v=aJvaOb5iwdE&pp=ygUdcWEg0LjQvdC20LXQvdC10YAg0YEg0L3Rg9C70Y8%3D\n'
        '\n'
        '3. LEARN QUALITY ASSURANCE FROM SCRATCH. Канал: alexusadays\n'
        'https://www.youtube.com/playlist?list=PLfw_nI4u_6WM8200HlderALoIYKpSa4W6\n'
        '\n'
        '4. QA Manual Testing Full Course for Beginners. Канал: SDET-QA\n'
        'https://www.youtube.com/watch?v=QJqNYhiHysM&ab_channel=SDET-QA\n'
        '\n'
        '5. Software Testing Full Course In 10 Hours. Канал: Edureka\n'
        'https://www.youtube.com/watch?v=sO8eGL6SFsA&ab_channel=edureka%21\n'
        '\n'
        '6. Курс Тестирование ПО с нуля. Канал: Serhii Hlivinskyi - QA START UP\n'
        'https://youtube.com/playlist?list=PLRs8EELOYKc7DYIQixlV1s4EH5SR3TdNB&si=CVD8mSLAp_xLrnXn\n'
        '\n'
        '7. Тестирование ПО. Профессиональный курс. Канал: Леша Маршал\n'
        'https://youtube.com/playlist?list=PLZqgWWF4O-zg03RGSZ2GpHLE3BmO8bjKo&si=h-uxFsj0V1jt0tKG\n'
        '\n'
        '8. Тестирование Программного Обеспечения в США. Онлайн курс 2018 для начинающих. Канал: Школа Михаила Портнова\n'
        'https://youtube.com/playlist?list=PL_CSTk3_YGZ8i3h8yai0Lp5yrtQ8ga92G&si=VjMDZbrA41KxaZTM\n'
        '\n'
        '9. Открытый курс - Software testing - 2022. Канал: SiliconValleyVoice\n'
        'https://youtube.com/playlist?list=PL7XXjge0nKZfUjvs_puLSXpkV-dBrihZu&si=-kfqf6FPJVKpS9br',
        parse_mode='HTML',
        reply_markup=keyboard_qa_youtube
    )

@dp.message(F.text == 'Книги QA')
async def qa_books(message: Message):
    keyboard_qa_books = ReplyKeyboardMarkup(
        keyboard=[[button_qa_youtube],
                  [button_qa_courses],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Книги по QA:</b>\n'
        '\n'
        '1. «Как тестируют в Google», Арбон Джейсон с Каролло Джеффом и Уиттакером Джеймсом\n'
        'https://www.litres.ru/book/d-uittaker/kak-testiruut-v-google-6701651/\n'
        '\n'
        '2. «Дневник охотника за ошибками», Тобиас Клейн \n'
        'https://www.labirint.ru/books/360829/\n'
        '\n'
        '3. «Непрерывное развертывание ПО», Джез Хамбл, Дэвид Фарли\n'
        'https://www.litres.ru/book/dzhez-hambl/nepreryvnoe-razvertyvanie-po-avtomatizaciya-processov-sborki-t-48613766/\n'
        '\n'
        '4. «Искусство автономного тестирования», Рой Ошероув \n'
        'https://www.labirint.ru/books/427977/\n'
        '\n'
        '5. Сандлер, Майерс, Баджетт: Искусство тестирования програм\n'
        'https://www.labirint.ru/books/764245/\n'
        '\n'
        '6. "Software Testing: Principles and Practices" by Srinivasan Desikan and Gopalaswamy Ramesh\n'
        'https://www.amazon.com/Software-Testing-Principles-Ramesh-Gopalaswamy/dp/817758121X\n'
        '\n'
        '7. Криспин, Грегори: Гибкое тестирование. Практическое руководство для тестировщиков ПО и гибких команд\n'
        'https://www.labirint.ru/books/236986/\n'
        '\n'
        '8. Уиттакер, Арбон, Каролло: Как тестируют в Google\n'
        'https://www.labirint.ru/books/421532/\n'
        '\n'
        '9. "Explore It!: Reduce Risk and Increase Confidence with Exploratory Testing" by Elisabeth Hendrickson\n'
        'https://www.amazon.com/Explore-Increase-Confidence-Exploratory-Testing/dp/1937785025',
        parse_mode='HTML',
        reply_markup=keyboard_qa_books
    )
@dp.message(F.text == 'Что нужно знать QA')
async def qa_what_to_know(message: Message):
    keyboard_qa_info = ReplyKeyboardMarkup(
        keyboard=[[button_qa_main],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Для качественной работы тестировщик должен знать:</b>\n'
        '\n'
        'Понимание теории тестирования (в том числе различные виды, типы и методы управления тестированием);\n'
        '\n'
        'Наличие начальных знаний в одном из популярных языков программирования (Java, Python и т.д.);\n'
        '\n'
        'Начальные знания принципов работы web-приложения;\n'
        '\n'
        'Основы Интернета\n'
        '\n'
        'Архитектура предприятия\n'
        '\n'
        'Основы жизненного цикла разработки программного обеспечения (SDLC)\n'
        '\n'
        'Что такое REST-сервисы, и как они работают;\n'
        '\n'
        'Взаимодействие backend — frontend;\n'
        '\n'
        'Начальные знания SQL;\n'
        '\n'
        'Умение работать с Git.',
        parse_mode='HTML',
        reply_markup=keyboard_qa_info
    )
button_ml_info = KeyboardButton(text = 'Что нужно знать ML')
button_ml_main = KeyboardButton(text = 'Перейти к курсам ML')

@dp.message(F.text == 'Machine Learning')
async def ml_main(message: Message):
    keyboard_ml_main = ReplyKeyboardMarkup(
        keyboard=[[button_ml_info,button_ml_main],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = 'Хотите узнать что нужно изучить или сразу перейдете к курсам?',
        reply_markup=keyboard_ml_main
    )

button_ml_youtube = KeyboardButton(text = 'Видео с Youtube ML')
button_ml_courses = KeyboardButton(text = 'Курсы ML')
button_ml_books = KeyboardButton(text = 'Книги ML')

@dp.message(F.text == 'Перейти к курсам ML')
async def ml_choose_menu(message: Message):
    keyboard_ml_choose = ReplyKeyboardMarkup(
        keyboard= [[button_ml_books,button_ml_courses],
                   [button_ml_youtube],
                   [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = 'Выберите источник информации',
        reply_markup=keyboard_ml_choose
    )

@dp.message(F.text == 'Что нужно знать ML')
async def what_to_know_ml(message: Message):
    keyboard_ml_info = ReplyKeyboardMarkup(
        keyboard=[[button_ml_main],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Ml специалисту нужно знать:</b>\n'
        '\n'
        '<i>Инструменты, используемые для машинного обучения</i>\n'
        '\n'
        '1. Python для высокоуровневого программирования\n'
        '2. Pandas для работы с наборами данных\n'
        '3. Numpy для численных вычислений\n'
        '4. Scikit-learn для ML-моделей (без глубокого обучения)\n'
        '5. TensorFlow или Pytorch для ML-моделей с глубоким обучением\n'
        '6. Высокоуровневые библиотеки глубокого обучения, такие как Keras и fast.ai\n'
        '7. Основы Git для работы над проектом\n'
        '8. Jupyter Notebook или Google Colab для экспериментов с кодом\n'
        '\n'
        '<i>Практические навыки</i>\n'
        '\n'
        '1. Извлечение данных из различных источников (чтение из файлов, API, базы данных)\n'
        '2. Очистка и трансформация данных, их подготовка к анализу\n'
        '3. Умение проводить разведывательный анализ данных\n'
        '4. Визуализация данных с помощью Pandas, Matplotlib\n'
        '5. Feature Engineering: оценка значимости фичей, отбор признаков, методы уменьшения размерности\n'
        '6. Обучение моделей методами классического машинного обучения\n'
        '7. Построение алгоритмов для рекомендательных систем\n'
        '8. Построение ML-моделей для решения задач с помощью временными рядами\n'
        '9. Построение пайплайнов от сбора данных до получения результатов моделирования\n'
        '10. Решение задач моделирования с помощью нейросетевых подходов\n'
        '11. Умение работать с NLP/CV-задачами с помощью стандартных методов и DL',
        parse_mode='HTML',
        reply_markup=keyboard_ml_info
    )

@dp.message(F.text == 'Книги ML')
async def ml_books(message: Message):
    keyboard_ml_books = ReplyKeyboardMarkup(
        keyboard=[[button_ml_courses],
                  [button_ml_youtube],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Книги по Machine Learning:</b>\n'
        '\n'
        '1. «Машинное обучение: алгоритмы для бизнеса». Маркос Лопез де Прадо\n'
        'https://www.litres.ru/book/markos-lopez-de-prado/mashinnoe-obuchenie-algoritmy-dlya-biznesa-50445876/\n'
        '\n'
        '2. «Машинное обучение с использованием библиотеки Н2О». Даррен Кук \n'
        'https://www.labirint.ru/books/609943/\n'
        '\n'
        '3. «Глубокое обучение на R». Франсуа Шолле\n'
        'https://www.litres.ru/book/fransua-sholle-17338303/glubokoe-obuchenie-na-r-pdf-epub-39123343/\n'
        '\n'
        '4. «Построение систем машинного обучения на языке Python». Луис Педро Коэльо,Вилли Ричарт\n'
        'https://www.ozon.ru/product/postroenie-sistem-mashinnogo-obucheniya-na-yazyke-python-koelo-luis-pedro-richart-villi-944138518/\n'
        '\n'
        '5. "Pattern Recognition and Machine Learning" (Распознавание образов и машинное обучение) автора Кристофа Бишопа\n'
        'https://www.labirint.ru/books/755682/\n'
        '\n'
        '6. "Deep Learning" (Глубокое обучение) авторов Иана Гудфеллоу, Йошуа Бенджио и Аарона Курвилля\n'
        'https://www.labirint.ru/books/620686/\n'
        '\n'
        '7. "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow"'
        '(Практическое машинное обучение с использованием Scikit-Learn, Keras и TensorFlow) автора Аурелиена Герона\n'
        'https://www.labirint.ru/books/772921/\n'
        '\n'
        '8. "The Elements of Statistical Learning" (Элементы статистического обучения) авторов Тревора Хасти, Роберта Тибширани и Джерома Фридмана.\n'
        'https://www.labirint.ru/books/755680/',
        parse_mode='HTML',
        reply_markup=keyboard_ml_books
    )
@dp.message(F.text == 'Видео с Youtube ML')
async def ml_youtube(message: Message):
    keyboard_ml_youtube = ReplyKeyboardMarkup(
        keyboard=[[button_ml_books,button_ml_courses],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Видео с Youtube по Machine Learning:</b>\n'
        '\n'
        '1. Машинное обучение (machine learning). Канал: selfedu\n'
        'https://www.youtube.com/playlist?list=PLA0M1Bcd0w8zxDIDOTQHsX68MCDOAJDtj\n'
        '\n'
        '2. Курс «Машинное обучение» 2019. Канал: Компьютерные науки\n'
        'https://www.youtube.com/playlist?list=PLJOzdkh8T5krxc4HsHbB8g8f0hu7973fK\n'
        '\n'
        '3. Machine Learning Course for Beginners. Канал: freeCodeCamp\n'
        'https://www.youtube.com/watch?v=NWONeJKn6kc\n'
        '\n'
        '4. Уроки Python OpenCV / Нейронные сети, машинное обучение. Канал: Гоша Дударь\n'
        'https://www.youtube.com/playlist?list=PL0lO_mIqDDFUAQ2RdAgLp6Tj_fREcxk6T\n'
        '\n'
        '5. Machine Learning Full Course - 12 Hours. Канал: Edureka\n'
        'https://www.youtube.com/watch?v=N5fSpaaxoZc&pp=ygUXTUwg0YEg0L3Rg9C70Y8g0LrRg9GA0YE%3D\n'
        '\n'
        '6. Machine Learning for Everybody – Full Course. Канал: freeCodeCamp\n'
        'https://www.youtube.com/watch?v=i_LwzRVP7bg&pp=ygUXTUwg0YEg0L3Rg9C70Y8g0LrRg9GA0YE%3D\n'
        '\n'
        '7. Курс «Машинное обучение 1» (Евгений Соколов). Канал: ФКН ВШЭ\n'
        'https://youtube.com/playlist?list=PLEqoHzpnmTfChItexxg2ZfxCsm-8QPsdS&si=tc6mBG0PiJ-lGKAh\n'
        '\n'
        '8. Открытый курс OpenDataScience и Mail.ru Group по машинному обучениюю. Канал: Василий Игнатов\n'
        'https://youtube.com/playlist?list=PLZSPcxXPEZVoaCDSEtrrSq2i_ewYqrzZE&si=w-Nm6p5Tv_G_vNWA\n'
        '\n'
        '9. Machine Learning. Курсы программирования. Канал: SkillBox программирование\n'
        'https://youtube.com/playlist?list=PLmEQTfkM_pfmG_xfwWv3-rqqxVJ7DSDt7&si=Wi-jhXtAs8XqKGGQ\n',
        parse_mode='HTML',
        reply_markup=keyboard_ml_youtube
    )

@dp.message(F.text == 'Курсы ML')
async def ml_courses(message: Message):
    keyboard_ml_courses = ReplyKeyboardMarkup(
        keyboard=[[button_ml_books],
                  [button_ml_youtube],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Платные курсы по Machine Learning</b>\n'
        '\n'
        '1. Профессия Machine Learning Engineer от SKillBox\n'
        'https://skillbox.ru/course/profession-machine-learning-service/\n'
        '<a href="https://mooc.ru/courses/professiya-machine-learning-engineer-skillbox">Отзывы</a>\n'
        '\n'
        '2. Машинное обучение от Нетологии\n'
        'https://netology.ru/programs/machine-learn\n'
        '\n'
        '3. Курс по машинному обучению от SkillFactory\n'
        'https://skillfactory.ru/machine-learning\n'
        '\n'
        '4. Курс Machine Learning и Deep Learning от SkillFactory\n'
        'https://skillfactory.ru/machine-learning-i-deep-learning\n'
        '<a href="https://learninghub.ru/machine-learning-i-deep-learning">Отзывы</a>\n'
        '\n'
        '5. Математика и Machine Learning для Data Science от SkillFactory\n'
        'https://skillfactory.ru/matematika-i-machine-learning-dlya-data-science\n'
        '\n'
        '6. MACHINE LEARNING ДЛЯ НАЧИНАЮЩИХ от karpov courses\n'
        'https://karpov.courses/ml-start\n'
        '<a href="https://karpov.courses/casesstartml">Отзывы</a>\n'
        '\n'
        '7. Deep Learning от Нетологии\n'
        'https://netology.ru/programs/deep-learning\n'
        '<a href="https://irecommend.ru/content/kurs-deep-learning-neplokho-ne-dlya-nachinayushchikh">Отзывы</a>\n'
        '\n'
        '<b>Бесплатные курсы:</b>\n'
        '\n'
        '1. Ускоренный курс по машинному обучению от Google\n'
        'https://developers.google.com/machine-learning/crash-course?hl=ru\n'
        '\n'
        '2. The Top 5 Machine Learning Libraries in Python от Udemy\n'
        'https://www.udemy.com/course/the-top-5-machine-learning-libraries-in-python/\n'
        '\n'
        '3. Машинное обучение от Stepik\n'
        'https://stepik.org/course/8057/promo\n'
        '\n'
        '4. Supervised Machine Learning: Regression and Classification от Coursera\n'
        'https://www.coursera.org/learn/machine-learning\n'
        '\n'
        '5. Machine Learning Foundations: A Case Study Approach от Coursera\n'
        'https://www.coursera.org/learn/ml-foundations',
        parse_mode='HTML',
        reply_markup=keyboard_ml_courses
    )
button_gamedev_info = KeyboardButton(text = 'Что нужно знать GameDev')
button_gamedev_main = KeyboardButton(text = 'Перейти к курсам GameDev')

@dp.message(F.text == 'GameDev')
async def gamedev_main(message: Message):
    keyboard_gamedev_main = ReplyKeyboardMarkup(
        keyboard=[[button_gamedev_info,button_gamedev_main],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = 'Хотите узнать что нужно изучить или сразу перейдете к курсам?',
        reply_markup=keyboard_gamedev_main
    )

button_gamedev_youtube = KeyboardButton(text = 'Видео с Youtube GameDev')
button_gamedev_courses = KeyboardButton(text = 'Курсы GameDev')
button_gamedev_books = KeyboardButton(text = 'Книги GameDev')

@dp.message(F.text == 'Перейти к курсам GameDev')
async def gamedev_choose_menu(message: Message):
    keyboard_gamedev_choose = ReplyKeyboardMarkup(
        keyboard= [[button_gamedev_books,button_gamedev_courses],
                   [button_gamedev_youtube],
                   [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = 'Выберите источник информации',
        reply_markup=keyboard_gamedev_choose
    )

@dp.message(F.text == 'Что нужно знать GameDev')
async def what_to_know_gamedev(message: Message):
    keyboard_gamedev_info = ReplyKeyboardMarkup(
        keyboard=[[button_gamedev_main],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Hard Skills GameDeveloper:</b>\n'
        '\n'
        '1. Знание нескольких языков программирования. Основные - C++, C#\n'
        '2. Хорошая математическая база — высшая математика, линейная алгебра и статистика.\n'
        '3. Опыт работы в Unreal Engine и Unity\n'
        '4. Понимание классических алгоритмов и структур данных\n'
        '5. Английский язык\n'
        '6. Умение пользоваться системами контроля версий — системы типа Git или SVN\n',
        parse_mode='HTML',
        reply_markup=keyboard_gamedev_info
    )

@dp.message(F.text == 'Книги GameDev')
async def gamedev_books(message: Message):
    keyboard_gamedev_books = ReplyKeyboardMarkup(
        keyboard=[[button_gamedev_courses],
                  [button_gamedev_youtube],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Книги по GameDevelopment</b>\n'
        '\n'
        '1. "The Art of Game Design: A Book of Lenses" by Jesse Schell\n'
        'https://www.amazon.com/Art-Game-Design-Book-Lenses/dp/0123694965\n'
        '\n'
        '2. Роберт Нистрем: Паттерны программирования игр\n'
        'https://www.labirint.ru/books/818401/\n'
        '\n'
        '3. Джейсон Грегори: Игровой движок. Программирование и внутреннее устройство\n'
        'https://www.labirint.ru/books/777006/\n'
        '\n'
        '4. Джозеф Хокинг: Unity в действии. Мультиплатформенная разработка на C#\n'
        'https://www.labirint.ru/books/667926/',
        parse_mode='HTML',
        reply_markup=keyboard_gamedev_books
    )
@dp.message(F.text == 'Видео с Youtube GameDev')
async def gamedev_youtube(message: Message):
    keyboard_gamedev_youtube = ReplyKeyboardMarkup(
        keyboard=[[button_gamedev_books,button_gamedev_courses],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Видео с Youtube по GameDevelopment</b>\n'
        '\n'
        '1. Уроки Unity для начинающих / Изучение движка Unity с нуля. Канал: школа itProger\n'
        'https://youtube.com/playlist?list=PLDyJYA6aTY1k_-3fFiMVoYY04jCr-QY55&si=FMp-OHgm3Xnz8R62\n'
        '\n'
        '2. GameDev курс. Канал: Владимир Труков\n'
        'https://youtube.com/playlist?list=PL2Li-NpFLOMS7uHh9oC0FUdNivY3UxjHc&si=O-k0sdfY2khE1FX-\n'
        '\n'
        '3. Unreal Engine 5 C++ Developer: Learn C++ & Make Video Games. Канал: VlaKu\n'
        'https://youtube.com/playlist?list=PLimG-ArmL2Pz_hAu7BM3VXRxxT0G26Wop&si=GvrKhC9LrriGGAAr\n'
        '\n'
        '4. Уроки Pygame для начинающих / Разработка игр на Python с нуля. Канал: школа itProger\n'
        'https://youtube.com/playlist?list=PLDyJYA6aTY1mLtXrGH55paZHFjpqHdDol&si=Jm5xSteWlHpvUckF',
        parse_mode='HTML',
        reply_markup=keyboard_gamedev_youtube
    )

@dp.message(F.text == 'Курсы GameDev')
async def gamedev_courses(message: Message):
    keyboard_gamedev_courses = ReplyKeyboardMarkup(
        keyboard=[[button_gamedev_books],
                  [button_gamedev_youtube],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Платные курсы по GameDev</b>\n'
        '\n'
        '1. Профессия Разработчик игр на Unreal Engine с нуля до Middle от SkillBox\n'
        'https://skillbox.ru/course/profession-ue4/\n'
        '<a href="https://otzovik.com/review_12688065.html">Отзывы</a>\n'
        '\n'
        '2. Курс «Разработчик игр на Unreal Engine» от GeekBrains\n'
        'https://gb.ru/geek_university/developer/programmer/unrealengine\n'
        '<a href="https://www.sravni.ru/shkola/geekbrains/otzyvy/575134/">Отзывы</a>\n'
        '\n'
        '3. Разработчик игр на Unity от SkillFactory\n'
        'https://skillfactory.ru/game-developer-pro\n'
        '<a href="https://eduverse.ru/skillfactory/professiya-razrabotcik-igr-na-unity-2">Отзывы</a>\n'
        '\n'
        '<b>Бесплатные курсы по GameDev</b>\n'
        '\n'
        '1. Создание игр на Unity от Udemy\n'
        'https://www.udemy.com/course/unity-mm/\n'
        '\n'
        '2. Создание  игр с нуля от XYZ school\n'
        'https://free.school-xyz.com/\n'
        '\n'
        '3. Unreal Engine 4 от SkillBox\n'
        'https://clck.ru/36kKyt\n'
        '\n'
        '4. Your First Hour in Unreal Engine 5.0 от EpicGames\n'
        'https://clck.ru/36kLMg',
        parse_mode='HTML',
        reply_markup=keyboard_gamedev_courses
    )

button_system_engineer_info = KeyboardButton(text = 'Что нужно знать System Engineering')
button_system_engineer_main = KeyboardButton(text = 'Перейти к курсам System Engineering')

@dp.message(F.text == 'System Engineering')
async def system_engineer_main(message: Message):
    keyboard_system_engineer_main = ReplyKeyboardMarkup(
        keyboard=[[button_system_engineer_info,button_system_engineer_main],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = 'Хотите узнать что нужно изучить или сразу перейдете к курсам?',
        reply_markup=keyboard_system_engineer_main
    )

button_system_engineer_youtube = KeyboardButton(text = 'Видео с Youtube System Engineering')
button_system_engineer_courses = KeyboardButton(text = 'Курсы System Engineering')
button_system_engineer_books = KeyboardButton(text = 'Книги System Engineering')

@dp.message(F.text == 'Перейти к курсам System Engineering')
async def system_engineer_choose_menu(message: Message):
    keyboard_system_engineer_choose = ReplyKeyboardMarkup(
        keyboard = [[button_system_engineer_books,button_system_engineer_courses],
                   [button_system_engineer_youtube],
                   [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = 'Выберите источник информации',
        reply_markup=keyboard_system_engineer_choose
    )

@dp.message(F.text == 'Что нужно знать System Engineering')
async def what_to_know_system_engineer(message: Message):
    keyboard_system_engineer_info = ReplyKeyboardMarkup(
        keyboard = [[button_system_engineer_main],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Навыки, знания и задачи System Engineer:</b>\n'
        '\n'
        '1. Знание TCP/IP\n'
        '2. Умение работать с веб-серверами (Apache, Ngninx, IIS)\n'
        '3. Понимание модели OSI\n'
        '4. Знание операционных систем Unix/Linux, Windows\n'
        '5. Навык и опыт работы управления, администрирование баз данных MySQL и MySql Workbench, Oracle и знание их синтаксиса\n'
        '6. Знание систем контроля и отслеживания: Cacti, Munin, Nagios, Zabbix\n'
        '7. Навык проводить диагностику и анализ проблемных мест\n'
        '8. Умение распознать следствие/причины некорректной работы ПО или техники.\n'
        '9. Анализ сетевого трафика\n'
        '10. Анализ защищенности сетевой инфраструктуры\n'
        '11. Владение инструментарием для тестирования безопасности сети Burp Suite, Metasploit, Nmap и др\n'
        '12. Знание почтовых и файловые служб основных ОС\n'
        '13. Работы с локальной документацией и отчетами о проделанной работе',
        parse_mode='HTML',
        reply_markup=keyboard_system_engineer_info
    )

@dp.message(F.text == 'Книги System Engineering')
async def system_engineer_books(message: Message):
    keyboard_system_engineer_books = ReplyKeyboardMarkup(
        keyboard = [[button_system_engineer_courses],
                  [button_system_engineer_youtube],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Книги по System Engineering</b>\n'
        '\n'
        '1. "Systems Engineering: Principles and Practice" (Системная инженерия: принципы и практика)\n'
        'авторов Александера Коскинаса и Уильяма Нейла.\n'
        'https://www.labirint.ru/books/435405/\n'
        '\n'
        '2. "Requirements Engineering: From System Goals to UML Models to Software\n'
        'Specifications" (Инженерия требований: от целей системы до UML-моделей и\n'
        'спецификаций программного обеспечения) автора Акселя ван Ламсвеерта\n'
        'https://www.amazon.com/Requirements-Engineering-System-Software-Specifications/dp/0470012706\n'
        '\n'
        '3. «Цифровая схемотехника и архитектура компьютера», Дэвид М. Харрис, Сара Л. Харрис\n'
        'https://is.ifmo.ru/books/2016/digital-design-and-computer-architecture-russian-translation_July16_2016.pdf\n'
        '\n'
        '4. «Unix и Linux. Руководство системного администратора», Эви Немет, Гарт Снайдер, Трент Р. Хейн, Бэн Уэйли\n'
        'https://doc.lagout.org/operating%20system%20/linux/Nemet.pdf\n'
        '\n'
        '5. «Системное и сетевое администрирование.\n'
        'Практическое руководство, 2-е издание», Томас А. Лимончелли, Кристина Хоган, Страта Чейлап\n'
        'https://clck.ru/36kJ2B\n'
        '\n'
        '6. «Linux. Необходимый код и команды. Карманный справочник», Скотт Граннеман\n'
        'https://www.labirint.ru/books/850120/\n'
        '\n'
        '7. «Python в системном администрировании UNIX и Linux», Ноа Гифт, Джереми М. Джонс\n'
        'https://www.litres.ru/book/m-dzhons-dzheremi/python-v-sistemnom-administrirovanii-unix-i-linux-24499422/\n'
        '\n'
        '8. «Linux from scratch», Герард Бикманс\n'
        'https://www.litres.ru/serii-knig/linux-from-scratch/',
        parse_mode='HTML',
        reply_markup=keyboard_system_engineer_books
    )
@dp.message(F.text == 'Видео с Youtube System Engineering')
async def system_engineer_youtube(message: Message):
    keyboard_system_engineer_youtube = ReplyKeyboardMarkup(
        keyboard = [[button_system_engineer_books,button_system_engineer_courses],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Видео с Youtube по System Engineering</b>\n'
        '\n'
        '1. Linux с нуля до DevNet инженера 2022. Канал: Cisco Ne Slabo / SEDICOMM TV\n'
        'https://youtube.com/playlist?list=PLMiVLClzZDbRv6BiFpkndO41DcTn0ILQE&si=hexuebLSTaJ0XEGj\n'
        '\n'
        '2. Курс Системного Администратора Linux для новичков. Канал: Linux Engineer\n'
        'https://youtube.com/playlist?list=PLMuaQLfeOXUwWMMnpNTcBGvJ5XDHLO5Pf&si=eTFnW4bUxsrcydGX\n'
        '\n'
        '3. The Linux Basics Course: Beginner to Sysadmin, Step by Step. Канал: tutorialLinux\n'
        'https://youtube.com/playlist?list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&si=a3YsboQNks-FxC89\n'
        '\n'
        '4. System engineering lectures. Канал: EduGrown\n'
        'https://youtube.com/playlist?list=PLelAq9xzEDXC5ikiGLE3CklnK5_VRW_bf&si=21Mkf9THPomlHEd6',
        parse_mode='HTML',
        reply_markup=keyboard_system_engineer_youtube
    )

@dp.message(F.text == 'Курсы System Engineering')
async def system_engineer_courses(message: Message):
    keyboard_system_engineer_courses = ReplyKeyboardMarkup(
        keyboard = [[button_system_engineer_books],
                  [button_system_engineer_youtube],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Платные курсы по System Engineering</b>\n'
        '\n'
        '1. Инженер Linux систем от Специалист\n'
        'https://www.specialist.ru/track/t-linuxdp\n'
        '<a href="https://kurshub.ru/reviews/specialist-ru/">Отзывы</a>'
        '\n'
        '2. Специалист систем мониторинга IT - инфраструктуры от Специалист\n'
        'https://www.specialist.ru/track/t-linmon\n'
        '\n'
        '3. Основы сетей, сетевые операционные системы и практикум Wi - Fi от Специалист\n'
        'https://www.specialist.ru/course/seti1-a\n'
        '\n'
        '4. Системный администратор от Нетологии\n'
        'https://clck.ru/36nKC6\n'
        '<a href="https://pgdv.ru/blog/netology-sistemnyi-administrator">Отзывы</a>\n'
        '\n'
        '5. Системный администратор от GeekBrains\n'
        'https://clck.ru/36nKFf\n'
        '<a href="https://www.sravni.ru/shkola/geekbrains/otzyvy/607348/">Отзывы</a>\n'
        '\n'
        '<b>Бесплатные курсы</b>\n'
        '\n'
        '1. Администрирование информационных систем от Stepik\n'
        'https://stepik.org/course/49857/promo\n'
        '\n'
        '2. Введение в сетевые технологии от Stepik\n'
        'https://stepik.org/course/58678/promo\n'
        '\n'
        '3. Введение в теорию защиты информации от Stepik\n'
        'https://stepik.org/course/56318/promo\n'
        '\n'
        '4. Анализ безопасности веб-проектов от Stepik\n'
        'https://stepik.org/course/127/promo\n',
        parse_mode='HTML',
        reply_markup=keyboard_system_engineer_courses
    )

button_backend_java = KeyboardButton(text = 'Java - разработка')
button_backend_python = KeyboardButton(text = 'Python - разработка')
button_backend_c = KeyboardButton(text = 'C/C++ разработка')

@dp.message(F.text == 'Backend')
async def backend_main(message: Message):
    keyboard_backend_main = ReplyKeyboardMarkup(
        keyboard = [[button_backend_java],
                  [button_backend_python],
                  [button_backend_c],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = 'Выберите предпочтительный язык разработки',
        reply_markup=keyboard_backend_main
    )

button_java_info = KeyboardButton(text = 'Что нужно знать Java - разработка')
button_java_main = KeyboardButton(text = 'Перейти к курсам Java - разработка')

@dp.message(F.text == 'Java - разработка')
async def java_main(message: Message):
    keyboard_java_main = ReplyKeyboardMarkup(
        keyboard = [[button_java_main],
                  [button_java_info],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = 'Хотите узнать что нужно изучить или сразу перейдете к курсам?',
        reply_markup= keyboard_java_main
    )

@dp.message(F.text == 'Что нужно знать Java - разработка')
async def java_info(message: Message):
    keyboard_java_info = ReplyKeyboardMarkup(
        keyboard = [[button_java_main],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Java разработчику необходимо знать:</b>\n'
        '\n'
        '<i>Базовые алгоритмы</i>\n'
        '<i>Java Syntax</i>\n'
        '<i>Паттерны программирования</i>\n'
        '<i>Парадигмы программирования. Чистота кода</i>\n'
        '<i>SQL</i>\n'
        '<i>MySQL/PostgreSQL</i>\n'
        '<i>Maven/Gradle</i>\n'
        '<i>Git</i>\n'
        '<i>JDBC</i>\n'
        '<i>JPA. Hibernate</i>\n'
        '<i>Spring</i>\n'
        '<i>Spring Core</i>\n'
        '<i>Spring JDBC</i>\n'
        '<i>Spring Hibernate</i>\n'
        '<i>Spring JPA</i>\n'
        '<i>Spring MVC</i>\n'
        '<i>Spring Boot</i>\n',
        parse_mode='HTML',
        reply_markup=keyboard_java_info
    )

button_java_courses = KeyboardButton(text = 'Курсы Java - разработка')
button_java_books = KeyboardButton(text = 'Книги Java - разработка')
button_java_youtube = KeyboardButton(text = 'Видео с Youtube Java - разработка')

@dp.message(F.text == 'Перейти к курсам Java - разработка')
async def java_choose_menu(message: Message):
    keyboard_java_choose = ReplyKeyboardMarkup(
        keyboard = [[button_java_courses,button_java_books],
                  [button_java_youtube],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = 'Выберите источник информации',
        reply_markup = keyboard_java_choose
    )

@dp.message(F.text == 'Книги Java - разработка')
async def java_books(message: Message):
    keyboard_java_books = ReplyKeyboardMarkup(
        keyboard = [[button_java_courses],
                  [button_java_youtube],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Книги по Java:</b>\n'
        '\n'
        '1. Лауренциу Спилкэ: Java. устранение проблем. Чтение, отладка и оптимизация JVM-приложений\n'
        'https://www.labirint.ru/books/979032/\n'
        '\n'
        '2. Барри Берд: Java для чайников\n'
        'https://www.labirint.ru/books/633539\n'
        '\n'
        '3. Джошуа Блох: Java. Эффективное программирование\n'
        'https://www.labirint.ru/books/674797/\n'
        '\n'
        '4. Кей Хорстманн: Java. Библиотека профессионала. Том 1. Основы\n'
        'https://www.labirint.ru/books/695676/',
        parse_mode='HTML',
        reply_markup=keyboard_java_books
    )
@dp.message(F.text == 'Видео с Youtube Java - разработка')
async def java_youtube(message: Message):
    keyboard_java_youtube = ReplyKeyboardMarkup(
        keyboard = [[button_java_books,button_java_courses],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Видео с Youtube по Java</b>\n'
        '\n'
        '1. Backend на Java: большой курс для входа в профессию. Канал: Mad Brains\n'
        'https://www.youtube.com/playlist?list=PLw6SJ6q6-1YptavAy65knVOSBZ_y6YxmV\n'
        '\n'
        '2. Java Tutorial - Complete User Login and Registration Backend + Email Verification. Канал: AmigosCode\n'
        'https://www.youtube.com/watch?v=QwQuro7ekvc&ab_channel=Amigoscode\n'
        '\n'
        '3. Java Programming for Beginners – Full Course. Канал: FreeCodeCamp\n'
        'https://www.youtube.com/watch?v=A74TOX803D0&ab_channel=freeCodeCamp.or\n'
        '\n'
        '4. JBoss Tutorial | Explore JBoss In Less Than An Hour. Канал: MindMajix\n'
        'https://www.youtube.com/watch?v=HgqcT3j7_x0&pp=ygUFSkJvc3M%3D',
        parse_mode='HTML',
        reply_markup=keyboard_java_youtube
    )

@dp.message(F.text == 'Курсы Java - разработка')
async def java_courses(message: Message):
    keyboard_java_courses = ReplyKeyboardMarkup(
        keyboard = [[button_java_books],
                  [button_java_youtube],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Платные курсы по Java</b>\n'
        '\n'
        '1. Курс «Backend-разработка на Java с нуля» от SkyPro\n'
        'https://sky.pro/courses/programming/java-backend\n'
        '\n'
        '2. Профессия Java-разработчик от SkillBox\n'
        'https://skillbox.ru/course/profession-java/\n'
        '<a href="https://www.sravni.ru/shkola/skillbox/otzyvy/584558/">Отзывы</a>\n'
        '\n'
        '3. Курс «Java-разработчик» от Яндекс Практикума\n'
        'https://practicum.yandex.ru/java-developer/\n'
        '<a href="https://otzovik.com/reviews/yandeks_praktikum-kurs_java-razrabotchik/">Отзывы</a>\n'
        '\n'
        '4. Курсы Java для начинающих от JavaRush\n'
        'https://javarush.com/\n'
        '<a href="https://otzovik.com/reviews/javarush_ru-onlayn-kurs_obucheniya_programmirovaniyu_na_java/">Отзывы</a>\n'
        '\n'
        '5. «Java-разработчик» от Хекслет\n'
        'https://ru.hexlet.io/programs/java\n'
        '<a href="https://education.pikabu.ru/courses-dev/hekslet/professiya-java-razrabotchik#reviews">Отзывы</a>\n'
        '\n'
        '<b>Бесплатные курсы</b>\n'
        '\n'
        '1. Java. Базовый курс от Stepik\n'
        'https://stepik.org/course/187/promo\n'
        '\n'
        '2. Практический мини-курс по Java: 3 программы с нуля от Skillbox\n'
        'https://clck.ru/36nL4u\n'
        '\n'
        '3. Консольные приложения на Java от GeekBrains\n'
        'https://gb.ru/courses/398\n'
        '\n'
        '4. Java-разработка от SkillBox\n'
        'https://live.skillbox.ru/playlists/code/java-razrabotka/\n'
        '\n'
        '5. Основы Java от Хекслет\n'
        'https://ru.hexlet.io/courses/java-basics\n'
        '\n'
        '6. Java: Многопоточность от Хекслет\n'
        'https://ru.hexlet.io/courses/concurrency\n'
        '\n'
        '7. Основы Java от Stepik\n'
        'https://stepik.org/course/82867/promo\n',
        parse_mode='HTML',
        reply_markup=keyboard_java_courses
    )

button_python_info = KeyboardButton(text = 'Что нужно знать Python - разработка')
button_python_main = KeyboardButton(text = 'Перейти к курсам Python - разработка')

@dp.message(F.text == 'Python - разработка')
async def python_main(message: Message):
    keyboard_python_main = ReplyKeyboardMarkup(
        keyboard = [[button_python_main],
                  [button_python_info],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = 'Хотите узнать что нужно изучить или сразу перейдете к курсам?',
        reply_markup= keyboard_python_main
    )

@dp.message(F.text == 'Что нужно знать Python - разработка')
async def python_info(message: Message):
    keyboard_python_info = ReplyKeyboardMarkup(
        keyboard = [[button_python_main],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Python разработчику необходимо знать</b>\n'
        '\n'
        '1. Синтаксис языка Python\n'
        '2. Английский язык\n'
        '3. Git & GitHub\n'
        '4. Алгоритмы и структуры данных\n'
        '5. Методологии разработки Agile/Scrum\n'
        '6. Веб-сервера (Nginx, Apache)\n'
        '7. Базы данных (MySQL, MongoDB)\n'
        '8. Фреймворки Flask/Django\n'
        '9. Паттерн MVC (Model-View-Controller)\n'
        '10. Вспомогательные технологии (Celery, RabbitMQ)\n'
        '11. Общие принципы работы интернета. API, протоколы (http, https), JSON-RPC, Protocol Buffers, gRPC.\n'
        '12. Linux, а также одна или несколько IDE',
        parse_mode='HTML',
        reply_markup=keyboard_python_info
    )

button_python_courses = KeyboardButton(text = 'Курсы Python - разработка')
button_python_books = KeyboardButton(text = 'Книги Python - разработка')
button_python_youtube = KeyboardButton(text = 'Видео с Youtube Python - разработка')

@dp.message(F.text == 'Перейти к курсам Python - разработка')
async def python_choose_menu(message: Message):
    keyboard_python_choose = ReplyKeyboardMarkup(
        keyboard = [[button_python_courses,button_python_books],
                  [button_python_youtube],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = 'Выберите источник информации',
        reply_markup = keyboard_python_choose
    )

@dp.message(F.text == 'Книги Python - разработка')
async def python_books(message: Message):
    keyboard_python_books = ReplyKeyboardMarkup(
        keyboard = [[button_python_courses],
                  [button_python_youtube],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Книги по Python:</b>\n'
        '\n'
        '1. Django. Разработка веб-приложений на Python — Джефф Форсье, Пол Биссекс, Уэсли Дж. Чан\n'
        'https://www.litres.ru/book/dzheff-forse/django-razrabotka-veb-prilozheniy-na-python-24499478/otzivi/\n'
        '\n'
        '2. Django: практика создания Web-сайтов на Python — Владимир Дронов\n'
        'https://www.litres.ru/book/vladimir-dronov/django-praktika-sozdaniya-web-saytov-na-python-19213409/\n'
        '\n'
        '3. Мигель Гринберг: Разработка веб-приложений с использованием Flask на языке Python\n'
        'https://www.labirint.ru/books/446705/\n'
        '\n'
        '4. Марк Лутц «Изучаем Python»\n'
        'https://www.ozon.ru/category/mark-lutts-izuchaem-python/\n'
        '\n'
        '5. Эрик Мэтиз «Изучаем Python. Программирование игр, визуализация данных, веб-приложения»\n'
        'https://clck.ru/36kJXb\n'
        '\n'
        '6. Бизли и Джонс «Python. Книга рецептов»\n'
        'https://yurecnt.ru/files/books/43hhsdjgo0mud4djzg2zveo1pnzc1o.pdf\n'
        '\n'
        '7. Эл Свейгарт «Автоматизация рутинных задач с помощью Python. Практическое руководство для начинающих»\n'
        'https://www.labirint.ru/books/824407/',
        parse_mode='HTML',
        reply_markup = keyboard_python_books
    )
@dp.message(F.text == 'Видео с Youtube Python - разработка')
async def python_youtube(message: Message):
    keyboard_python_youtube = ReplyKeyboardMarkup(
        keyboard = [[button_python_books,button_python_courses],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Видео с Youtube по Python</b>\n'
        '\n'
        '1. [Yandex лекторий] Python backend. Канал: Grigoriy Romanenkov\n'
        'https://www.youtube.com/playlist?list=PLoaXavbYQKPPN9wruJe2pLPuEKjXWvaM1\n'
        '\n'
        '2. Python Backend Web Development Course (with Django). Канал: FreeCodeCamp\n'
        'https://www.youtube.com/watch?v=jBzwzrDvZ18&ab_channel=freeCodeCamp.org\n'
        '\n'
        '3. Мастер-класс: "Backend на Python". Канал: ИИКС НИЯУ МИФИ\n'
        'https://www.youtube.com/watch?v=LcZ9uJn8ffA&ab_channel=%D0%98%D0%98%\n'
        '\n'
        '4. Уроки изучения Django / Создание сайта на Джанго. Канал: школа itProger\n'
        'https://www.youtube.com/playlist?list=PLDyJYA6aTY1nZ9fSGcsK4wqeu-xaJksQQ\n'
        '\n'
        '5. Изучение Flask для начинающих / Создание сайта на Python. Канал: Гоша Дударь\n'
        'https://www.youtube.com/playlist?list=PL0lO_mIqDDFXiIQYjLbncE9Lb6sx8elKA',
        parse_mode='HTML',
        reply_markup=keyboard_python_youtube
    )

@dp.message(F.text == 'Курсы Python - разработка')
async def python_courses(message: Message):
    keyboard_python_courses = ReplyKeyboardMarkup(
        keyboard = [[button_python_books],
                  [button_python_youtube],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Платные курсы по Python</b>\n'
        '\n'
        '1. Бэкэнд-разработчик на Python от SF Education\n'
        'https://sf.education/bkpython\n'
        '\n'
        '2. Бэкенд - разработчик на Python от Специалист\n'
        'https://www.specialist.ru/track/dp-pythonmax\n'
        '\n'
        '3. Курс «Python-разработчик» от Яндекс Практикума\n'
        'https://practicum.yandex.ru/backend-developer/\n'
        '<a href="https://otzovik.com/reviews/yandeks_praktikum-kurs_python-razrabotchik/">Отзывы</a>\n'
        '\n'
        '<b>Бесплатные курсы по Python</b>\n'
        '\n'
        '1. Программирование на Python от Stepik\n'
        'https://stepik.org/course/67/promo\n'
        '\n'
        '2. Добрый, добрый Python - обучающий курс от Сергея Балакирева на Stepik\n'
        'https://stepik.org/course/100707/promo?search=783470253\n'
        '\n'
        '3. Основы Python: создаём телеграм-бота от Нетологии\n'
        'https://netology.ru/programs/pyfree-async\n'
        '\n'
        '4. Основы Python от Хекслет\n'
        'https://clck.ru/36nLv5\n'
        '\n'
        '5. Python для всех: практический мини-курс для новичков от Skillbox\n'
        'https://clck.ru/36nM2S\n'
        '\n'
        '6. «Основы Python-разработки» от Яндекс Практикума\n'
        'https://practicum.yandex.ru/python-free/',
        parse_mode='HTML',
        reply_markup=keyboard_python_courses
    )

button_c_info = KeyboardButton(text = 'Что нужно знать C/C++ разработка')
button_c_main = KeyboardButton(text = 'Перейти к курсам C/C++ разработка')

@dp.message(F.text == 'C/C++ разработка')
async def c_main(message: Message):
    keyboard_c_main = ReplyKeyboardMarkup(
        keyboard = [[button_c_main],
                  [button_c_info],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = 'Хотите узнать что нужно изучить или сразу перейдете к курсам?',
        reply_markup= keyboard_c_main
    )

@dp.message(F.text == 'Что нужно знать C/C++ разработка')
async def c_info(message: Message):
    keyboard_c_info = ReplyKeyboardMarkup(
        keyboard = [[button_c_main],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>C/C++ разработчику необходимо знать</b>\n'
        '\n'
        '1. Знание C++ и его стандартов.(C++11, C++14, C++17, C++20)\n'
        '2. Понимание алгоритмов и структур данных\n'
        '3. Умение оптимизировать код для увеличения производительности и эффективности приложения\n'
        '4. Управление памятью. Использование указателей, сборку мусора и RAII\n'
        '5. Работа с многозадачностью и потоками в C++ \n'
        '6. Знание библиотек и фреймворков: Qt, Boost и STL\n',
        parse_mode='HTML',
        reply_markup=keyboard_c_info
    )

button_c_courses = KeyboardButton(text = 'Курсы C/C++ разработка')
button_c_books = KeyboardButton(text = 'Книги C/C++ разработка')
button_c_youtube = KeyboardButton(text = 'Видео с Youtube C/C++ разработка')

@dp.message(F.text == 'Перейти к курсам C/C++ разработка')
async def c_choose_menu(message: Message):
    keyboard_c_choose = ReplyKeyboardMarkup(
        keyboard = [[button_c_courses,button_c_books],
                  [button_c_youtube],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = 'Выберите источник информации',
        reply_markup = keyboard_c_choose
    )

@dp.message(F.text == 'Книги C/C++ разработка')
async def c_books(message: Message):
    keyboard_c_books = ReplyKeyboardMarkup(
        keyboard = [[button_c_courses],
                  [button_c_youtube],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Книги по C/C++:</b>\n'
        '\n'
        '1. Qt 5.10. Профессиональное программирование на C++. Макс Шлее\n'
        'https://www.ozon.ru/product/qt-5-10-professionalnoe-programmirovanie-na-c-shlee-maks-elektronnaya-kniga-1105001443/\n'
        '\n'
        '2. Beginning C++20\n'
        'https://www.labirint.ru/books/925628/\n'
        '\n'
        '3. Стивен Прата: Язык программирования C++. Лекции и упражнения\n'
        'https://www.labirint.ru/books/512980/\n'
        '\n'
        '4. Лакос, Хлебников, Мередит: Современный С++. Безопасное использование \n'
        'https://www.labirint.ru/books/955812/\n'
        '\n'
        '5. Антон Полухин: Разработка приложений на С++ с использованием Boost\n'
        'https://www.labirint.ru/books/761225/',
        parse_mode='HTML',
        reply_markup = keyboard_c_books
    )
@dp.message(F.text == 'Видео с Youtube C/C++ разработка')
async def c_youtube(message: Message):
    keyboard_c_youtube = ReplyKeyboardMarkup(
        keyboard = [[button_c_books,button_c_courses],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Видео с Youtube по C/C++</b>\n'
        '\n'
        '1. C++ Programming Course - Beginner to Advanced. Канал: FreeCodeCamp\n'
        'https://www.youtube.com/watch?v=8jLOx1hD3_o&pp=ygUMYysrIGJhY2tlbmQg\n'
        '\n'
        '2. C++ FULL COURSE For Beginners (Learn C++ in 10 hours). Канал: CodeBeaty\n'
        'https://www.youtube.com/watch?v=GQp1zzTwrIg&ab_channel=CodeBeauty\n'
        '\n'
        '3. Уроки Qt Creator | Графический интерфейс на С++. Канал: Гоша Дударь\n'
        'https://www.youtube.com/playlist?list=PL0lO_mIqDDFUaZe7H9kY6vWbSVrtwFv4M\n'
        '\n'
        '4. Boost C++ Сборка, Настройка и Использование. Канал: AmbushedRaccoon\n'
        'https://www.youtube.com/watch?v=PP0RCyNc_68&pp=ygUJQm9vc3QgYysr\n'
        '\n'
        '5. Writing a Network Client with POCO. Канал: Utah Cpp Progremmers\n'
        'https://www.youtube.com/watch?v=rRR9RTUEn4k&ab_channel=UtahCppProgram',
        parse_mode='HTML',
        reply_markup=keyboard_c_youtube
    )

@dp.message(F.text == 'Курсы C/C++ разработка')
async def c_courses(message: Message):
    keyboard_c_courses = ReplyKeyboardMarkup(
        keyboard = [[button_c_books],
                  [button_c_youtube],
                  [button_main_menu]],
        resize_keyboard=True
    )
    await message.answer(
        text = '<b>Платные курсы по C/C++</b>\n'
        '\n'
        '1. Курс «C++ для бэкенда» от Яндекс Практикума\n'
        'https://practicum.yandex.ru/cpp-backend/\n'
        '\n'
        '2. Курс «Разработчик C++» от Яндекс Практикума\n'
        'https://practicum.yandex.ru/cpp/\n'
        '<a href="https://otzovik.com/reviews/yandeks_praktikum-kurs_razrabotchik_c_plus/">Отзывы</a>\n'
        '\n'
        '3. C++ разработчик от SkillFactory\n'
        'https://skillfactory.ru/c-plus-plus-razrabotchik\n'
        '\n'
        '4. Разработчик на C++ от Нетологии\n'
        'https://clck.ru/36mTcg\n'
        '<a href="https://pgdv.ru/blog/netology-cpp-developer">Отзывы</a>\n'
        '\n'
        '<b>Бесплатные курсы</b>\n'
        '\n'
        '1. Программирование на языке C++ от Stepik\n'
        'https://stepik.org/course/7/promo\n'
        '\n'
        '2. Основы С++ от Яндекс Образования\n'
        'https://education.yandex.ru/handbook/cpp\n'
        '\n'
        '3. Курс C++: онлайн обучение с нуля от CodeBasics\n'
        'https://code-basics.com/ru/languages/cpp?ysclid=lpe4x8x5h2208167518\n'
        '\n'
        '4. Основы С++ и основы UE4 от Udemy\n'
        'https://www.udemy.com/course/fundamental-coding/\n',
        parse_mode='HTML',
        reply_markup=keyboard_c_courses
    )
if __name__ == '__main__':
    dp.run_polling(bot)
