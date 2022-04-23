'''
    A main module.
'''
import game

stryiska = game.Room("вул. Стрийська")
stryiska.set_description("Темна і загадкова...")

kozelnytska = game.Room("вул. Козельницька")
kozelnytska.set_description(
    "Вже зовсім близько!.")

shevchenka = game.Room("пр.Т.Шевченка")
shevchenka.set_description(
    "Широкий проспект з світлими вітринами. Не блищько ще...")

syhiv = game.Room("Сихів")
syhiv.set_description(
    "Найстрашніше місце. Кажуть, тут вечорами ходять маньяки.\n\
Стоп, як ти узагалі потрапив до Сихова?!")

pid_dubom = game.Room("вул. Під дубом")
pid_dubom.set_description(
    "Ти добре погуляв з друзяками. Мабуть, треба уже в колегіум потихеньку.\n\
На-жаль, хильнув ти немало, тому доведеться трохи поблукати.")


pid_dubom.link_room(syhiv, "схід")
syhiv.link_room(pid_dubom, "захід")

stryiska.link_room(kozelnytska, "південь")
kozelnytska.link_room(stryiska, "північ")

shevchenka.link_room(syhiv, "північ")
syhiv.link_room(shevchenka, "південь")

stryiska.link_room(shevchenka, "захід")
shevchenka.link_room(stryiska, "схід")

hopnik = game.Enemy("Гопнік Петро", "П'яний і смердючий - якщо коротко.\n\
Втекти не вийде.")
hopnik.set_conversation("Е, малий! А шо ти там-о маєш?.")
hopnik.set_weakness("Львівське 1715")
syhiv.set_character(hopnik)

student = game.Enemy(
    "Студент-рекламщик", "Звичайний студент політеху, що підробляє роздаванням листівок")
student.set_conversation("Безліміт на дзвінки, 12 Гіг!")
student.set_weakness("20 гривень")
stryiska.set_character(student)

pyvo = game.Item("Львівське 1715")
pyvo.set_description("Хтось недопив і поставив під лавку Львівське 1715.")
pid_dubom.set_item(pyvo)

money = game.Item("20 гривень")
money.set_description("Під ногами лежали зелененькі 20 гривень. Халява!")
shevchenka.set_item(money)

current_room = pid_dubom
backpack = []

DEAD = False

while DEAD is False:

    if current_room == kozelnytska:
        print("Вітаю, ти досяг колегіуму цілим і неушкодженим!")
        break

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input(">>> ")

    if command in ["північ", "південь", "схід", "захід"]:
        if current_room.get_character() is None or current_room.get_character().is_defeated is True:
            # Move in the given direction
            current_room = current_room.move(command)
        else:
            print('Тікати нікуди!')
    elif command == "говорити":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "змагатись":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("Чим будемо відмазуватись?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.fight(fight_with) is True:
                    print("Ти виграв бій!")
                    current_room.character = None
                else:
                    # What happens if you lose?
                    print("На жаль, ти програв бій =(")
                    print("Це кінець...")
                    DEAD = True
            else:
                print("Ти не маєш " + fight_with)
        else:
            print("Нема з ким змагатись, охолонь.")
    elif command == "взяти":
        if item is not None:
            print("Ти взяв " + item.get_name() + " до свого рюкзака.")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("Нема що взяти.")
    else:
        print("Не розумію, що значить " + command)
