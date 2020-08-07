#users/ASUS/chatbot.venv/python3

import random

from chat_bot import handlers

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


class UserState:
    """Состояния пользователя внутри сценария"""
    def __init__(self, scenario_name, step_name, context=None):
        self.scenario_name = scenario_name
        self.step_name = step_name
        self.context = context or {}


class Bot:
    """
      Use python 3.8
      Сценарий регистрации на конференцию "Skillbox Conf" через vk.com

        Поддерживает ответы на вопросы про дату, место проведание и сценарий регистрации:
        - спрашиваем имя
        - спрашиваем email
        - говорим об успешной регистрации
        Если шаг не пройден, задаем уточняющий вопрос пока шаг не будет пройден.
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
        print(self.long_poller, '+++')
        self.api = self.vk.get_api()
        self.user_states = dict() # user_id -> UserState

    def run(self):
        """
        Запуск бота
        """
        for event in self.long_poller.listen():
            print(event, '+++')
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
        if event.type != VkBotEventType.MESSAGE_NEW:
            log.info('Мы не можем обрабатывать событие такого типа %s', event.type)
            return
        user_id = event.object.peer_id
        text = event.object.text
        print(user_id, text, '+++')
        if user_id in self.user_states:
            text_to_send = self.continue_scenario(user_id, text)
        else:
            #search intent
            for intent in settings.INTENTS:
                log.debug(f'User gets {intent}')
                if any(token in text.lower() for token in intent['tokens']):
                    if intent['answer']:
                        text_to_send = intent['answer']
                    else:
                        text_to_send = self.start_scenario(user_id, intent['scenario'])
                    break
            else:
                text_to_send = settings.DEFAULT_ANSWER
        self.api.messages.send(message=text_to_send,
                               random_id=random.randint(0, 2 ** 20), peer_id=user_id)

    def start_scenario(self, user_id, scenario_name):
        scenario = settings.SCENARIOS[scenario_name]
        first_step = scenario['first_step']
        step = scenario['steps'][first_step]
        text_to_send = step['text']
        self.user_states[user_id] = UserState(scenario_name=scenario_name, step_name=first_step)
        return text_to_send

    def continue_scenario(self, user_id, text):
        state = self.user_states[user_id]
        steps = settings.SCENARIOS[state.scenario_name]['steps']
        step = steps[state.step_name]
        handler = getattr(handlers, step['handler'])
        if handler(text=text, context=state.context):
            # next step
            next_step = steps[step['next_step']]
            text_to_send = next_step['text'].format(**state.context)
            if next_step['next_step']:
                state.step_name = step['next_step']
                # switch to next step
            else:
                # finish scenario
                log.info('Зарегистрирован: {name} {email}'.format(**state.context))
                self.user_states.pop(user_id)
        else:
            # retry current step
            text_to_send = step['failure_text']
        return text_to_send

# log.debug('отправляяем сообщение назад')
#             self.api.messages.send(message='Я тебя понял. Возвращаю тебе твое слово.  ' + event.object.text,
#                                    random_id =random.randint(0, 2**20), peer_i= event.object.peer_id)


if __name__ == '__main__':
    configure_log()
    bot = Bot(settings.GROUP_ID, settings.TOKEN)
    bot.run()