import re

def read_template(path):
    '''
    A function to read files and retern the content of them, this function close the file automaticly after pulling the data from it.
    Input: the path of the file.
    Output: the content of the file.
    '''
    # try:
    with open(path, 'r') as f:
        the_text = f.read()
    return the_text
    # except FileNotFoundError:
        # return ('The file is not found')


def parse_template(str):
    '''
    A function to identify the missing words in the game and thier type, it is store them in a tuple then remove them from the test.
    Input: string
    Output: The new string without the type of the mixxing words a list of missing word's types
    ex: If you input (It was a {Adjective} {Noun}.) The output will be (It was a {} {}. , (Adjective, Noun))
    '''
    words_list = tuple(re.findall(r'{(.*?)}', str))
    new_str = re.sub(r'{(.*?)}', '{}', str)
    return new_str, words_list



def take_inputs(words_list):
    '''
    A function to take the missing words from the user.
    Input: a tuple of the missing words.
    Output: a list of the usre inputs.
    '''
    # This function is Zaid's idea, I sow it and found that it is reasanable to add it to my code. The rest code is totally mine.
    taken_inputs = []
    for word in words_list:
        new_input = input(f'Enter a/an {word} > ')
        taken_inputs.append(new_input)
    return taken_inputs


def merge(str, inputs):
    '''
    A function to merge the inout words that the user entered, with the strinng of the game.
    Input: the srting that have empty carly brackets (missing words), and the user input of these words.
    Output: the text without any missing words
    '''
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
    parsed_text, words_list = parse_template(read_template("./assets/madlib.txt"))
    taken_inputs = take_inputs(words_list)
    print((f'\n*********************************************************************\n The final result is: \n {merge(parsed_text,taken_inputs)} \n'))
