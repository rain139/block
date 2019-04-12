from src.command.create_block import CreateBlock
from src.command.config import Config
from src.command.remove_block import RemoveBlock
from src.command.help import Help
import subprocess
from src.helpers import *


class block:
    def __init__(self):
        dir_ = __file__.replace('block.py', '')
        command = 'cd ' + dir_ + ' && git checkout master && git pull'
        subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)

    def route(self):
        if '--help' in sys.argv:
            Help().run()
        elif 'init' in sys.argv:
            Config(True).create_config()
            exit('Success')
        elif search_key('--rm'):
            RemoveBlock(Config().get_settings()).run()
            exit('Success')
        else:
            CreateBlock(Config().get_settings()).run()
            exit('Success')


block().route()
