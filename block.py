from src.command.create_block import CreateBlock
from src.command.config import Config
from src.command.remove_block import RemoveBlock
from src.command.help import Help
from src.helpers import *
import sys


class block:
    __config = None

    def __init__(self):
        if not 'init' in sys.argv:
            self.__config = Config().get_settings()

    def route(self):
        if '--help' in sys.argv:
            Help().run()
        elif 'init' in sys.argv:
            Config(True).create_config()
            exit('Success')
        elif search_key('--rm'):
            RemoveBlock(self.__config).run()
            exit('Success')
        else:
            CreateBlock(self.__config).run()
            exit('Success')


block().route()

