import os
import sys
from src.helpers import *


class RemoveBlock:
    __settings = None
    __block_class = None
    __dir_blocks = None

    def __init__(self, settings):
        self.__settings = settings
        self.__set_dir_blocks()
        self.__set_block_class()

    def __set_dir_blocks(self):
        dir_blocks = os.path.abspath(self.__settings['path_block_class'].strip('/'))
        if os.path.isdir(dir_blocks):
            self.__dir_blocks = dir_blocks
        else:
            exit("\n \033[91m  Dir not found:  " + dir_blocks + "\n  \033[0m see " + os.path.abspath(
                'create_block.conf'))

    def __set_block_class(self):
        if 2 >= len(sys.argv):
            exit("\n \033[91m Error not find argument [class_name] --rm see --help \n \033[0m")
        else:
            self.__block_class = sys.argv[1]

    def run(self):
        self.__remove_with_settings()
        self.__remove_block_class()
        self.__remove_template()

    def __remove_block_class(self):
        path_block = self.__dir_blocks + "/block_" + self.__block_class + ".class.php"
        if os.path.isfile(path_block):
            os.remove(path_block)
        else:
            exit("\n \033[91m Not find file " + path_block + " \n \033[0m")

    def __remove_with_settings(self):
        path_settings = self.__dir_blocks + "/settings.php"
        file = open(path_settings, "r")
        lines = file.readlines()
        file.close()

        file = open(path_settings, "w")

        found_in_setting = False

        for line in lines:
            if line.find(', \'' + self.__block_class + '\'  ') == -1:
                file.write(line)
            else:
                found_in_setting = True

        if not found_in_setting:
            exit("\n \033[91m Not find block in " + self.__dir_blocks + "/settings.php" + " \n \033[0m")

    def __remove_template(self):
        path_template = os.path.abspath(
            self.__settings['path_to_blocks_views'].strip('/')) + "/block_" + self.__block_class + '.' + \
                        self.__settings['ext_tpl_block'].strip('.')

        if os.path.isfile(path_template):
            os.remove(path_template)
