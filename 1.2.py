# by LatsPlayNoOne
# https://github.com/LatsPlayNoOne/YoutuberSimulator
# https://www.youtube.com/@privet_kire/featured

import random
from os import system
import json
from time import sleep

views = 0
money = 0
subscribers = 0
boost = 1
likes = 0
dislikes = 0
monetization = False
busyness = 0
day = 0
popularity = 1
complete = False
week = "воскресенье"


def new_day():
    global busyness, day, week, freenees
    system("cls")
    busyness = random.randint(0, 2); day += 1
    if week == "понедельник":freenees = random.randint(4,6) - busyness; week = "вторник"
    elif week == "вторник": freenees = random.randint(4,6) - busyness; week = "среда"
    elif week == "среда": freenees = random.randint(4,6) - busyness; week = "четверг"
    elif week == "четверг": freenees = random.randint(4,6) - busyness; week = "пятница"
    elif week == "пятница": freenees = random.randint(8,10) - busyness; week = "суббота"
    elif week == "суббота": freenees = random.randint(8,10) - busyness; week = "воскресенье"
    elif week == "воскресенье": freenees = random.randint(4,6) - busyness; week  = "понедельник"
    print(f"Наступил новый день! Сегодня ваша занятость: {busyness},")
    print(f"поэтому у вас есть {freenees} часов свободного времени.")
    print(f"А по счёту сегодня {day}-й день, или {week}. \n"); main()

class saving:
    def exit():
        saving.save()
        exit()
    def save():
        global views, money, subscribers, boost, likes, monetization, freenees, busyness, day, week, channel_name
        save = {
            "freenees": freenees, "busyness": busyness, "day": day, "week": week,
            "views": views, "money": money, "likes": likes, "boost": boost,
            "subscribers": subscribers, "monetization": monetization,
            "dislikes": dislikes, "channelName": channel_name}
        try:
            with open("data.json", "w+") as fh: json.dump(save, fh)
        except: input("Не удалось сохранить сохранение. ")
    def beginning():
        global channel_name
        input("друг издевается надо мной "); input("говорит что у него есть канал с одной тысячей подписчиков... ")
        input("я его точно смогу обогнать, ведь это не сложно, да? ")
        channel_name = input("название канала: ")
        while len(channel_name) < 2 or len(channel_name) > 31: channel_name = input("(от 3 до 30 символов) название канала: "); system("cls")
        input("(цель: 1.000.000 подписчиков) "); system("cls"); new_day()
    def end():
        global subscribers
        endStory = [
            "(встреча друга и меня) ", "я: привет ", "друг: ну привет, лошок. ",
            "я: почему ты меня всегда принижаешь? ",
            "друг: потому что у тебя нету канала, а у меня растущий канал ",
            "я: а если я скажу, что у меня уже больше, чем 1к подписчиков? ",
            "друг: не верю, да и у меня в отличии от тебя уже 2,5к ",
            f"я: точно, забыл уточнить, что у меня так-то уже {subscribers} ",
            "друг: пффф, да как у такого лоха может быть так мно- ",
            "чего? откуда у тебя, бездаря, так много подписчиков? ",
            "а-а-а, накрутка) таких всегда банит ютуб ",
            "я: только ты не учёл просмотры, теперь бездарь тут только ты :D ",
            "друг: ... ", "да иди ты нахер ", '("друг" убегает) ',
            "я: странно, вроде взрослый чел, а обиделся и убежал ",
            "ладно, в любом случае, вернусь к работе "]
        for text in endStory: input(text)
    def load():
        global views, money, subscribers, boost, likes, dislikes, monetization, freenees, busyness, day, week, channel_name
        try:
            with open('data.json') as f: data = json.load(f)
            views = data['views']; money = data['money']; subscribers = data['subscribers']
            boost = data['boost']; likes = data['likes']; dislikes = data['dislikes']
            monetization = data['monetization']; freenees = data['freenees']; busyness = data['busyness']
            day = int(data['day']); week = data['week']; channel_name = data['channelName']
        except FileNotFoundError: saving.beginning()

