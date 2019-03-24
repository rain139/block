# Create block
Automatic created block and remove in fsm/amparo cms


# Install
    1. git clone https://github.com/rain139/block.git
    
    2. Create alias (command block) (see example)
    
    3. In your project home dir run command: block init or if extension: block init --ext
    
# Example create alias:
    1. nano ~ / .bashrc
    2. alias block='python3 /home/egor/www/skeleton/block/block.py'
    3. source ~/.bashrc

 #Commands
        block init    --------------------------------------- install script block in this project
        
        block init --ext   ------------ install script block in this project with extension config
        
        block [class name block] [name block] [visible:1 or 0, default: 1]   -------- create block
        
        block [class name block] --rm     ------------------------------------------- remove block

# Config

       Project confing in create_block.conf (when you run block init)
       
       path_block_class   --------------------------------- where the blocks class are located
       
       path_to_blocks_views   -------------------------- where the blocks template are located
       
       ext_tpl_block   ----------------------------------- extension template block (tpl.html)
       
       default_tpl_content   -------------------- default function with helpers in views (1/0)
        
       default_block_content   ------------------ default function with helpers in class (1/0) 