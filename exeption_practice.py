# Перепишите функцию ask_user() из задания про while, чтобы она перехватывала 
# KeyboardInterrupt, писала пользователю "Пока!" и завершала работу при помощи 
# оператора break

dialog = {
    "Хорошо": "Спроси меня о чём-нибудь.",
    "Что делаешь?": "С тобой разговариваю",
    "Кушать хочешь?": "Нет, я же машина",
    "Я пошел спать": "Спокойной ночи"
}

def ask_user():
    try:
        while True:
            user_say = input("Как дела? ")
            
            for question in dialog:
            
                if user_say == question:
                    user_say = input(dialog[question] + ' ')

                    if dialog[question] == "Спокойной ночи":
                        return 0
       
            else:
                print("Не понимаю. Давай попробуем снова?")
    
    except KeyboardInterrupt:
        print(" Ну ладно, пока.")
        break

ask_user()