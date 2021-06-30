# chat/consumers.py
from django.core.checks import messages
from channels.generic.websocket import WebsocketConsumer
import json
from .models import Car

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # проверяем корректность запроса
        if message[0] == '#':
            search_ad = message[1:]  # убираем '#'
            
            # проверяем есть ли указанное сообщение
            all_cars = Car.objects.all()
            for ad in all_cars:
                if search_ad == ad.title:
                    # Формируем сообщение - информацию о машине
                    message = ('Название машины: ' + str(ad.title) + '\n' + 
                                'Описание: ' + str(ad.description) + '\n' + 
                                'Цена: ' + str(ad.price) + '\n' +
                                'Категория: ' + str(ad.category) + '\n' + 
                                'Тип двигателя: ' + str(ad.type_fuel) + '\n' + 
                                'Объём двигателя: ' + str(ad.engine_volume))
                    
                else:
                    message = ("\nПо вашему запросу нечего не найдено.")
        else:
            message = ("\nВы ввели неверный запрос, добавте в начале знак '#'.")

        # отправляем в чат сообщение
        self.send(text_data=json.dumps({
            'message': message
        }))
