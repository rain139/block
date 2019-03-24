import os
from src.helpers import *


class Config:
    __path = None

    def __init__(self):
        self.__path = os.path.abspath('create_block.conf')
        self.create_config()

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
        if not os.path.isfile(self.__path):
            with open(os.path.abspath('create_block.conf'), "w") as file:
                file.write('path_to_blocks=templates/site\n')
                file.write('ext_tpl_block=tpl.html\n')
                file.write('default_tpl_content=1\n')
                file.write('default_block_content=1\n')
                file.close()

    def get_settings(self):
        config = {}
        file = open(self.__path, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            split = line.split('=')
            config[split[0]] = split[1].strip('\n')

        return config
