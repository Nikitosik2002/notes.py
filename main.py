import json
import datetime
import sys


def printer():
    dt_now = str(datetime.datetime.now())
    def print_start():
        print("Введите команду для работы с заметками.\n"
              "Если хотите создать новую заметку, введите: 'add'\n"
              "Если хотите прочитать заметки, введите: 'read'\n"
              "Если хотите изменить заметку, введите: 'modify'\n"
              "Если хотите удалить заметку, введите: 'del'\n"
              "Если хотите закончить работу с заметками, введтие: 'exit'\n")

    print_start()
    value = input("Введите команду: ")
    id = 0

    if value == 'add':
        with open("notes.json", 'r', encoding='utf-8') as f:
            data = json.load(f)
            for txt in data['notes']:
                id = txt['id']
        id = str(int(id)+1)

        heading = input("Введите заголовок заметки: ")
        middle = input("Введите основу заметки: ")
        print("Заметка успешно сохранена")

        dict_in_json = {
            "id": id,
            "date": dt_now,
            "heading": heading,
            "middle": middle
        }
        with open('notes.json', encoding='utf-8') as f_n:
            obj = json.load(f_n)
            obj['notes'].append(dict_in_json)

        with open('notes.json', 'w', encoding='utf-8') as f_w:
            json.dump(obj, f_w, ensure_ascii=False, indent=2)
        print()
        printer()
    elif value == "del":
        with open('notes.json', encoding='utf-8') as f_n:
            print(f_n.read())

        user_del = input("Напишите id заметки, которую хотите удалить: ")
        with open("notes.json", 'r', encoding='utf-8') as f:
            data = json.load(f)
            minimal = 0
            for txt in data['notes']:
                if txt["id"] == user_del:
                    data['notes'].pop(minimal)
                else:
                    None
                minimal += 1
            with open("notes.json", "w", encoding='utf-8') as out:
                json.dump(data, out, ensure_ascii=False, indent=2)
        print("Заметка успешно удалена")
        printer()
    elif value == "read":
        one_more = input("Если хотите прочитать все заметки, напишите: one\n"
                  "Ecли хотите прочитать одну заметку, напишите: more\n"
                  "Введите команду: ")
        if one_more == 'one':
            user_read = input("Напишите id заметки, которую хотите прочитать: ")
            with open("notes.json", 'r', encoding='utf-8') as f:
                data = json.load(f)
                for txt in data['notes']:
                    if txt["id"] == user_read:
                        print(txt)
                    else:
                        None
        elif one_more == 'more':
            with open('notes.json', encoding='utf-8') as f_n:
                print(f_n.read())
        else:
            print("Была введена неверная команда, попробуйте снова...\n")
        print()
        printer()

    elif value == "exit":
        sys.exit()

    elif value == "modify":
        with open('notes.json', encoding='utf-8') as f_n:
            print(f_n.read())
        user_read = input("Напишите id заметки, которую хотите изменить: ")
        mod = input("Если хотите поменять заголовок заметки, напишите: heading\n"
                    "Если хотите поменять основу заметки, напишите: middle\n")
        oldname = input("Введите старый заголовок\заметку: ")
        newname = input("Введите новый заголовок\заметку: ")
        with open("notes.json", 'r', encoding='utf-8') as f:
            data = json.load(f)
            for txt in data['notes']:
                if mod == 'heading':
                    if txt["id"] == user_read:
                        if txt["heading"] == oldname:
                            txt["heading"] = newname
                    else:
                        None
                elif mod == 'middle':
                    if txt["id"] == user_read:
                        if txt["middle"] == oldname:
                            txt["middle"] = newname
                    else:
                        None
            with open('notes.json', 'w', encoding="utf-8") as outfile:
                json.dump(data, outfile, ensure_ascii=False, indent=2)
        print()
        printer()
    else:
        print("Была введена неверная команда, попробуйте снова...\n")
        print()
        printer()


printer()