class shop:
    @staticmethod
    def main(money, boost):
        system("cls")
        print("Улучшения - важный элемент игры. Купив любое улучшение вы ускоряете развитие.")
        choice = input("0. Выход\n1. Комплектующие\n2. Периферия\n3. Настройка\nВыбери категорию: ")
        if choice == "0": system("cls"); main()
        elif choice == "1": money, boost = shop.parts(money, boost)
        elif choice == "2": money, boost = shop.periphery(money, boost)
        elif choice == "3": money, boost = shop.other(money, boost)
        system("cls"); return money, boost  # возвращаем измененные значения
    @staticmethod
    def parts(money, boost):
        system("cls")
        text = [f"Монеты: {money}", "0. Выход", "1. Старый компьютер - 2500 монет", "2. Бюджетный компьютер - 7500 монет", "3. Стандартный ноутбук - 12500 монет",
                "4. Хороший компьютер - 15000 монет", "5. Ультрабук - 22500 монет", "6. Мощный компьютер - 30000 монет"]
        for i in text: print(i)
        choice = input("Выбери устройство: ")
        if choice == "0": shop.main(money,boost)
        prices = {"1": 2500, "2": 7500, "3": 10000, "4": 15000, "5": 22500, "6": 30000}
        try:
            if choice in prices: price = prices[choice]
        except:
            print("Неверный выбор!"); shop.main(money,boost)
        if price > money: print("Недостаточно монет! Вы можете зарабатывать монеты ")
        else: money -= price; boost += price / 10000; print(f"Успешная покупка! Теперь ваш множитель (к просмотрам) - {boost}, остаток монет - {money}")
        input("(Enter для продолжения) "); system("cls")
        return money, boost  # возвращаем измененные значения
    @staticmethod
    def periphery(money, boost):
        system("cls")
        text = [f"Монеты: {money}", "0. Выход", "1. Улучшенная мышь - 5000 монет", "2. Бизнес клавиатура (мембранка) - 8000 монет", 
                "3. Геймерская мышь - 10000 монет", "4. Механическая клавиатура - 15000 монет",
                 "5. Геймерская наушники - 20000 монет", "6. Веб-камера Full HD - 25000 монет"]
        for i in text: print(i)
        choice = input("Выбери устройство: ")
        if choice == "0": shop.main(money,boost)
        prices = {"1": 5000, "2": 8000, "3": 10000, "4": 15000, "5": 20000, "6": 25000}
        if choice in prices: price = prices[choice]
        else: print("Неверный выбор!")
        if price > money: print("Недостаточно монет!")
        else: money -= price; boost += int(price / 2000); print("Успешно!")
        input("(Enter для продолжения) "); system("cls")
        return money, boost  # возвращаем измененные значения
    @staticmethod
    def other(money, boost):
        system("cls")
        text = [f"Монеты: {money}", "0. Выход", "1. Настройка OBS - 15000 монет", "2. Хромакей - 20000 монет", "3. Студия - 1000000 монет"]
        for i in text: print(i)
        choice = input("Выбери устройство: ")
        if choice == "0": shop.main(money,boost)
        prices = {"1": 15000, "2": 20000, "3": 1000000}
        if choice in prices: price = prices[choice]
        else: print("Неверный выбор!")
        if price > money: print("Недостаточно монет!")
        else: money -= price; boost += int(price / 2000); print("Успешно!")
        input("(Enter для продолжения) "); system("cls")
        return money, boost  # возвращаем измененные значения

class video:
    def main():
        global freenees, busyness
        if freenees >= 2+busyness: freenees -= 2+busyness
        else: system("cls"); print("Времени не хватит... Похоже, нужно заняться этим завтра\n"); main()
        system("cls")
        title = input("Название видео: ")
        while len(title) > 30 or len(title) < 3: system("cls"); title = input("Название видео (3-30 символов): ")
        video.create(title)
    def create(title):
        global views, money, subscribers, likes, dislikes, boost, freenees, popularity, monetization
        for i in range(100): system("cls"); print(f"{i}% видео снято"); sleep(random.randint(20,200)/1000)
        viewersEarned = int(views / random.randint(1,50) * (boost + popularity) + random.randint(1,10) * 10)
        subscribersEarned = int(viewersEarned / 50); likesEarned = int(viewersEarned/20); dislikesEarned = int(likesEarned / 8)
        if monetization != False: moneyEarned = int(viewersEarned / monetization); subscribers += subscribersEarned
        else: moneyEarned = 0
        views += viewersEarned; likes += likesEarned; dislikes += dislikesEarned; money += moneyEarned
        print("\nВидео снято было снято, смонтированно и выложено. А вот и его статистика:")
        input(f"Просмотры: {viewersEarned}\nПодписки: {subscribersEarned}\nЛайки: {likesEarned}\nДизлайки: {dislikesEarned}\nМонеты: {moneyEarned} \n")
        system("cls")

def show_statistics():
    global views, money, subscribers, likes, dislikes, boost
    system("cls")
    stats = ["Статистика:",f"Монеты: {money}", f"Просмотры: {views}", f"Подписчики: {subscribers}",
            f"Лайки: {likes}", f"Дизлайки: {dislikes}", f"Множитель к просмотрам: {boost}\n"]
    for i in stats: print(i)

