#users/ASUS/chatbot.venv/python3

import random
try:
    import settings
except ImportError:
    exit('Do cp settings.py.default settings.py and TOKEN')
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import logging


log = logging.getLogger('bot')


def configure_log():
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter(" %(levelname)s %(message)s"))
    stream_handler.setLevel(logging.INFO)
    log.addHandler(stream_handler)

    file_handler = logging.FileHandler('bot.log', encoding='utf-8')
    file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s",
                                                 datefmt="%Y-%m-%d %H:%M:%S"))
    file_handler.setLevel(logging.DEBUG)
    log.addHandler(file_handler)
    log.setLevel(logging.DEBUG)


class Bot:
    """
    Echo bot для vk.com
    python 3.8
    """
    def __init__(self, group_id, token):
        """

        :param group_id: group id из группы vk
        :param token: секретный токен
        """
        self.group_id = group_id
        self.token = token

        self.vk = vk_api.VkApi(token=token)
        self.long_poller = VkBotLongPoll(vk=self.vk, group_id=self.group_id)
        self.api = self.vk.get_api()

    def run(self):
        """
        Запуск бота
        """
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception:
                log.exception('ошибка в обработке события')

    def on_event(self, event):
        """
        Отправляет сообщение назад, если это текст
        :param event: VkBotMessageEvent objects
        :return: None
        """
        if event.type == VkBotEventType.MESSAGE_NEW:
            log.debug('отправляяем сообщение назад')
            self.api.messages.send(message='Я тебя понял. Возвращаю тебе твое слово.  ' + event.object.text,
                                   random_id =random.randint(0, 2**20), peer_id = event.object.peer_id)
        else:
            log.info('Мы не можем обрабатывать событие такого типа %s', event.type)



if __name__ == '__main__':
    configure_log()
    bot = Bot(settings.GROUP_ID, settings.TOKEN)
    bot.run()