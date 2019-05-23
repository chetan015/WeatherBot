from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import warnings

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.run import serve_application
from rasa_core.utils import EndpointConfig
import requests
#from rasa_core.channels.console import ConsoleInputChannel


def run(serve_forever=True):
    # interpreter = RasaNLUInterpreter("models/nlu/default/current")
    # agent = Agent.load("models/dialogue", interpreter=interpreter)
    # print(agent.handle_text("Bye"))
    '''
    To load the rasa core model and handle messages
    interpreter = RasaNLUInterpreter("models/nlu/default/current")
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    agent = Agent.load("models/dialogue", interpreter=interpreter,action_endpoint=action_endpoint)
    print("Your bot is ready to talk! Type your messages here or send 'stop'")
    while True:
        a = input()
        if a == 'stop':
            break
        responses = agent.handle_text(a)
        for response in responses:
            print(response["text"])
    '''
    # To make post calls to http server and retreive messages. Make sure the rasa core server is up and running
    print("Your bot is ready to talk! Type your messages here or send 'stop'")
    while True:
        userResponse = input()
        if userResponse == 'stop':
            break
        response = requests.post('http://localhost:5005/conversations/default/respond',json={"query":userResponse}).json()
        botResponse = response[0]["text"]
        print(botResponse)

if __name__ == '__main__':
    warnings.filterwarnings(action='ignore', category=DeprecationWarning)
    utils.configure_colored_logging(loglevel="INFO")

    parser = argparse.ArgumentParser(
            description='starts the bot')

    parser.add_argument(
            'task',
            choices=["train-nlu", "train-dialogue", "run"],
            help="what the bot should do?")
    task = parser.parse_args().task

    # decide what to do based on first parameter of the script
    if task == "run":
        run()