class work:
    def main():
        global money, busyness, freenees; system("cls")
        if freenees >= 3+busyness: freenees -= 3+busyness
        else: system("cls"); print("Времени не хватит... Похоже, нужно заняться этим завтра\n"); main()
        choice = input("Чтобы получить монет, нужно выйграть мини-игру: \n1. Угадай число\n2. Камень, ножницы, бумага\n3. Виселица\nВведите номер игры (1-3): ")
        system("cls")
        if choice == "1": money += work.GuessTheNumber()
        elif choice == "2": money += work.RockPaperScissors()
        elif choice == "3": money += work.Hangman()
        else: print("Неправильный выбор игры."); freenees += 3+busyness
    def GuessTheNumber():
        global money
        print("Угадай число от 1 до 100 за 10 попыток!")
        number = random.randint(1,100); choice = int(input("Ваше число: ")); attempts = 10
        while choice != number:
            attempts -= 1
            if choice > number: print(f"Загаданное число меньше. Попытки: {attempts}. Прошлое число: {choice}.")
            elif choice < number: print(f"Загаданное число больше. Попытки: {attempts}. Прошлое число: {choice}.")
            if attempts == 0: print("Попытки закончились, а число было '{number}'."); break
            choice = int(input("Ваше число: ")); system("cls")
        input(f"Ты угадал число {number} и получил {attempts * 200} монет. А остаток попыток был: {attempts}")
        return attempts * 200
    def RockPaperScissors():
        choices = ["1", "2", "3"]; global freenees, busyness
        choice = input("0. Выход\n1. Камень\n2. Ножницы\n3. Бумага\nВаш выбор: ")
        choiceRandom = random.choice(choices)
        if choice not in choices: print("Неправильный выбор. Выбери действие с помощью цифр 1-3"); return 0
        system("cls")
        input(f"Вы выбрали: {choice}\nКомпьютер выбрал: {choiceRandom} ")
        if choice == choiceRandom: input("Ничья! Дам ещё одну попытку"); freenees += 3+busyness; work.main()
        elif (choice == "1" and choiceRandom == "2") or \
            (choice == "2" and choiceRandom == "3") or \
            (choice == "3" and choiceRandom == "1"): input("Вы выиграли 1000 монет! Нажмите Enter: "); system("cls"); return int(1000)
        else: input("Проигрыш! Может, в следующий раз?"); system("cls"); return 0
    def Hangman():
        words = [
            "яблоко", "банан", "морковь", "собака", "слон","маяк",
            "цветок", "виноград", "дом", "мороженое", "куртка",
            "кенгуру", "лимон", "мышь", "лапша", "апельсин",
            "пингвин", "ковёр", "кролик", "клубника", "дерево",
            "зонт", "скрипка", "арбуз", "ксилофон", "якорь"]
        word = random.choice(words)
        guessed, attempts = [], 10 # Базовые значения
        while True: # Основной цикл мини-игры
            display = ""
            for letter in word:
                if letter in guessed: display += letter + " "
                else: display += "_ "
            print(f"Отгаданное слово - {display}, осталось {attempts} попыток.")
            guess = input("Буква: ").lower()
            system("cls")
            if "_" not in display: return 1000
            elif attempts == 0: return 0
            elif guess in guessed: print("Буква уже отгадана, попробуй другую"); continue
            elif len(guess) != 1 or not guess.isalpha(): print("Нужно подбирать слово по одной букве"); continue
            guessed.append(guess)
            if guess not in word: print("Буквы нет в слове, попробуй другую"); attempts -= 1

def monetize():
    system("cls"); global subscribers, monetization
    monetizationText = [
        "Монетизация",
        "Выберите способ монетизации:",
        "0. Назад",
        "1. Монета за 1000 просмотров (1 тысяча подписчиков)",
        "2. Монета за 500 просмотров (10 тысяч подписчиков)",
        "3. Монета за 100 просмотров (500 тысяч подписчиков)"]
    for i in monetizationText: print(i)
    choice = input("Ваш выбор: ")
    if choice == "0": system("cls"); main()
    elif choice == "1":
        if monetization > 1000 or monetization == False:
            if subscribers >= 1000: monetization = 1000; input("Заявку приняли!")
            else: input("Заявку отклонили из-за недостатка подписчиков"); monetize()
        else: input("Это неактуально для вас, и вы решили отказаться от этого"); monetize()
    elif choice == "2":
        if monetization > 500 or monetization == False:
            if subscribers >= 10000: monetization = 500; input("Заявку приняли!")
            else: input("Заявку отклонили из-за недостатка подписчиков"); monetize()
        else: input("Это неактуально для вас, и вы решили отказаться от этого"); monetize()
    elif choice == "3":
        if monetization > 100 or monetization == False:
            if subscribers >= 50000: monetization = 100; input("Заявку приняли!")
            else: input("Заявку отклонили из-за недостатка подписчиков"); monetize()
        else: input("Это неактуально для вас, и вы решили отказаться от этого"); monetize()

def checkTime(take):
    global freenees, busyness
    if freenees >= take + busyness: return True
    else: return False

def main():
    global money, boost, freenees
    while True:
        if subscribers >= 1000000: saving.end()
        info = ["Добро пожаловать в симулятор ютубера!", f"Свободное время: {freenees} часов.", f"Также у меня есть {money} монет.",
        "\n0. Выход", f"1. Снять видео ({2+busyness} часа)", "2. Статистика канала", "3. Улучшения",
        f"4. Работа ({3+busyness} часа)", "5. Монетизация", "6. Новый день"]
        for text in info: print(text)
        choice = input("Номер действия: ")
        if choice == "0": saving.exit()
        elif choice == "1": video.main()
        elif choice == "2": system("cls"); show_statistics()
        elif choice == "3": money,boost = shop.main(money,boost)
        elif choice == "4": work.main()
        elif choice == "5": monetize()
        elif choice == "6": new_day()
        else: system("cls"); print("Неправильный ввод")

if __name__ == "__main__":
    saving.load()
    system("cls")
    main()