from src.command.create_block import CreateBlock
from src.command.config import Config
from src.command.remove_block import RemoveBlock
from src.helpers import *


if '--help' in sys.argv:
    show_help()
elif 'init' in sys.argv:
    Config(True).create_config()
    exit('Success')
elif search_key('--rm'):
    RemoveBlock(Config().get_settings()).run()
    exit('Success')
else:
    CreateBlock(Config().get_settings()).run()
    exit('Success')


# alias block='python3 /home/egor/www/skeleton/block/block.py'
