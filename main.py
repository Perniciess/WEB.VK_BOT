import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import random



# Функция для отправки сообщений
def send_message(user_id, message, keyboard=None):
    post = {
        "user_id": user_id,
        "message": message,
        "random_id": random.randint(0, 2 ** 64)}
    if keyboard != None:
        post["keyboard"] = keyboard.get_keyboard()
    else:
        post = post
    vk_session.method("messages.send", post)


# Главная функция со всей логикой бота
def main():
    for event in longpoll.listen():
        keyboard = VkKeyboard()
        keyboard.add_button('Помощь', VkKeyboardColor.POSITIVE)
        keyboard.add_button('Сайт', VkKeyboardColor.PRIMARY)
        if event.type == VkBotEventType.MESSAGE_NEW:
            text = event.obj.message['text'].lower()
            user_id = event.obj.message['from_id']
            if text == "start" or text == 'начать' or text == 'старт':
                send_message(user_id, "Здравствуйте!", keyboard)
            elif text == "помощь":
                send_message(user_id, 'Мы обязательно Вам поможем')
            elif text == "сайт":
                send_message(user_id, 'http://libraryonline1.herokuapp.com/')


if __name__ == '__main__':
    main()
