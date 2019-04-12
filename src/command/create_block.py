import os
import sys
from src.helpers import *


class CreateBlock:
    __arguments = {}
    __settings = {}
    __path_blocks = None

    def __init__(self, settings):
        self.__settings = settings
        self.default_argument()
        self.__set_argument('Not find first argument (class_name)', 1, 'class_name')
        self.__set_argument('Not find second argument (name block)', 2, 'name_block')
        self.__set_argument(False, 3, 'visible', ['1', '0'])
        self.__set_argument(False, 4, 'sub_class_name')
        self.__edit_argument_sub_block()

    def __edit_argument_sub_block(self):
        if 'sub_class_name' in self.__arguments:
            sub_class_name = self.__arguments['sub_class_name'].split(',')
            self.__arguments['sub_class_name'] = list(map(lambda item: item.strip(), sub_class_name))

    def __set_argument(self, error, key, name_argument, value=[]):
        if key >= len(sys.argv) and error:
            exit("\n \033[91m " + error + " see --help \n \033[0m")
        elif value:
            if sys.argv[key].isdigit() and sys.argv[key] in value:
                self.__arguments[name_argument] = sys.argv[key]
            else:
                allowed_arguments = to_string(value)
                exit("\n \033[91m Not valid argument [" + str(
                    sys.argv[key]) + "] must be " + allowed_arguments + " \n \033[0m")
        else:
            self.__arguments[name_argument] = sys.argv[key]

    def default_argument(self):
        self.__arguments['visible'] = 1

    def run(self):
        self.__set_path_block()
        self.__create_block()
        self.__create_templates()
        self.__change_settings_block()
        self.__create_sub_blocks()

    def __set_path_block(self):
        dir_blocks = os.path.abspath(self.__settings['path_block_class'].strip('/'))
        if os.path.isdir(dir_blocks):
            self.__path_blocks = dir_blocks + "/block_" + self.__arguments['class_name'] + ".class.php"
        else:
            exit("\n \033[91m  Dir not found:  " + dir_blocks + "\n  \033[0m see " + os.path.abspath(
                'create_block.conf'))

    def __create_block(self):
        if not os.path.isfile(self.__path_blocks):
            with open(self.__path_blocks, "w") as file:
                file.write("<?php\n\n")
                file.write("class block_" + self.__arguments['class_name'] + " extends parent_block \n{")
                if int(self.__settings['default_block_content']):

                    if 'sub_class_name' in self.__arguments:
                        sub_class_name = self.__get_name_sub_block()
                        file.write(
                            '\n\n    public function getVars() \n    {\n       $vars = [];\n\n       $vars[\'title\'] = \'text\';\n       $vars[\'items\'] = \'items\';\n\n       return $vars;\n    }\n\n\n')
                        file.write(
                            '     public function typeItems($lang = 99, $name = \'\', $val = \'\')\n     {\n         return $this->typeBlocks($lang, $name, $val, [\'' + sub_class_name + '\']);\n     }\n\n\n\n')
                    else:
                        file.write(
                            '\n\n    public function getVars() \n    {\n       $vars = [];\n\n       $vars[\'title\'] = \'text\';\n       $vars[\'description\'] = \'textarea\';\n\n       return $vars;\n    }\n\n\n')
                        file.write(
                            '    //public function typeItems($lang = 99, $name = \'\', $val = \'\')\n    //{\n        //return $this->typeBlocks($lang, $name, $val, []);\n    //}\n\n\n\n')

                    file.write(
                        '    //public function typeSelect($lang = 99, $name = \'\', $val = \'\')\n    //{\n        //return parent::typeArray($lang, $name, $val, \'1;2;3;\');\n    //}\n\n')
                    file.write(
                        "//$langs = site_lang::getLangArray();\n//foreach ($langs as $k => $v) {\n     //$vars[\'labels_\' . strtolower($v[\'prefix\'])] = strtolower($v[\'prefix\']);\n\n//}")
                file.write("\n}")
                file.close()
        else:
            exit("\n \033[91m  Block " + self.__arguments['class_name'] + " exist!!\n \033[0m ")

    def __get_name_sub_block(self):
        return '\',\''.join(self.__arguments['sub_class_name'])

    def __change_settings_block(self):
        path_settings = os.path.abspath(self.__settings['path_block_class'].strip('/')) + "/settings.php"

        file = open(path_settings, "r")
        lines = file.readlines()
        file.close()

        file = open(path_settings, "w")

        for line in lines:
            if line != "];":
                file.write(line)

        file.write(
            "    , '" + self.__arguments['class_name'] + "'       =>   ['name' => '" + self.__arguments['name_block'] +
            "', 'visible' => " + str(self.__arguments['visible']) + "] \n];")
        file.close()

    def __create_templates(self):
        if int(self.__arguments['visible']):
            path = os.path.abspath(self.__settings['path_to_blocks_views'].strip('/'))
            name_tpl = '/block_' + self.__arguments['class_name'] + "." + self.__settings['ext_tpl_block'].strip('.')
            if os.path.isdir(path):
                with open(path + name_tpl, "w") as file:
                    if int(self.__settings['default_tpl_content']):
                        file.write('{*{assign var=geo value=$app->getBlocksPid("`$block_id`_items")}*}\n\n')
                        file.write(
                            '{*{assign var=gallery value=$app->blockGallery->getImages($block_id,\'gallery\')}*}\n\n')
                        file.write(
                            '{*{include file="blocks/blocks_content.html.tpl"  blocks=$place_objects[0][\'blocks\']}*}')
                file.close()
            else:
                os.remove(self.__path_blocks)
                exit("\n \033[91m  Dir  " + path + " not exits!!\n \033[0m see " + os.path.abspath('create_block.conf'))

    def __create_sub_blocks(self):
        if 'sub_class_name' in self.__arguments:
            sub_blocks = self.__arguments['sub_class_name']
            for class_name in sub_blocks:
                self.__arguments = {}
                self.__arguments['class_name'] = class_name
                self.__arguments['name_block'] = class_name
                self.__arguments['visible'] = 0
                self.run()
