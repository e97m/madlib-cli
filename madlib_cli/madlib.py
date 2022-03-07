import re

def read_template(path):
    # try:
        with open(path, 'r') as f:
            the_text = f.read()
        return the_text
    # except FileNotFoundError:
        # return ('The file is not found')


def parse_template(str):
    words_list = tuple(re.findall(r'{(.*?)}', str))
    new_str = re.sub(r'{(.*?)}', '{}', str)
    return new_str, words_list



def take_inputs(words_list):
    # This function is Zaid's idea, I sow it and found that it is reasanable to add it to my code
    taken_inputs = []
    for word in words_list:
        new_input = input(f'Enter a/an {word} > ')
        taken_inputs.append(new_input)
    return taken_inputs


def merge(str, inputs):
    final_text = str.format(*inputs)
    return final_text


print('''
*********************************************************************
* Hi... This is madlip game, all you have to do is insert one word  *
*   everytime the game asks you. Pay attention to the type of the   *
*                     reqiered word everytime.                      *
*********************************************************************
''')

if __name__ == "__main__": 
    parsed_text, words_list = parse_template(read_template("./assets/dark_and_stormy_night_template.txt")) # you can try the path: ./assets/midlib.txt
    taken_inputs = take_inputs(words_list)
    print((f'\n*********************************************************************\n The final result is: \n {merge(parsed_text,taken_inputs)} \n'))
