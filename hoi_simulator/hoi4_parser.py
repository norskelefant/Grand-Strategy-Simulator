from hoi_simulator import construction_types, modifier_types, modifier_classes, economy_laws, modifier, ideologies, trade_laws, requirements, conscription_laws

import math

def parse_file(path): 
    file = open(path, "r")
    text = file.read()

    target = "focus = {"
    index = 0

    start_focus = ""
    next_focus = ""

    while index < len(text): 
        start_focus += text[index]
        if len(start_focus) > 5: 
            if text[index-8:index+1] == target: 
                focus_text, extra_index = find_block_end(text[index-9:])
                index += extra_index
                handle_focus(focus_text)
        index += 1

def find_block_end(text): 
    index = 0
    parenthesis = 1
    focus_text = ""
    while index < len(text): 
        start_focus += text[index]
        if text[index] == '{': 
            parenthesis += 1
        if text[index] == '}': 
            parenthesis -= 1
        if parenthesis == 0: 
            return text[:index + 1], index
        index += 1      

def handle_focus(): 
    return None
