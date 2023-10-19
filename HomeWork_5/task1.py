import random
import time


# функция проверки на корректность введенного числа
def is_valid(num):
    return num.isdigit() and 1 <= int(num) <= 10

# функция приветствия
def is_hello():
    print("🎲 Добро пожаловать в игру!🎲")
    time.sleep(1)
    print("Я загадываю число, а ты попробуй угадай🤔")
    time.sleep(1)

# функция ввода и проверки числа на корректность
def input_number():
    while True:
        num = input("Введите загаданное число от 1 до 10: ")
        if is_valid(num):
            return int(num)
        else:
            print("А может быть все-таки введем целое число от 1 до 10? 🤷‍♀️")
            time.sleep(1)

def play_game(random_num):
    while True:
        num = input_number()

        if num == random_num:
            print("🎉 Вы угадали, поздравляем! 👍")
            time.sleep(1)
            print("Спасибо, что играли в нашу игру. Еще увидимся... 😜")
            break
        elif num < random_num:
            print("😔 Ваше число меньше загаданного, попробуйте еще разок 🤔")
        else:
            print("😔 Ваше число больше загаданного, попробуйте еще разок 🤔")

def game_reply():
    while True:

        replygame = input("Вы хотите сыграть снова? 🤖 напишите да/нет: ")
        if replygame == "да":
            game()
        elif replygame == "нет":
            print("Конец игры, всего хорошего! 👌")
            break
        else:
            print("🚨 🚧 ☔ Некорректный ввод. Пожалуйста, ответь 'да' или 'нет'")

def game():
    is_hello()
    random_num = random.randint(1, 10)
    play_game(random_num)
    game_reply()
game()