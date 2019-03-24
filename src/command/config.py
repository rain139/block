import os
from src.helpers import *


class Config:
    __path = None

    def __init__(self, init=False):
        dir_conf = os.path.abspath('create_block.conf')
        if os.path.isfile(dir_conf) or init:
            self.__path = dir_conf
        else:
            exit(
                "\n \033[91m Block script not init. run: \n\n \033[0m    block init \n\n     block init --ext (for extension)\n")

    def change(self, key, value=[]):
        if 2 >= len(sys.argv):
            exit("\n \033[91m Not find argument (config." + key + " ARGUMENT) \n \033[0m")

        if value and not sys.argv[2] in value:
            allowed_arguments = to_string(value)
            exit("\n \033[91m Not valid argument [" + str(
                sys.argv[2]) + "] must be: " + allowed_arguments + " \n \033[0m")

        file = open(self.__path, "r")
        lines = file.readlines()
        file.close()

        file = open(self.__path, "w")

        for line in lines:
            if line.find(key):
                file.write(line)

        file.write(key + "=" + sys.argv[2] + "\n")
        file.close()

    def create_config(self):
        for_extension = False

        if 2 < len(sys.argv):
            if sys.argv[2] == '--ext':
                for_extension = True
            else:
                exit("\033[91m What is " + sys.argv[2] + "?\n\n --ext ?\n \033[0m")

        if not os.path.isfile(self.__path):
            with open(os.path.abspath('create_block.conf'), "w") as file:
                if for_extension:
                    file.write('path_block_class=blocks\n')
                    file.write('path_to_blocks_views=../../../templates/site\n')
                else:
                    file.write('path_block_class=app/blocks\n')
                    file.write('path_to_blocks_views=templates/site\n')

                file.write('ext_tpl_block=tpl.html\n')
                file.write('default_tpl_content=1\n')
                file.write('default_block_content=1\n')

                file.close()
        else:
            exit('\033[91m BLOCK IS INIT see ' + os.path.abspath('create_block.conf') + ' \033[0m')

    def get_settings(self):
        config = {}
        file = open(self.__path, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            split = line.split('=')
            config[split[0]] = split[1].strip('\n')

        return config
