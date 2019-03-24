from src.command.create_block import CreateBlock
from src.command.config import Config
from src.command.remove_block import RemoveBlock
from src.helpers import *

settings = Config().get_settings()

if '--help' in sys.argv:
    show_help()
elif 'init' in sys.argv:
    Config().create_config()
elif search_key('--rm'):
    exit('remove')
elif search_key('config.'):
    if 'config.ext_tpl_block' in sys.argv:
        Config().change('ext_tpl_block')
    elif 'config.path_to_blocks' in sys.argv:
        Config().change('path_to_blocks')
    elif 'config.default_tpl_content' in sys.argv:
        Config().change('default_tpl_content', ['0', '1'])
    elif 'config.default_block_content' in sys.argv:
        Config().change('default_block_content', ['1', '0'])
    else:
        exit("\n \033[91m Not find config " + sys.argv[1] + " \n \033[0m \npath_to_blocks\n"
                                                            "default_tpl_content\ndefault_block_content\next_tpl_block")
else:
    CreateBlock(settings).run()

# alias block='python3 /home/egor/www/skeleton/block/block.py'
