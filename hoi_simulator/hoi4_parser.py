from hoi_simulator import construction_types, modifier_types, modifier_classes, economy_laws, modifier, ideologies, trade_laws, requirements, conscription_laws, focus

import math

#This is for parsing a file to create the focuses of a country

#Parses a national_focus file for a specific country to create all the focuses for set country
def parse_file(path): 
    file = open(path, "r")
    text = file.read()

    text_without_comments = remove_comments_from_text(text)

    target = "focus = {"
    index = 0

    start_focus = ""
    next_focus = ""

    while index < len(text): 
        start_focus += text[index]
        if len(start_focus) > 5: 
            if text[index-8:index+1] == target: 
                focus_text, extra_index = find_block_end(text[index-8:])
                index += extra_index
                handle_focus(focus_text)
        index += 1

def remove_comments_from_text(text): 
    lines = text.splitlines(True)
    new_text = ""
    for line in lines: 
        comment_index = line.find("#")
        if comment_index != -1: 
            new_text += line
        else: 
            #Adds eveything before the comment. THe \n is because that would become part of the comment, but it is still needed to get to the next line
            new_text += line[:comment_index] + "\n"
    return new_text

#Finds when a focus block ends, where the whole focus block can be sent to handle focus
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

#Handles a focus block to produce a focus in the simulator format
def handle_focus(text): 
    new_focus = create_new_focus()
    id_index = text.find("id = ")
    if id_index != -1: 
        #Since id_index starts at the i, in "id = ", we start after it is written instead
        id_index += len("id = ")
        focus_id = ""
        while id_index < len(text): 
            if text[id_index] == " " or text[id_index] == "\n": 
                break
            else: 
                focus_id += text[id_index]
            id_index += 1
        new_focus.id = focus_id

    #Prerequisites can either be written in different prerequisite blocks, meaning it is an and condition, or in the same block, meaning an or condition
    prereq_index = 0
    while True: 
        prereq_index = text.find("prerequisite = { focus = ", prereq_index)
        if prereq_index == -1: 
            break
        prereq_index += len("prerequisite = { focus = ")
        prerequisites_id = ""
        #The general idea is to have lists inside a list to distinguish between or and and. In the file, at least one thing in a prerequisite block is required, meaning more focuses in one prerequisite block means an or between those focuses, while a new prerequisite block is instead an and between the other prerequisite blocks
        current_prerequisite_statement = []
        while prereq_index < len(text): 
            if text[prereq_index] == " " or text[prereq_index] == "\n":
                if prerequisites_id != "": 
                    current_prerequisite_statement.append(prerequisites_id)
                prerequisites_id = ""
                if text[prereq_index + 1] == "}": 
                    break
                if text[prereq_index + 1] == "f": 
                    prereq_index += len("focus = ")
            else: 
                prerequisites_id += text[prereq_index]
            prereq_index += 1
        new_focus.prerequisite_focuses.append(current_prerequisite_statement)

    mut_excl_index = text.find("mutually_exclusive = { focus = ")
    if mut_excl_index != -1: 
        mut_excl_index += len("mutually_exclusive = { focus = ")
        mut_excl_focuses_id = ""
        while mut_excl_index < len(text): 
            if text[mut_excl_index] == " ": 
                new_focus.mutually_exclusive_focuses.append(mut_excl_focuses_id)
                mut_excl_focuses_id = ""
                if text[mut_excl_index + 1] == "}": 
                    break
                if text[mut_excl_index + 1] == "f": 
                    mut_excl_index += len("focus = ")
            else: 
                mut_excl_focus_id += text[mut_excl_index]
            mut_excl_index += 1

    






    


def create_new_focus(): 
    return focus.Focus(
        id=None, 
        name=None,
        duration=None,
        prerequisite_focuses={}, 
        mutually_exclusive_focuses={}, 
        requirements={}, 
        effects=None
    )
