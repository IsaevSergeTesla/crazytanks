import json
from random import randint
from time import sleep

from channels.generic.websocket import WebsocketConsumer


class Player():
    def __init__(self, name):
        self.name = name

def initiate_players();


def initiate_all():
    initiate_players()
    initiate_bases()

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        for i in range(1000):
            self.send(json.dumps({'message': randint(1, 100)}))
            sleep(1)

