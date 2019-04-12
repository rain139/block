import os

class Help:
    def run(self):
        message = ''

        message += '\nConfig:\n'
        message += '\nProject confing in '+os.path.abspath('create_block.conf')+'\n'
        message += '\npath_block_class   --------------------------------- where the blocks class are located \n'
        message += '\npath_to_blocks_views   -------------------------- where the blocks template are located \n'
        message += '\next_tpl_block   ----------------------------------- extension template block (tpl.html) \n'
        message += '\ndefault_tpl_content   -------------------- default function with helpers in views (1/0) \n'
        message += '\ndefault_block_content   ------------------ default function with helpers in class (1/0) \n'

        message +='\nСommands:\n'
        message += '\nblock init    -------------------------------------------------------- install script block in this project\n'
        message += '\nblock init --ext   ----------------------------- install script block in this project with extension config\n'
        message += '\nblock [class name block*] [name block*] [visible:1 or 0, default: 1] [sub class names]  -------- create block\n'
        message += '\nblock [class name block*] --rm     ------------------------------------------------------------ remove block\n'
        message += '\n* - required params\n'
        exit(message)